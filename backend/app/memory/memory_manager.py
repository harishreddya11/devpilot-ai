from app.memory.chat_memory import ChatMessage


class MemoryManager:

    def __init__(self):
        self.messages: list[ChatMessage] = []

    def add_user(self, message: str):
        self.messages.append(
            ChatMessage(
                role="user",
                content=message,
            )
        )

    def add_assistant(self, message: str):
        self.messages.append(
            ChatMessage(
                role="assistant",
                content=message,
            )
        )

    def get_messages(self):
        return [
            {
                "role": m.role,
                "content": m.content,
            }
            for m in self.messages
        ]

    def clear(self):
        self.messages.clear()