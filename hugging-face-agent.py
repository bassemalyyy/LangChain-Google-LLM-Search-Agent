#IMPORTS
#pip install langchain==0.1.13 langchainhub==0.1.15 google-api-python-client==2.124.0 python-dotenv==1.0.1 huggingface_hub==0.23.2

import streamlit as st
import toml
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from langchain.llms import HuggingFaceHub
from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain import hub

# Load configuration from config.toml
config = toml.load("config.toml")

# Extract theme values from the config file
primary_color = config['theme']['primaryColor']
background_color = config['theme']['backgroundColor']
secondary_background_color = config['theme']['secondaryBackgroundColor']

# Set the page configuration using Streamlit's `set_page_config` method
st.set_page_config(page_title="Search Agent with HuggingFace", page_icon=":mag_right:", layout="centered")

# Set custom background and text colors using HTML and CSS
st.markdown(
    f"""
    <style>
    /* Background color for the whole page */
    div.stApp {{
        background-color: {background_color};
    }}
    /* Custom text styles */
    .custom-title {{
        color: {primary_color};
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }}

    .custom-subtitle {{
        color: {primary_color};
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
    }}
    /* Styling Streamlit buttons */
    div.stButton > button {{
        background-color: {primary_color} !important;
        color: white !important;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }}

    /* Styling input fields */
    input {{
        background-color: {secondary_background_color} !important;
        color: {primary_color} !important;
        border: 2px solid {secondary_background_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit Header
st.markdown('<div class="custom-title">Search Agent with HuggingFace</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-subtitle">Enter your query below to search using Google and get an AI-powered response.</div>', unsafe_allow_html=True)

# Google Search Tool
google_search = GoogleSearchAPIWrapper(
    google_api_key="AIzaSyDoMRCGeC9g-wPJRKq-mDUgH40tUqtLPsI",
    google_cse_id="b29af7a6a1b1c405e"
)
google_tool = Tool(
    name="google-search",
    description="Search Google for recent results.",
    func=google_search.run
)

# Hugging Face LLM Integration
# Add Hugging Face API token here (read from environment variable or other secure storage)
HUGGINGFACE_API_TOKEN = "HUGGINGFACE_API_TOKEN", "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"

# Hugging Face LLM Integration
llm = HuggingFaceHub(
    repo_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    model_kwargs={"temperature": 0.7, "max_length": 512},
    huggingfacehub_api_token=HUGGINGFACE_API_TOKEN  # Set the API token
)

# Pull Prompt for the Agent
prompt = hub.pull("hwchase17/structured-chat-agent")

# Create the Structured Chat Agent
agent = create_structured_chat_agent(llm, [google_tool], prompt)

# Create the Agent Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[google_tool],
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=7,
    max_execution_time=60
)

# Query Input Section
query = st.text_input("Enter Your Query:")

# Button to Execute the Agent
if st.button("Submit Query"):
    if query.strip():
        processing_message = st.empty()  # Create an empty slot for the message
        processing_message.markdown("<h3 style='color: black;'>Processing Your Query...</h3>", unsafe_allow_html=True)

        try:
            last_output = None  # Initialize variable to store the last valid output
            # Execute the query using the agent executor
            for _ in range(agent_executor.max_iterations):
                # Try to get the response from the agent
                response = agent_executor({"input": query})  # Pass query as a dictionary
                # Check if the response is valid and not empty
                if response and 'output' in response:
                    last_output = response['output']  # Store the last valid output
                    processing_message.markdown("<h3 style='color: black;'>Processing Query Done.</h3>", unsafe_allow_html=True)
                    st.markdown(f"<h3 style='color: black;'>Response:</h3><p style='color: black;'>{last_output}</p>", unsafe_allow_html=True)
                    break  # Break the loop as soon as a valid response is found
                else:
                    # Continue searching if no valid response is found
                    continue

            # If no valid response is found after all iterations, show an error message
            if not last_output:
                processing_message.markdown("<h3 style='color: black;'>Processing Query Done.</h3>", unsafe_allow_html=True)
                st.error("No valid response was generated.")
        except Exception as e:
            processing_message.markdown("<h3 style='color: black;'>Processing Query Done.</h3>", unsafe_allow_html=True)
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query.")
