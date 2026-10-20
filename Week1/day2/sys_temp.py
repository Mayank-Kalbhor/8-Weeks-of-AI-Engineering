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
prompt="suggest me a name for my food company"
message_system={
    "role": "system",
    "content": "you are a brand manager, who suggests a name for my food brand, it should be one word name."
}
message = {"role": role, "content": prompt}
response = client.chat.completions.create(model=model, messages=[message_system,message], temperature=3)
print(response.choices[0].message.content)
