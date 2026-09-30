from collections import defaultdict

class MemoryService:
    """
    Simple in-memory storage. Redis ki zaroorat nahi.
    Server restart hone pe history delete ho jayegi — 
    lekin basic chatbot ke liye ye kaafi hai.
    """
    def __init__(self):
        self._store = defaultdict(list)
        self.max_history = 6  # last 6 messages yaad rakhega

    async def get_history(self, user_id: str) -> list:
        return self._store.get(user_id, [])

    async def add_message(self, user_id: str, role: str, content: str):
        history = self._store[user_id]
        history.append({"role": role, "content": content})
        self._store[user_id] = history[-self.max_history:]

    async def clear(self, user_id: str):
        self._store.pop(user_id, None)

memory_service = MemoryService()