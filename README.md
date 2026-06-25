# Basic-Groq-Chatbot
Zero-setup AI terminal chatbot powered by Groq + Llama 3.1 with automatic environment and dependency management.

🤖 Groq Llama Terminal Chatbot

A fully automated terminal-based chatbot powered by the Groq API and Llama 3.1.
The application requires no manual setup — it automatically handles dependencies and environment configuration on first run.

🚀 Features
⚡ Fast responses using Groq API
🧠 Powered by Llama 3.1 (llama-3.1-8b-instant)
📦 Automatic dependency installation (no requirements.txt needed)
🔐 Auto .env creation and API key setup on first run
💬 Simple terminal chat interface
⛔ Exit anytime with exit or finish
🧠 How It Works

On first launch, the program automatically:

Checks required Python packages
Installs missing dependencies via pip
Checks for .env file
Prompts user for Groq API key if missing
Starts the chatbot

No setup or configuration required.

📁 Project Structure
project/
│── a.py
│── .env (auto-generated)
▶️ Run the chatbot
python a.py

That’s it — everything is handled automatically.

💬 Usage
You: Hello
Bot: Hi! How can I help you?

You: exit
# program closes

You can also type:

finish
exit
🔐 Security
API key is stored locally in .env
.env file is automatically created if missing
Recommended .gitignore:
.env
__pycache__/
🛠 Future Improvements
🧠 Conversation memory system
⚡ Streaming responses (real-time typing effect)
🔁 Retry system for API errors
🧩 Command system (/reset, /help)
🌐 Multi-model support (Groq + fallback APIs)
📜 License

MIT License

💡 Why this project?

This project is a zero-setup AI chatbot CLI tool built for:

learning LLM APIs
building automation scripts
practicing Python tooling
creating AI agents
