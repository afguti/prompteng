### This is a set of script for prompt engineering

This set of scripts are part of a short course on prompt engineering offered by Open Ai and deeplearning.ai

#### answer.py
This script answer questions and is a practice of one of the principles of prompt engineering; "Write clear and especific instructions". Espesifically, the tactic number one; "Use delimiters".

#### eigogpt.py
This is an ai assitant that helps to incorporate new words to the learner vocabulary. 

# Audio Transcription Module record.py

This module allows you to record audio and transcribe it using the OpenAI API.

## Installation

To use this module, you need to install the following dependencies:

- sounddevice
- soundfile
- requests

You can install them using pip:


## Usage

First, make sure you have set up your OpenAI API key as an environment variable named `OPENAI_API_KEY`.

```python
Out[1]: from recorder import record_audio as record
record()
Recording audio. Press Enter to stop...

Recording stopped.
Out[2]: "Hey, this is just a try. It's almost 1.52. Thanks!"

graph LR
A[Start] --> B(Record Audio)
B --> C{Enter Key Pressed?}
C -- Yes --> D[Stop Recording]
C -- No --> C
D --> E(Make API Request)
E --> F{Response OK?}
F -- Yes --> G[Retrieve Transcription]
F -- No --> F
G --> H[Return Transcription]



