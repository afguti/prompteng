#!/usr/bin/env python3
#import sys
import openai

#lines below are to add api key as an env variable
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

#I think I dont need this function for the chatbot
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_message(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def default():
	print("Empty!")

def execute():
    context = [{'role':'system', 'content':"""You are a friendly chatbot"""}]
    while True:
        user_input = input("You: ")
        context.append({'role':'user', 'content':f"{user_input}"})
        response = get_completion_from_message(context, temperature=0.3)
        context.append({'role':'assistant', 'content':f"{response}"})
        #print(str(context)) #For texting purposes
        print("Chatbot: ", response)

def main():
	execute()

if __name__ == "__main__":
	main()
