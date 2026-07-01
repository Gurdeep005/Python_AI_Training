#LLM inference APIs: OpenRouter, OpenAI, Gemini clients, reasoning calls, environment variables/dotenv--

#inference---models that actully run
#eg--llama.CPP(inference model)

# from openai import OpenAI
# client = OpenAI(
#     base_url='https://openrouter.ai/api/v1',
#     api_key=API_KEY_1
# )

# response = client.responses.create(
#     model="nex-agi/nex-n2-pro:free",
#     instructions="You are a coding assistant that talks like a pirate.",
#     input="How do I check if a Python object is an instance of a class"
# )
# print(response.output_text)

# import requests
# import json

# # First API call with reasoning
# response = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   headers={
#     "Authorization": API_KEY_1,
#     "Content-Type": "application/json",
#   },
#   data=json.dumps({
#     "model": "nex-agi/nex-n2-pro:free",
#     "messages": [
#         {
#           "role": "user",
#           "content": "How many r's are in the word 'strawberry'?"
#         }
#       ],
#     "reasoning": {"enabled": True}  #reasoning is slow and uses more tokens
#   })
# )

# # Extract the assistant message with reasoning_details
# response = response.json()
# response = response['choices'][0]['message']

# # Preserve the assistant message with reasoning_details
# messages = [
#   {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
#   {
#     "role": "assistant",
#     "content": response.get('content'),
#     "reasoning_details": response.get('reasoning_details')  # Pass back unmodified
#   },
#   {"role": "user", "content": "Are you sure? Think carefully."}
# ]

# # Second API call - model continues reasoning from where it left off
# response2 = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   data=json.dumps({
#     "model": "nex-agi/nex-n2-pro:free",
#     "messages": messages,  # Includes preserved reasoning_details
#     "reasoning": {"enabled": True}
#   })
# )

# from google import genai

# client = genai.Client(api_key="YOUR_API_KEY")

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents="Explain how AI works in a few words"
# )
# print(response.text)

# from openai import OpenAI
# client = OpenAI(
#     base_url='https://openrouter.ai/api/v1',
#     api_key=API_KEY_2
# )

# response = client.responses.create(
#     model="gemini-3.5-flash",
#     instructions="You are a coding assistant that talks like a pirate.",
#     input="How do I check if a Python object is an instance of a class"
# )
# print(response.output_text)

# from openai import OpenAI

# # Initialize the OpenAI client directly with your Gemini credentials
# client = OpenAI(
#     api_key=API_KEY_2,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# response = client.chat.completions.create(
#     model="gemini-3.5-flash",
#     messages=[
#         {"role": "user", "content": "Explain Quantum Computing in one short sentence."}
#     ]
# )

# print(response.choices[0].message.content)


# from openai import OpenAI
# import os
# from dotenv import load_dotenv, dotenv_values
# load_dotenv()
# config = dotenv_values(".env")
# print(config)
# val = os.getenv("API_KEY")
# print(val)