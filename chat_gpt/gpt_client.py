import os
from dotenv import load_dotenv

from openai import AsyncOpenAI


load_dotenv()

GPT_TOKEN = os.getenv('OPENAI_API_KEY')

client = AsyncOpenAI(api_key=GPT_TOKEN)


async def ask_gpt(prompt):
    """
    Функція для запиту до GPT.
    Приймає prompt (текст запиту), повертає текст відповіді.
    """
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

async def ask_gpt_talk(messages):
    """
    Функція для запиту до GPT.
    Приймає prompt (рядок), повертає текст відповіді.
    """
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content