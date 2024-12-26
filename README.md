# Streamlit Search Agent with Ollama 🔍

A powerful web application that combines Google Search capabilities with Ollama's LLM to provide AI-enhanced search responses. Built with Streamlit and LangChain, this application offers an intuitive interface for users to search and receive AI-processed answers.

## Features

- 🎯 Google Search integration through LangChain
- 🤖 Ollama LLM integration for intelligent response processing
- 💻 Clean, modern Streamlit interface with customizable theming
- ⚡ Real-time query processing and response generation
- 🛠️ Error handling and retry mechanisms
- ⚙️ Configurable search parameters and agent behavior

## Prerequisites

- Python 3.8+
- Streamlit
- LangChain
- Ollama
- Google Search API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bassemalyyy/LangChain-Google-LLM-Search-Agent.git
```

2. Install required packages:
```bash
pip install streamlit langchain ollama toml
```

3. Set up your configuration:
   - Create a `.streamlit/config.toml` file with your theme preferences
   - Configure your Google Search API credentials

## Configuration

Create a `config.toml` file in the `.streamlit` directory with the following structure:

```toml
[theme]
primaryColor = "#YOUR_PRIMARY_COLOR"
backgroundColor = "#YOUR_BACKGROUND_COLOR"
secondaryBackgroundColor = "#YOUR_SECONDARY_BACKGROUND_COLOR"
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Enter your search query in the text input field
3. Click "Submit Query" to get AI-enhanced search results

## Environment Variables

The following environment variables need to be set:

- `GOOGLE_API_KEY`: Your Google Search API key
- `GOOGLE_CSE_ID`: Your Google Custom Search Engine ID

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://python.langchain.com/)
- Uses [Ollama](https://ollama.ai/) for LLM capabilities
