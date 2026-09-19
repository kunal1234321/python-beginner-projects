from openai import OpenAI

client = OpenAI()

question = input("Ask AI: ")

response = client.responses.create(
    model="gpt-5-mini",
    input=question
)

print("\nAI:", response.output_text)