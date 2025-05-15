
# 🧠 Website Chatbot/Assistant 

A Python-based desktop application that functions as a Website Assistant to extract information from website. It extracts relevant content using web scraping and leverages **LLM models** to answer user queries.

---

## 🌐 Purpose

The app is designed to assist users in navigating and extracting information from website. While `https://lthrpk.com` is used as a **sample site**, the codebase is built to support **any website** with minimal changes.

---

## ✨ Features

* ⚡ Intelligent product assistant powered by free-to-use LLM models using GROQ
* 🧹 Cleans irrelevant HTML elements like scripts and styles
* 🧾 Extracts and parses readable website text for query context
* 💬 Chat interface with multi-turn support
* 📦 Built with modularity for different website use-cases

---

## 🛠️ Requirements

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**

```txt
PyQt5
requests
beautifulsoup4
python-dotenv
groq
```

---

## 📦 Installation & Setup

1. **Clone the repository**

```bash
https://github.com/faizanfaiz11422/LLM_Projects.git
cd Website_Assistant
```

2. **Create a virtual environment** (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your `.env` file**
   Create a `.env` file in the project root and add your API key:

```env
API_KEY=gsk_your_groq_api_key_here
```

5. **Run the application**

```bash
python app.py
```

---

## 💡 How It Works

1. **Scrapes the target website** using `requests` and `BeautifulSoup`.
2. **Cleans the content** by removing scripts, styles, and inputs.
3. **Constructs a prompt** based on the system role and page content.
4. **Sends the prompt** to Groq's LLaMA 3.3 model for a natural language response.
5. **Displays results** in a simple PyQt5 GUI where users can ask product-related questions.

---

## 🧪 Sample Use (Using [https://lthrpk.com](https://lthrpk.com))

**Prompt:**

> What types of leather jackets are available?

**Assistant Reply:**

> The site lists various leather jackets including classic, biker, and bomber styles. They are available in sizes S to XXL and materials such as sheepskin and cowhide leather.

---

## 🧩 Customizing for Other Websites

* Change the URL passed to `get_response(url, query)` in `handle_input()` method.
* Optional: Update the `system_prompt` variable to customize the assistant's role.

---

## 🔐 Security Note

Never commit your `.env` file with the API key to GitHub. Use `.gitignore` to avoid accidentally exposing it.

---

## 📄 License

Licensed under the MIT License. See `LICENSE` file for details.

---

## 🤝 Contributing

Pull requests are welcome! If you have suggestions for improving the generic chatbot, feel free to open an issue or fork the project.

---

## 📬 Contact

* Developer: \[faizanfaiz11422]
* GitHub: [@faizanfaiz11422](https://github.com/faizanfaiz11422)
* Email: [faizanfaiz11422@gmail.com](mailto:faizanfaiz11422@gmail.com)
