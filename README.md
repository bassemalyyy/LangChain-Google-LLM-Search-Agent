Search Agent with Ollama
========================

A modern web application built with Reflex that combines Google Search with local Ollama LLM to provide AI-powered search responses. This app creates an intelligent search agent that can query Google for recent information and generate comprehensive responses using the Llama 3.2 model.

Features
--------

-   🔍 **Google Search Integration** - Real-time web search using Serper API
-   🤖 **Local LLM Processing** - Powered by Ollama and Llama 3.2 model
-   🎨 **Modern UI** - Beautiful gradient design with responsive components
-   ⚡ **Real-time Updates** - Async processing with loading states
-   🛡️ **Error Handling** - Comprehensive error management and user feedback
-   📱 **Responsive Design** - Works seamlessly across all devices

Prerequisites
-------------

Before running this application, make sure you have the following installed:

-   Python 3.10 or higher
-   [Ollama](https://ollama.ai/) installed and running
-   A Serper API key (get one from [serper.dev](https://serper.dev/))

Installation
------------

1.  **Clone the repository**

    ```bash
    git clone https://github.com/bassemalyyy/LangChain-Search-Agent.git
    cd LangChain-Search-Agent
    ```

2.  **Create a virtual environment**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate # On Windows
    ```

3.  **Install dependencies**

    ```bash
    pip install reflex langchain langchain-community langchain-ollama
    ```

4.  **Install and setup Ollama**

    Download and install Ollama from [ollama.ai](https://ollama.ai/)

    Then pull the Llama 3.2 model:

    ```bash
    ollama pull llama3.2
    ```

    Start Ollama service:

    ```bash
    ollama serve
    ```

5.  **Configure API Key**

    Replace the Serper API key in the code with your own:

    ```bash
    serper_search = GoogleSerperAPIWrapper(
    serper_api_key="serper_api_key")
    ```

Running the Application
-----------------------

1.  **Initialize Reflex**

    ```bash
    reflex init
    ```

2.  **Run the development server**

    ```bash
    reflex run
    ```

3.  **Open your browser**

    Navigate to `http://localhost:3000` to access the application.

Project Structure
-----------------

```bash
langchain_reflex_agent/
├── assets/                     
├── langchain_reflex_agent/     # Application package
│   ├── __init__.py
│   └── langchain_reflex_agent.py # Main Reflex entrypoint
├── rxconfig.py                 # Reflex build configuration
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview & setup instructions
├── .gitignore                  # Ignored files
```

Configuration
-------------

### Ollama Model Configuration

You can change the Ollama model by modifying this line in `main.py`:

```bash
ollama_llm = OllamaLLM(model="llama3.2")  # Change to any model you have installed
```

Available models can be listed with:

```bash
ollama list
```

Usage
-----

1.  Enter your search query in the input field
2.  Click "Submit Query" or press Enter
3.  The application will:
    -   Search Google for relevant information
    -   Process the results using the local Llama 3.2 model
    -   Generate a comprehensive AI-powered response

Dependencies
------------

-   **reflex** - Web framework for Python
-   **langchain** - LLM application framework
-   **langchain-community** - Community integrations for LangChain
-   **langchain-ollama** - Ollama integration for LangChain

Acknowledgments
---------------

-   [Reflex](https://reflex.dev/) for the amazing Python web framework
-   [Ollama](https://ollama.ai/) for local LLM capabilities
-   [LangChain](https://langchain.com/) for LLM orchestration
-   [Serper](https://serper.dev/) for Google Search API

Support
-------

If you encounter any issues or have questions, please:

1.  Check the troubleshooting section above
2.  Search existing [GitHub Issues](https://github.com/yourusername/search-agent-ollama/issues)
3.  Create a new issue with detailed information about your problem

* * * * *

⭐ If you found this project helpful, please give it a star!
