from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model = "gpt-4.1",
    input="Write a one-sentence story about two dogs and a plushy squid toy.",
)

print(response.output_text)
