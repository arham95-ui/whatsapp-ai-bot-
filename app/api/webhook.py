from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import PlainTextResponse
from app.config import settings
from app.services.whatsapp import whatsapp_service
from app.services.ai_service import ai_service

router = APIRouter()

@router.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
):
    """Meta calls this to verify your webhook."""
    if hub_mode == "subscribe" and hub_token == settings.VERIFY_TOKEN:
        return PlainTextResponse(hub_challenge)
    raise HTTPException(status_code=403, detail="Verification failed")

@router.post("/webhook")
async def receive_message(request: Request):
    """Receives incoming WhatsApp messages."""
    body = await request.json()

    try:
        entry = body["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        # Ignore status updates (delivered, read)
        if "messages" not in value:
            return {"status": "ok"}

        message = value["messages"][0]
        from_number = message["from"]
        message_id = message["id"]

        # Only handle text messages
        if message["type"] != "text":
            await whatsapp_service.send_text(
                from_number, "Filhal sirf text messages support hain."
            )
            return {"status": "ok"}

        user_text = message["text"]["body"]

        # Mark as read
        await whatsapp_service.mark_as_read(message_id)

        # Get AI reply
        ai_reply = await ai_service.get_reply(from_number, user_text)

        # Send back to WhatsApp
        await whatsapp_service.send_text(from_number, ai_reply)

    except (KeyError, IndexError) as e:
        print(f"Parse error: {e}")

    return {"status": "ok"}