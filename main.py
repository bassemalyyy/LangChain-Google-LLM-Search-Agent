#IMPORTS
#pip install langchain==0.1.13 langchainhub==0.1.15 google-api-python-client==2.124.0 python-dotenv==1.0.1 huggingface_hub==0.23.2

from langchain import hub
from langchain.agents import initialize_agent
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from langchain_community.llms import Ollama
import streamlit as st
import toml

# Load configuration from config.toml
config = toml.load("D:\\Titan Graduation Project\\.venv\\.streamlit\\config.toml")

# Extract theme values from the config file
primary_color = config['theme']['primaryColor']
background_color = config['theme']['backgroundColor']
secondary_background_color = config['theme']['secondaryBackgroundColor']

# Set the page configuration using Streamlit's `set_page_config` method
st.set_page_config(page_title="Search Agent with Ollama", page_icon=":mag_right:", layout="centered")

# Set custom background and text colors using HTML and CSS
st.markdown(
    f"""
    <style>
    div.stApp {{
        background-color: {background_color};
    }}
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
st.markdown('<div class="custom-title">Search Agent with Ollama</div>', unsafe_allow_html=True)
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

# Ollama LLM Integration
ollama_llm = Ollama(model="llama3.2")  # Replace with the specific model name

# Pull the prompt from Langchain Hub
# prompt = hub.pull("hwchase17/self-ask-with-search")
prompt = hub.pull("hwchase17/structured-chat-agent")

# Define tools
tools = [google_tool]

# Create the agent using initialize_agent
agent = initialize_agent(
    tools=tools,
    llm=ollama_llm,
    agent="zero-shot-react-description",
    verbose=True,
    prompt=prompt,
    handle_parsing_errors=True,  # Added this parameter
    max_iterations=5,  # Added max iterations
    early_stopping_method="generate"  # Added early stopping
)

# Query Input Section
query = st.text_input("Enter Your Query:")

# Button to Execute the Agent
if st.button("Submit Query"):
    if query.strip():
        st.markdown("<h3 style='color: black;'>Processing Your Query...</h3>", unsafe_allow_html=True)

        try:
            # Use the agent to run the query
            response = agent.run(query)
            if response:
                st.markdown("<h3 style='color: black;'>Response:</h3>", unsafe_allow_html=True)
                # st.write(response)
                st.markdown(f"<p style='color: black;'>{response}</p>", unsafe_allow_html=True)
            else:
                st.error("No response generated.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query.")
