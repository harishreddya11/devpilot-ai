from app.llm.openai_provider import OpenAIProvider


class ProviderFactory:

    @staticmethod
    def get_provider():
        return OpenAIProvider()