from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
cliente = OpenAI()

resposta = cliente.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente útil"},
        {"role": "user", "content": "Me conte uma piada"}
    ]
)

texto_resposta = resposta.choices[0].message.content
print(texto_resposta)