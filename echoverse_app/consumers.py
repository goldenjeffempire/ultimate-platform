import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatSession, ChatMessage
from .utils import get_ai_response

class ChatBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        session = ChatSession.objects.get(id=self.session_id)

        # Save User Message
        ChatMessage.objects.create(session=session, sender="User", message=message)

        # Get AI Response
        ai_response = get_ai_response(message)

        # Save Bot Response
        ChatMessage.objects.create(session=session, sender="Bot", message=ai_response)

        # Send Response to Frontend
        await self.send(text_data=json.dumps({"message": ai_response, "sender": "Bot"}))
