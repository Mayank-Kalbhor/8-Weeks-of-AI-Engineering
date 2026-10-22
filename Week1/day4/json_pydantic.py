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

import pydantic 
from pydantic import BaseModel
class UserInfo(BaseModel):
    name: str
    product: str
    issue: str
    location: str
    contact_number: str

import json

schema = json.dumps(UserInfo.model_json_schema(), indent=2)
response_format = {"type": "json_object"}
system_prompt = f"Extract the personal information from the ticket strictly based on this schema, and give it in a json format: {schema}"
message_system = {"role": "system", "content": system_prompt}

text ="Hello my name is Mayank . I have purchased a Samsung S25 from your store, that has stopped working. I live in Delhi, India.My contact number is 1234567890"
prompt=f"""Please extract the personal information from the text. The text is: {text}"""

message = {"role": role, "content": prompt}
messages=[message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format={"type": "json_object"})
# print(response.choices[0].message.content)

raw_json = response.choices[0].message.content
data_file= json.loads(raw_json)
ticket_info = UserInfo(**data_file)

print(ticket_info.name)
print(ticket_info.product)
print(ticket_info.issue)
print(ticket_info.location)
print(ticket_info.contact_number)