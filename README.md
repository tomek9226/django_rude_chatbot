Django Rude Chatbot API

A simple sarcastic chatbot powered by Django and Cohere’s Large Language Model. This project exposes a single API endpoint that accepts a user message and returns a rude, humorous, and overly honest reply.

✅ Features
Sarcastic Responses – Generates intentionally rude and satirical replies powered by Cohere.
Cohere Integration – Uses the Cohere Chat API for conversational logic.
API Key Security – Loads secrets from a .env file using python-dotenv.
Simple Django Endpoint – Clean and lightweight JSON API for chat requests.

📌 Project Structure
django_rude_chatbot/        # Repository root
├── venv/                   # Python virtual environment
├── django_rude_chatbot/    # Django project (settings, URLs, config)
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── rude_bot/               # Main app (views, API logic)
│   ├── migrations/
│   ├── __init__.py
│   ├── urls.py
│   └── views.py            # Contains the rude_bot_api function
├── .env                    # Environment variables (Cohere API key)
├── .gitignore              # Keeps secrets & local files out of Git
└── manage.py               # Django management utility

🚀 Setup & Installation
Follow these steps to run the Rude Chatbot API locally.

1. Clone the Repository
git clone https://github.com/tomek9226/django_rude_chatbot
cd django_rude_chatbot

2. Create and Activate a Virtual Environment
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install django cohere python-dotenv
# OR, if using requirements.txt:
# pip install -r requirements.txt

4. Add Your Cohere API Key
Create a .env file in the project root and place your key inside:
COHERE_API_KEY=your_cohere_api_key_here

5. Run Migrations
python manage.py migrate

6. Start the Development Server
python manage.py runserver


Your API will now be running at:
👉 http://127.0.0.1:8000/

💬 API Usage

The chatbot is available via a POST request to:

POST http://127.0.0.1:8000/api/chat/

Example Request (cURL)
curl -X POST \
  http://127.0.0.1:8000/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "I feel like I had a really productive day today."}'

Example Response
{
  "reply": "Oh, you 'feel' productive? That's what people say right before they realize they achieved nothing of value. Go back to your nap."
}

🎯 Purpose

This API is meant for fun and experimentation, showcasing how to:
Integrate Cohere with Django
Build a minimal chat API
Work with environment-based secrets in Python
