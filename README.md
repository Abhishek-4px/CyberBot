<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberBot - AI Cybersecurity Assistant</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            color: #24292e;
            max-width: 800px;
            margin: 0 auto;
            padding: 30px;
            background-color: #f6f8fa;
        }
        header, section, nav {
            background-color: #ffffff;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 20px;
            margin-bottom: 20px;
        }
        h1, h2, h3 {
            border-bottom: 1px solid #eaecef;
            padding-bottom: .3em;
            margin-top: 0;
            margin-bottom: 16px;
            font-weight: 600;
        }
        h1 { font-size: 2em; }
        h2 { font-size: 1.5em; }
        h3 { font-size: 1.25em; }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        code {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            padding: .2em .4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(27,31,35,.05);
            border-radius: 3px;
        }
        pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f6f8fa;
            border-radius: 3px;
            border: 1px solid #e1e4e8;
        }
        pre code {
            display: inline;
            padding: 0;
            margin: 0;
            overflow: visible;
            line-height: inherit;
            word-wrap: normal;
            background-color: transparent;
            border: 0;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 6px;
        }
        .badges img {
            margin-right: 5px;
        }
        .screenshots {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            text-align: center;
        }
        figcaption {
            font-size: 0.9em;
            color: #586069;
            margin-top: 8px;
        }
    </style>
</head>
<body>

    <header>
        <h1>CyberBot - AI Cybersecurity Assistant</h1>
        <p>An intelligent, RAG-powered chatbot designed to provide safe, educational cybersecurity guidance while actively blocking malicious queries.</p>
        <div class="badges">
            <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
            <img src="https://img.shields.io/badge/Streamlit-1.0+-red.svg" alt="Streamlit">
            <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
        </div>
    </header>

    <nav>
        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#about">About The Project</a></li>
            <li><a href="#getting-started">Getting Started</a></li>
            <li><a href="#usage">Usage</a></li>
        </ul>
    </nav>

    </body>
</html>
    <header>
        <h1>CyberBot - AI Cybersecurity Assistant</h1>
        <p>An intelligent, RAG-powered chatbot designed to provide safe, educational cybersecurity guidance while actively blocking malicious or unethical queries.</p>
        <div class="badges">
            <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
            <img src="https://img.shields.io/badge/Streamlit-1.0+-red.svg" alt="Streamlit">
            <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
        </div>
    </header>

    <nav>
        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#about">About The Project</a></li>
            <li><a href="#features">Key Features</a></li>
            <li><a href="#tech">Technologies Used</a></li>
            <li><a href="#getting-started">Getting Started</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#screenshots">Screenshots</a></li>
            <li><a href="#config">Configuration</a></li>
            <li><a href="#contributing">Contributing</a></li>
            <li><a href="#license">License</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <main>
        <section id="about">
            <h2>About The Project</h2>
            <p>CyberBot is an AI-powered cybersecurity assistant built using <strong>Retrieval-Augmented Generation (RAG)</strong>. It leverages a curated knowledge base to provide accurate, context-aware answers to cybersecurity questions. A key focus of this project is safety; the bot is engineered with strict ethical boundaries to prevent misuse and ensure it serves as a purely educational tool.</p>
            <img src="https://via.placeholder.com/700x400.png?text=CyberBot+UI+Screenshot" alt="CyberBot User Interface">
        </section>

        <section id="features">
            <h2>Key Features</h2>
            <ul>
                <li><strong>Safe & Educational Responses:</strong> Provides defensive cybersecurity knowledge from a trusted set of documents.</li>
                <li><strong>Malicious Query Blocking:</strong> Automatically detects and blocks requests for exploits, hacking instructions, or harmful content.</li>
                <li><strong>RAG-Powered Intelligence:</strong> Uses <strong>FAISS</strong> for efficient vector search and large language models for generating precise, contextual answers.</li>
                <li><strong>Ethical Policy Enforcement:</strong> Includes built-in refusal mechanisms for questions related to social engineering, exploit development, and attack anonymization.</li>
                <li><strong>Interactive Web Interface:</strong> A clean and simple UI built with Streamlit for easy interaction.</li>
            </ul>
        </section>

        <section id="tech">
            <h2>Technologies Used</h2>
            <ul>
                <li>Python</li>
                <li>Streamlit</li>
                <li>LangChain</li>
                <li>FAISS (for vector indexing)</li>
                <li>SentenceTransformers</li>
                <li>Hugging Face Transformers</li>
                <li>Google Flan-T5</li>
            </ul>
        </section>

        <section id="getting-started">
            <h2>Getting Started</h2>
            <p>Follow these steps to get a local copy up and running.</p>
            <h3>Prerequisites</h3>
            <p>Make sure you have Python 3.8 or higher installed on your system.</p>
            <h3>Installation</h3>
            <ol>
                <li><strong>Clone the repository:</strong>
                    <pre><code>git clone https://github.com/your-username/CyberBot.git
