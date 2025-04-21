from typing import List
import groq
from app.core.config import settings
from app.schemas.ticket import TicketWithMessages
from app.schemas.message import MessageInDB

class AIService:
    def __init__(self):
        self.client = groq.Client(api_key=settings.GROQ_API_KEY)

    async def generate_response(self, ticket: TicketWithMessages) -> str:
        # Format message history
        message_history = "\n".join(
            f"{'AI' if msg.is_ai else 'Customer'}: {msg.content}"
            for msg in ticket.messages[:-1]
        )
        
        # Latest message is the last one in the list
        latest_message = ticket.messages[-1].content
        
        # Create prompt
        prompt = f"""
        You are a helpful customer support assistant.
        The customer has the following issue: {ticket.description}

        Previous messages:
        {message_history}

        Customer's latest message: {latest_message}

        Provide a helpful response that addresses their concern
        """
        
        # Get response from Groq
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="mixtral-8x7b-32768",
            temperature=0.7,
            max_tokens=1024,
            stream=True
        )
        
        return chat_completion