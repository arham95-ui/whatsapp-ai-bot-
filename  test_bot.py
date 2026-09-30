import asyncio
from app.services.ai_service import ai_service

async def main():
    test_messages = [
        "Hello",
        "Aap kya services dete ho?",
        "IoT project banwana hai, kitna kharcha aayega?",
        "Kya aap Faisalabad se bahar kaam karte ho?",
    ]
    
    user_id = "test_user_123"
    
    for msg in test_messages:
        print(f"\n{'='*60}")
        print(f"👤 User: {msg}")
        print(f"{'='*60}")
        
        reply = await ai_service.get_reply(user_id, msg)
        
        print(f"🤖 Nexi: {reply}")
        print()

if __name__ == "__main__":
    asyncio.run(main())