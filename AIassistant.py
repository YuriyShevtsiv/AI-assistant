import os
import datetime
import random
import webbrowser
import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

# =========================
# 🔹 CONFIG
# =========================
SYSTEM_PROMPT = """
You are an intelligent, precise, and efficient AI assistant.
- Give clear, useful, and direct answers.
- Think step-by-step internally but respond concisely.
- Use tools when needed.
- Avoid unnecessary fluff.
"""

MAX_HISTORY = 12  # prevents memory overload


# =========================
# 🔹 AI ENGINE
# =========================
class Brain:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            api_key = input("Enter your OpenAI API key: ")
        self.client = OpenAI(api_key=api_key)

    def think(self, messages):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI Error: {str(e)}"


# =========================
# 🔹 MEMORY
# =========================
class Memory:
    def __init__(self):
        self.history = [{"role": "system", "content": SYSTEM_PROMPT}]

    def add(self, role, content):
        self.history.append({"role": role, "content": content})
        self.trim()

    def trim(self):
        if len(self.history) > MAX_HISTORY:
            self.history = [self.history[0]] + self.history[-MAX_HISTORY:]

    def clear(self):
        self.history = self.history[:1]

    def get(self):
        return self.history


# =========================
# 🔹 TOOLS
# =========================
class Tools:
    @staticmethod
    def calc(expr):
        try:
            return str(eval(expr))
        except:
            return "Calculation error"

    @staticmethod
    def time():
        return datetime.datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def date():
        return datetime.datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def open(url):
        webbrowser.open(url)
        return f"Opened {url}"

    @staticmethod
    def random(a, b):
        return str(random.randint(a, b))


# =========================
# 🔹 SMART ASSISTANT
# =========================
class SmartAssistant:
    def __init__(self):
        self.brain = Brain()
        self.memory = Memory()

    def detect_intent(self, text):
        text = text.lower()

        if text.startswith("calc"):
            return "calc"
        if text.startswith("open"):
            return "open"
        if text == "time":
            return "time"
        if text == "date":
            return "date"
        if text.startswith("random"):
            return "random"
        if text == "clear":
            return "clear"
        if text == "exit":
            return "exit"

        return "chat"

    def use_tool(self, intent, text):
        parts = text.split()

        if intent == "calc":
            return Tools.calc(" ".join(parts[1:]))

        if intent == "open":
            return Tools.open(parts[1])

        if intent == "time":
            return Tools.time()

        if intent == "date":
            return Tools.date()

        if intent == "random":
            return Tools.random(int(parts[1]), int(parts[2]))

        if intent == "clear":
            self.memory.clear()
            return "Memory cleared."

        return None

    def reflect(self, response):
        """Improves answer quality (mini self-critique)"""
        critique_prompt = [
            {"role": "system", "content": "Improve this answer to be clearer and smarter."},
            {"role": "user", "content": response}
        ]
        return self.brain.think(critique_prompt)

    def chat(self, user_input):
        intent = self.detect_intent(user_input)

        if intent == "exit":
            return "exit"

        if intent != "chat":
            return self.use_tool(intent, user_input)

        self.memory.add("user", user_input)

        raw = self.brain.think(self.memory.get())
        improved = self.reflect(raw)

        self.memory.add("assistant", improved)
        return improved


# =========================
# 🔹 GUI
# =========================
class AIAssistantGUI:
    def __init__(self, root):
        self.bot = SmartAssistant()
        self.root = root
        self.root.title("Smart AI Assistant")
        self.root.geometry("600x400")

        # Output area
        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
        self.output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.output.insert(tk.END, "🧠 Smart AI Assistant\nType 'exit' to quit\n\n")

        # 1Input frame
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        self.input_entry = tk.Entry(input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.pack(pady=5)

    def send_message(self, event=None):
        user_input = self.input_entry.get().strip()
        if not user_input:
            return
        self.input_entry.delete(0, tk.END)

        self.output.insert(tk.END, f"You: {user_input}\n")

        result = self.bot.chat(user_input)

        if result == "exit":
            self.output.insert(tk.END, "Goodbye 👋\n")
            self.root.quit()
        else:
            self.output.insert(tk.END, f"AI: {result}\n\n")

        self.output.see(tk.END)

    def quit_app(self):
        self.root.quit()


def main():
    root = tk.Tk()
    app = AIAssistantGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()