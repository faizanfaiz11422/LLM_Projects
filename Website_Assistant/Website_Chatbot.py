from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv(dotenv_path='PATH_TO.env')
api_key = os.getenv('API_KEY') or 'gsk_4CH6...............ls'

# Initialize the Groq Client
client = Groq(api_key=api_key)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

system_prompt = "You are a smart assistant that helps users find specific products listed on the site, including their prices, sizes, materials, or any other information available."

def user_prompt_for(website, user_query):
    return f"""You are looking at a website titled {website.title}.
Website content:
{website.text}

User Query: {user_query}
Please respond in context with the website, keeping product specifications as the priority.
"""

def get_response(url, query):
    website = Website(url)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website, query)}
    ]
    try:
        response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=messages)
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

class ChatbotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Website Assistant")
        self.setGeometry(100, 100, 720, 540)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Chat display
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # User input
        self.user_input = QTextEdit(self)
        layout.addWidget(self.user_input)

        # Send button
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.handle_input)
        layout.addWidget(self.send_button)

        central_widget.setLayout(layout)
        self.chat_display.append("Assistant: Hello! Welcome to the LTHRPK. How may I assist you?")

    def handle_input(self):
        user_query = self.user_input.toPlainText().strip()
        if not user_query:
            self.chat_display.append("Error: Please enter a query.")
            return

        self.chat_display.append(f"You: {user_query}")
        self.user_input.clear()

        response = get_response("https://lthrpk.com", user_query)
        self.chat_display.append(f"Assistant: {response}")

if __name__ == "__main__":
    app = QApplication([])
    chatbot = ChatbotUI()
    chatbot.show()
    app.exec_()