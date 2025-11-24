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
    logprobs=True,
    top_logprobs=3
)

texto_resposta = resposta.choices[0].message.content
print(texto_resposta)

with open("resposta.json", "w") as f:
    f.write(resposta.choices[0].to_json())