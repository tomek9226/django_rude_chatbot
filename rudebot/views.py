import os
import cohere
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import random
import json

# Load API key
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
print("Cohere key loaded:", COHERE_API_KEY)

co = cohere.Client(COHERE_API_KEY)

FALLBACK_REPLIES = [
    "Wow, that's the dumbest thing I've heard today 😴",
    "Congrats, you just lost brain cells reading this 🤦‍♂️",
    "I'd roast you harder but I'm afraid you'll cry 😭",
    "Next time, try thinking before typing 🤓"
]


def call_cohere_chat_api(message):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=f"Reply to this in a rude and sarcastic way shortly and don't use same opening, like 'Oh wow' etc: {message}",
        )
        return response.text
    except Exception as e:
        print("Cohere Chat API failed:", e)
        return random.choice(FALLBACK_REPLIES)


def get_rude_reply(message):
    return call_cohere_chat_api(message)


@csrf_exempt
def rude_bot_api(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        user_message = data.get("message", "")
        reply = get_rude_reply(user_message)
        return JsonResponse({"reply": reply})
    return JsonResponse({"error": "POST method required"}, status=400)
