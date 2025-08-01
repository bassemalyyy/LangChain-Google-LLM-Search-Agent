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

-   Python 3.8 or higher
-   [Ollama](https://ollama.ai/) installed and running
-   A Serper API key (get one from [serper.dev](https://serper.dev/))

Installation
------------

1.  **Clone the repository**

    ```
    git clone https://github.com/yourusername/search-agent-ollama.git
    cd search-agent-ollama

    ```

2.  **Create a virtual environment**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    ```

3.  **Install dependencies**

    ```
    pip install reflex langchain langchain-community langchain-ollama

    ```

4.  **Install and setup Ollama**

    Download and install Ollama from [ollama.ai](https://ollama.ai/)

    Then pull the Llama 3.2 model:

    ```
    ollama pull llama3.2

    ```

    Start Ollama service:

    ```
    ollama serve

    ```

5.  **Configure API Key**

    Replace the Serper API key in the code with your own:

    ```
    serper_search = GoogleSerperAPIWrapper(
        serper_api_key="YOUR_SERPER_API_KEY_HERE"
    )

    ```

Running the Application
-----------------------

1.  **Initialize Reflex**

    ```
    reflex init

    ```

2.  **Run the development server**

    ```
    reflex run

    ```

3.  **Open your browser**

    Navigate to `http://localhost:3000` to access the application.

Project Structure
-----------------

```
search-agent-ollama/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── rxconfig.py            # Reflex configuration
├── .web/                  # Generated web assets (auto-created)
└── README.md              # This file

```

Configuration
-------------

### Environment Variables (Recommended)

For better security, consider using environment variables for your API key:

```
import os
from dotenv import load_dotenv

load_dotenv()

serper_search = GoogleSerperAPIWrapper(
    serper_api_key=os.getenv("SERPER_API_KEY")
)

```

Create a `.env` file:

```
SERPER_API_KEY=your_serper_api_key_here

```

### Ollama Model Configuration

You can change the Ollama model by modifying this line in `main.py`:

```
ollama_llm = OllamaLLM(model="llama3.2")  # Change to any model you have installed

```

Available models can be listed with:

```
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

Troubleshooting
---------------

### Common Issues

**Ollama Connection Error**

-   Ensure Ollama is running: `ollama serve`
-   Check if the model is installed: `ollama list`
-   Verify the model name matches in the code

**Serper API Error**

-   Check your API key is valid and has remaining credits
-   Ensure you're connected to the internet

**Reflex Build Issues**

-   Try deleting the `.web` directory and running `reflex init` again
-   Ensure all dependencies are installed: `pip install -r requirements.txt`

### Debug Mode

Run the application in debug mode for more detailed error messages:

```
reflex run --debug

```

Dependencies
------------

-   **reflex** - Web framework for Python
-   **langchain** - LLM application framework
-   **langchain-community** - Community integrations for LangChain
-   **langchain-ollama** - Ollama integration for LangChain

Contributing
------------

1.  Fork the repository
2.  Create a feature branch (`git checkout -b feature/amazing-feature`)
3.  Commit your changes (`git commit -m 'Add some amazing feature'`)
4.  Push to the branch (`git push origin feature/amazing-feature`)
5.  Open a Pull Request

License
-------

This project is licensed under the MIT License - see the [LICENSE](https://claude.ai/chat/LICENSE) file for details.

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
