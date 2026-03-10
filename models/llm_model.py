from groq import Groq
from config.settings import GROQ_API_KEY, LLM_MODEL


class LLMModel:

    def __init__(self):

        if not GROQ_API_KEY:
            raise ValueError("GROQ API KEY not found. Check .env file.")

        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = LLM_MODEL

    def generate_answer(self, question: str, memories: str):

        system_prompt = """
You are an intelligent personal AI assistant.

You have access to memories about the user.

Your job is to:
1. Use the memories if they are relevant
2. Personalize the response
3. Ignore memories that are unrelated
4. Provide clear and helpful answers
"""

        memory_section = f"""
User Memories:
{memories}
"""

        user_section = f"""
User Question:
{question}
"""

        reasoning_instruction = """
Reason carefully before answering.

Steps:
1. Determine if any memory is relevant
2. Use relevant memories to personalize the answer
3. If no memory is useful, answer normally
"""

        final_prompt = f"""
{memory_section}

{user_section}

{reasoning_instruction}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": final_prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content