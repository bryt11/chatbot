# 🧠 OpenAI Chatbot Web App

A simple web-based chatbot application built with [Flask](https://flask.palletsprojects.com/) and powered by [OpenAI's GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5).

This project demonstrates how to integrate natural language conversation into a web application with session-based memory and a clean, interactive interface.

---

## 🚀 Features

* Live chat interface with OpenAI's GPT-3.5-turbo model
* Session-based memory (preserves multi-turn conversations)
* Clean web interface built with Jinja2 templates
* Reset conversation history with one click

---

## 🛠️ Technologies Used

* Python 3.7+
* Flask
* OpenAI Python SDK
* HTML (Jinja2 templating)

---

## 📆 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/openai-chatbot-flask.git
cd openai-chatbot-flask
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Create a `requirements.txt` manually if it’s missing:

```text
flask
openai
```

---

## 🔐 Set Your OpenAI API Key

Set your API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

On Windows (CMD):

```cmd
set OPENAI_API_KEY=your-api-key-here
```

---

## 🧪 Run the App

```bash
python app.py
```

Open your browser and go to `http://localhost:8000`

---

## 🧠 How It Works

* User messages are stored in `session["chat_context"]`
* The full context is sent to OpenAI on each turn
* Responses are parsed and rendered dynamically in a chat interface
* You can clear/reset the conversation using a dedicated `/clear` route

---

## 🗅 Screenshot

> Add a screenshot of the interface in the `static/` folder and embed it below:

```markdown
![Chat UI](static/screenshot.png)
```

---

## 📁 Project Structure

```
.
├── app.py                # Main Flask application
├── templates/
│   └── chat.html         # Web UI (Jinja2)
├── static/               # Static files (CSS, images, etc.)
├── README.md
└── requirements.txt
```

---

## ✅ To-Do / Extensions

* [ ] Add authentication
* [ ] Add streaming responses
* [ ] Use a database for persistent history
* [ ] Switch to OpenAI Assistants API (for tool use and memory)

---

## 📝 License

This project is licensed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgements

* [OpenAI API](https://platform.openai.com/)
* [Flask](https://flask.palletsprojects.com/)
* [ChatGPT](https://chat.openai.com/)
