import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
client = Groq(api_key=my_api_key)
model="allam-2-7b"
role="user"

# 3 Prompts
prompt1 = "Hii"
prompt2 = "Explain time travel in detail"
prompt3 = "Write a 1000 word essay on Machine learning."

prompts=[prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {"role": role, "content": prompt}

    response = client.chat.completions.create(model=model, messages=[message])
    usage = response.usage
    print (f"Prompt: {prompt} --> Your Tokens: {usage.prompt_tokens}, Completion Tokens: {usage.completion_tokens}, Total Tokens: {usage.total_tokens}")