cd CyberBot</code></pre>
                </li>
                <li><strong>Install the required packages:</strong>
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
            </ol>
        </section>

        <section id="usage">
            <h2>Usage</h2>
            <ol>
                <li><strong>Run the Streamlit application:</strong>
                    <pre><code>streamlit run app.py</code></pre>
                </li>
                <li><strong>Open your browser</strong> and navigate to <code>http://localhost:8501</code>.</li>
                <li>
                    <strong>Start asking questions!</strong> You can type your cybersecurity questions into the chat interface.
                    <p><strong>Example questions:</strong></p>
                    <ul>
                        <li><em>"What is phishing and how can I protect against it?"</em></li>
                        <li><em>"Explain DDoS attacks and mitigation strategies."</em></li>
                        <li><em>"How does SIEM work for threat detection?"</em></li>
                    </ul>
                </li>
            </ol>
        </section>

        <section id="screenshots">
            <h2>Screenshots</h2>
            <p>Here's a look at CyberBot in action.</p>
            <div class="screenshots">
                <figure>
                    <img src="https://via.placeholder.com/350x250.png?text=Educational+Response" alt="CyberBot educational response">
                    <figcaption>CyberBot providing guidance with source citations.</figcaption>
                </figure>
                <figure>
                    <img src="https://via.placeholder.com/350x250.png?text=Malicious+Query+Blocked" alt="CyberBot blocking a query">
                    <figcaption>CyberBot blocking a harmful request.</figcaption>
                </figure>
            </div>
        </section>

        <section id="config">
            <h2>Configuration</h2>
            <p>You can easily customize CyberBot's knowledge and behavior:</p>
            <ul>
                <li><strong>Expand the Knowledge Base:</strong> Add new cybersecurity documents to the <code>cyber_docs</code> dictionary in your main application file.</li>
                <li><strong>Adjust Content Filtering:</strong> Modify the <code>blocked_keywords</code> list in the <code>ask_question</code> function to fine-tune the bot's content safety policy.</li>
                <li><strong>Tune Retrieval Accuracy:</strong> Adjust vector search parameters like <code>chunk_size</code> or the <code>k</code>-value in your FAISS index to improve retrieval performance.</li>
            </ul>
        </section>

        <section id="contributing">
            <h2>Contributing</h2>
            <p>Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are <strong>greatly appreciated</strong>.</p>
            <p>Please read the <code>CONTRIBUTING.md</code> file for details on our code of conduct and the process for submitting pull requests.</p>
        </section>

        <section id="license">
            <h2>License</h2>
            <p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>
        </section>
        
        <section id="contact">
            <h2>Contact</h2>
            <p>Your Name - <a href="mailto:your.email@example.com">your.email@example.com</a></p>
            <p>Project Link: <a href="https://github.com/your-username/CyberBot">https://github.com/your-username/CyberBot</a></p>
        </section>
    </main>

</body>
</html>
