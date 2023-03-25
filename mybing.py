import openai
import json
import os
import copy

DEBUG=False
openai.api_key = os.getenv("OPENAI_API_KEY")

with open('prompt.md', 'r') as file:
    assistant_instructions = file.read()

base_mensages=[
      {"role": "system", "content": assistant_instructions},
   ]

messages = copy.deepcopy(base_mensages)

def processRequest(msg):
    messages.append(msg)
    answer =  openai.ChatCompletion.create(
      model="gpt-4", 
      messages=messages
    )

    if DEBUG:
       print(f"================================================================================")
       print(f"Request chars: {len(json.dumps(messages))} and total usage is {answer.usage.total_tokens} token")
       print(f"{json.dumps(answer)}")
       print(f"================================================================================")
    return answer


print("Welcome!\nBing: How can I help you?")

import readline
line = input('User: ')
while line:
    content = processRequest({ "role": "user", "content": line}).choices[0].message.content
    print(f"Bing: {content} \n================================================================================")
    line = input('User: ')

