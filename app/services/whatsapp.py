import httpx
from app.config import settings

class WhatsAppService:
    def __init__(self):
        self.base_url = f"{settings.WHATSAPP_API_URL}/{settings.PHONE_NUMBER_ID}"
        self.headers = {
            "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
            "Content-Type": "application/json",
        }

    async def send_text(self, to: str, message: str):
        """Send text message to a WhatsApp number."""
        url = f"{self.base_url}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message},
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=self.headers)
            return response.json()

    async def mark_as_read(self, message_id: str):
        """Mark incoming message as read."""
        url = f"{self.base_url}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id,
        }
        async with httpx.AsyncClient() as client:
            await client.post(url, json=payload, headers=self.headers)

whatsapp_service = WhatsAppService()