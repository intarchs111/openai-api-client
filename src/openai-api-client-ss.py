# import the necessary modules
import os

import openai
from dotenv import load_dotenv, find_dotenv

# load .env file
load_dotenv(find_dotenv())

# get api key from environment
api_key = os.getenv("OPENAI_API_KEY")             
        
# initialize OpenAI API client with api key
client = openai.OpenAI(api_key=api_key)

# create response from OpenAI Responses API with request parameters model, input, max_output_tokens and store
# POST https://api.openai.com/v1/responses
response = client.responses.create(
    model="gpt-5-nano",
    input="What is the capital of France?",
    store=False,
    max_output_tokens=300
)

# print model response
print(response.output_text)


