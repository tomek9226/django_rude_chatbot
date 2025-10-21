Django Rude Chatbot API

A simple, sarcastic chatbot powered by Django and the Cohere Large Language Model. This project exposes a single API endpoint that processes a user message and returns a rude, humorous reply.

Features

Sarcastic Replies: Uses Cohere to generate intentionally rude and satirical responses.

Cohere Integration: Implements the Cohere Chat API for core conversational logic.

API Key Security: Utilizes environment variables (.env file) to securely manage the Cohere API Key.

Simple Django API: Provides a single, clean JSON endpoint for chat requests.

Project Structure

django_rude_chatbot/  # Repository Root Folder
├── venv/             # Python virtual environment
├── django_rude_chatbot/ # Django project folder (settings, URLs)
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── rude_bot/         # Main Django application (Views, logic)
│   ├── migrations/
│   ├── init.py
│   ├── urls.py
│   └── views.py      # Contains the rude_bot_api function
├── .env              # Environment file storing the API key
├── .gitignore        # Ensures secrets and local files are not committed
└── manage.py         # Django management utility


Setup

Follow these steps to set up and run the Rude Chatbot API locally.

1. Clone the Repository

git clone [https://github.com/tomek9226/django_rude_chatbot](https://github.com/tomek9226/django_rude_chatbot)
cd django_rude_chatbot


2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate


3. Install Dependencies

You will need to install the packages used in the project, primarily Django, cohere, and python-dotenv.

pip install django cohere python-dotenv
# Alternatively, use a requirements.txt if you generated one:
# pip install -r requirements.txt


4. Configure API Key

Create a file named .env in the root directory of your project (django_rude_chatbot/) and add your Cohere API key:

# .env file content
COHERE_API_KEY=your_cohere_api_key_here


5. Run Migrations

python manage.py migrate


6. Start the Development Server

python manage.py runserver


The API will be running at http://127.0.0.1:8000/.

API Usage

The chat logic is exposed via a POST request to the chat endpoint.

Endpoint

POST http://127.0.0.1:8000/api/chat/

Example Request (using curl)

curl -X POST \
  [http://127.0.0.1:8000/api/chat/](http://127.0.0.1:8000/api/chat/) \
  -H 'Content-Type: application/json' \
  -d '{"message": "I feel like I had a really productive day today."}'


ply": "Oh, you 'feel' productive? That's what people say right before they realize they achieved nothing of value. Go back to your nap."
}
