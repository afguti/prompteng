#!/usr/bin/env python3
import openai
import re
import os
from dotenv import load_dotenv, find_dotenv
from recorder import record_audio as record
import threading
import subprocess

_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def get_completion_from_message(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def default():
    print("Empty!")

def listen_for_input():
    global user_input
    input("Press ENTER to start recording...")
    user_input = record()

def execute():
    with open("./systems/system", "r") as file:
        text = file.read()
    
    context = [{'role':'system', 'content':f"""{text}"""}]
    while True:
        thread = threading.Thread(target=listen_for_input)
        thread.start()
        thread.join()
        print("You: " + user_input)
        context.append({'role':'user', 'content':f"{user_input}"})
        response = get_completion_from_message(context, temperature=0.3)
        #tts goes here

        context.append({'role':'assistant', 'content':f"{response}"})
        print("Chatbot: ", response)
        answ = response.replace('"','\\"')
        command = f'mimic3 --voice en_US/vctk_low \"{answ}\"'
        subprocess.run(command, shell=True)

def main():
    execute()

if __name__ == "__main__":
    main()
