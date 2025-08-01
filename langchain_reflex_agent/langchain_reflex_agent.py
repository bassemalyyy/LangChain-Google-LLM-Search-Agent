import reflex as rx
from langchain import hub
from langchain.agents import initialize_agent
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from langchain_ollama import OllamaLLM
import asyncio



class State(rx.State):
    """The app state."""
    query: str = ""
    response: str = ""
    is_loading: bool = False
    error_message: str = ""
    
    def set_query(self, query: str):
        """Set the query value."""
        self.query = query
    
    async def submit_query(self):
        """Submit the query and get response from the agent."""
        if not self.query.strip():
            self.error_message = "Please enter a query."
            return
        
        self.is_loading = True
        self.error_message = ""
        self.response = ""
        yield
        
        try:
            # Google Search Tool
            serper_search = GoogleSerperAPIWrapper(
                serper_api_key="serper_api_key"
            )
            serper_tool = Tool(
                name="serper-search",
                description="Search Google for recent results.",
                func=serper_search.run
            )
            
            # Ollama LLM Integration
            ollama_llm = OllamaLLM(model="llama3.2")
            
            # Pull the prompt from Langchain Hub
            prompt = hub.pull("hwchase17/structured-chat-agent")
            
            # Define tools
            tools = [serper_tool]
            
            # Create the agent
            agent = initialize_agent(
                tools=tools,
                llm=ollama_llm,
                agent="zero-shot-react-description",
                verbose=True,
                prompt=prompt,
                handle_parsing_errors=True,
                max_iterations=5,
                early_stopping_method="generate"
            )
            
            # Run the agent
            response = await asyncio.to_thread(agent.run, self.query)
            
            if response:
                self.response = response
            else:
                self.error_message = "No response generated."
                
        except Exception as e:
            self.error_message = f"An error occurred: {str(e)}"
        
        finally:
            self.is_loading = False
            yield


def header() -> rx.Component:
    """Create the header component."""
    return rx.vstack(
        rx.heading(
            "Search Agent with Ollama",
            size="9",
            color="#ffffff",
            font_weight="800",
            text_align="center",
            text_shadow="2px 2px 4px rgba(0,0,0,0.5)",
            margin_bottom="2",
        ),
        rx.text(
            "Enter your query below to search using Google and get an AI-powered response.",
            size="5",
            color="#e2e8f0",
            text_align="center",
            max_width="600px",
            text_shadow="1px 1px 2px rgba(0,0,0,0.3)",
        ),
        spacing="4",
        align="center",
        padding_y="8",
    )


def search_form() -> rx.Component:
    """Create the search form component."""
    return rx.vstack(
        rx.input(
            placeholder="Enter your query here...",
            value=State.query,
            on_change=State.set_query,
            size="3",
            width="100%",
            max_width="600px",
            border_radius="12px",
            border="2px solid rgba(255,255,255,0.3)",
            background="rgba(255,255,255,0.9)",
            color="#1e293b",
            font_weight="500",
            _placeholder={"color": "#64748b"},
            _focus={
                "border_color": "#3b82f6",
                "box_shadow": "0 0 0 3px rgba(59, 130, 246, 0.3)",
                "outline": "none",
                "background": "#ffffff",
            },
        ),
        rx.button(
            rx.cond(
                State.is_loading,
                rx.hstack(
                    rx.spinner(size="3", color="white"),
                    rx.text("Processing...", color="white", font_weight="600"),
                    spacing="2",
                ),
                rx.hstack(
                    rx.icon("search", size=18, color="white"),
                    rx.text("Submit Query", color="white", font_weight="600"),
                    spacing="2",
                ),
            ),
            on_click=State.submit_query,
            disabled=State.is_loading,
            size="3",
            width="100%",
            max_width="200px",
            background="linear-gradient(45deg, #3b82f6 0%, #1d4ed8 100%)",
            border_radius="12px",
            border="none",
            cursor="pointer",
            _hover={
                "background": "linear-gradient(45deg, #2563eb 0%, #1e40af 100%)",
                "transform": "translateY(-2px)",
                "box_shadow": "0 10px 25px rgba(59, 130, 246, 0.4)",
            },
            _disabled={
                "opacity": "0.6",
                "cursor": "not-allowed",
            },
            transition="all 0.3s ease",
        ),
        spacing="5",
        align="center",
        width="100%",
    )


def response_section() -> rx.Component:
    """Create the response section component."""
    return rx.cond(
        State.error_message != "",
        rx.callout(
            State.error_message,
            icon="triangle_alert",
            color_scheme="red",
            size="2",
            width="100%",
            max_width="800px",
            background="rgba(239, 68, 68, 0.1)",
            border="1px solid rgba(239, 68, 68, 0.4)",
            color="#fca5a5",
        ),
        rx.cond(
            State.response != "",
            rx.card(
                rx.vstack(
                    rx.heading(
                        "AI Response:",
                        size="6",
                        color="#ffffff",
                        margin_bottom="3",
                        font_weight="700",
                        text_shadow="1px 1px 2px rgba(0,0,0,0.5)",
                    ),
                    rx.text(
                        State.response,
                        size="4",
                        color="#f1f5f9",
                        line_height="1.7",
                        white_space="pre-wrap",
                        text_shadow="1px 1px 1px rgba(0,0,0,0.3)",
                    ),
                    spacing="3",
                    align="start",
                ),
                width="100%",
                max_width="800px",
                padding="6",
                border_radius="16px",
                background="rgba(30, 41, 59, 0.8)",
                border="1px solid rgba(255, 255, 255, 0.2)",
                box_shadow="0 8px 32px rgba(0, 0, 0, 0.4)",
            ),
        ),
    )


# def index() -> rx.Component:
#     """The main page."""
#     return rx.box(
#         rx.container(
#             rx.vstack(
#                 header(),
#                 search_form(),
#                 response_section(),
#                 spacing="8",
#                 align="center",
#                 min_height="100vh",
#                 padding_y="8",
#             ),
#             max_width="1200px",
#             padding_x="4",
#             center_content=True,
#         ),
#         background="linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #334155 50%, #475569 75%, #64748b 100%)",
#         min_height="100vh",
#         width="100vw",
#         position="fixed",
#         top="0",
#         left="0",
#         overflow_y="auto",
#     )

def index() -> rx.Component:
    """The main page."""
    return rx.box(
        rx.container(
            rx.vstack(
                header(),
                search_form(),
                response_section(),
                spacing="8",
                align="center",
                min_height="100vh",
                padding_y="8",
                width="100%",  # Added this
                justify="center",  # Added this
            ),
            max_width="1200px",
            padding_x="4",
            center_content=True,
            width="100%",  # Added this
            display="flex",  # Added this
            justify_content="center",  # Added this
            align_items="center",  # Added this
        ),
        background="linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #334155 50%, #475569 75%, #64748b 100%)",
        min_height="100vh",
        width="100vw",
        position="fixed",
        top="0",
        left="0",
        overflow_y="auto",
        display="flex",  # Added this
        justify_content="center",  # Added this
        align_items="center",  # Added this
    )

# Add page
app = rx.App(
    style={
        "font_family": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif",
    }
)
app.add_page(index, title="Search Agent with Ollama")

if __name__ == "__main__":
    app._compile()
