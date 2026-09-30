from pydantic import BaseModel
from typing import Optional, List, Any

class WhatsAppMessage(BaseModel):
    from_number: str
    message_id: str
    text: Optional[str] = None
    timestamp: str
    type: str

class WebhookPayload(BaseModel):
    object: str
    entry: List[Any]