Here’s a clean **README.mb (Markdown-based)** for your smart AI assistant project, structured and ready for GitHub or school submission:

---

# 🧠 Smart AI Assistant

A powerful, feature-rich AI assistant built with Python.
This program combines conversational AI with built-in tools like a calculator, time/date system, and web automation.

---

## 📌 Features

* 💬 Intelligent AI chat with memory
* 🧠 Context-aware conversation (remembers recent messages)
* 🔄 Self-improving responses (reflection system)
* 🧮 Built-in calculator
* 🌐 Open websites from commands
* ⏰ Time and date retrieval
* 🎲 Random number generator
* 🧹 Memory reset command
* ⚡ Fast and lightweight CLI interface

---

## 🛠️ Technologies Used

* Python 3
* OpenAI API
* Colorama (for colored terminal output)
* Standard libraries:

  * `os`
  * `datetime`
  * `random`
  * `webbrowser`

---

## 🚀 Installation

### 1. Clone the repository

```bash id="clone123"
git clone https://github.com/your-username/smart-ai-assistant.git
cd smart-ai-assistant
```

### 2. Install dependencies

```bash id="install456"
pip install openai colorama
```

---

## 🔑 API Key Setup

Get your API key from OpenAI (https://platform.openai.com/api-keys).

**Important:** OpenAI API usage requires credits. New accounts get free credits that expire after a few months. For continued use, add a payment method at https://platform.openai.com/account/billing. Costs depend on model and usage (e.g., ~$0.002 per 1K tokens for GPT-4o-mini).

### Mac/Linux:

```bash id="env789"
export OPENAI_API_KEY="your_api_key_here"
```

### Windows (PowerShell):

```bash
$env:OPENAI_API_KEY = "your_api_key_here"
```

For persistent (survives restarts):

```bash
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your_api_key_here", "User")
```

For persistent (survives restarts):

```bash
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your_api_key_here", "User")
```

---

## ▶️ Run the Program

Activate the virtual environment first:

```bash
# On Windows
& .venv-1\Scripts\Activate.ps1
```

Then run:

```bash id="run111"
python AIassistant.py
```

---

## 🎮 How to Use

Once the program starts, type commands or chat naturally.

### 💬 Chat

```id="chat001"
What is artificial intelligence?
Explain black holes simply
```

### 🧮 Calculator

```id="calc001"
calc 5 * 10
```

### 🌐 Open Website

```id="web001"
open https://google.com
```

### ⏰ Time & Date

```id="time001"
time
date
```

### 🎲 Random Number

```id="rand001"
random 1 100
```

### 🧹 Clear Memory

```id="clear001"
clear
```

### 🚪 Exit

```id="exit001"
exit
```

---

## 🧠 How It Works

### 1. AI Engine

Uses the OpenAI API to generate responses.

### 2. Memory System

* Stores recent conversation history
* Automatically trims old messages
* Keeps responses relevant and fast

### 3. Tool System

Detects commands and executes:

* Calculator
* Browser
* Time/date
* Random generator

### 4. Reflection Layer

* AI improves its own responses
* Makes answers clearer and more useful

---

## 🧱 Project Structure

```id="structure001"
smart-ai-assistant/
│
├── main.py        # Main application code
└── README.md      # Documentation
```

---

## ⚠️ Notes

* Requires internet connection
* API usage may incur costs
* Avoid entering sensitive data

---

## 🚀 Future Improvements

* 🖥️ GUI version (Tkinter / CustomTkinter)
* 🎤 Voice assistant (speech-to-text)
* 🌐 Internet search integration
* 🧠 Local/offline AI model
* 📊 Data analysis tools
* 🎭 Personality modes

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by Yuriy Shevtsiv
