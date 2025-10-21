import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .views import get_rude_reply


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        rude_reply = get_rude_reply(message)

        await self.send(text_data=json.dumps({
            'message': rude_reply,
            'user': 'GrokBot'
        }))
