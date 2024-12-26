import os
from typing import List, Dict
from groq import Groq
from groq.types.chat.chat_completion import ChatCompletion


class GroqInference:
    def __init__(self, model: str = "llama-3.3-70b-versatile") -> None:
        os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
        self.groq_client = Groq()
        self.model = model

    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        """
        Generate a response using Groq's LLM.

        Args:
            messages: List of message dictionaries with 'role' and 'content' keys

        Returns:
            str: The generated response from the model
        """
        completion: ChatCompletion = self.groq_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.1,
            max_tokens=512,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content