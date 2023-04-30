#!/usr/bin/env python3
import sys
import openai

#lines below are to add api key as an env variable
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def default():
	print("Empty!")

def execute():
	entra = sys.argv[1]
	text = f"""{entra}"""
	prompt = f"""Answer the question delimited by the backticks. ```{text}```"""
	response = get_completion(prompt)
	print(response) #FOR CONTROL

def main():
	if len(sys.argv) < 2:	
		default()
	else:
		execute()

if __name__ == "__main__":
	main()
