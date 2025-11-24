from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
cliente = OpenAI()

resposta = cliente.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente útil"},
        {"role": "user", "content": "Me conte uma piada"}
    ],
    # max_tokens=20,
    # stop=["?", "matemática", "matemático"],
    n=3
)

for resposta in resposta.choices:
    print(resposta.message.content)
    print("=" * 50)