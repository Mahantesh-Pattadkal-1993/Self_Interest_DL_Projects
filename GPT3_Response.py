# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import openai
import os


input_string = "Where is India?"
API_key =  "************"

#Assign API Key 
openai.api_key = API_key

#function to get response from GPT3 via API
def GPT3(stext):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= stext,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
        )
  return response.choices[0].text.split('.')

#Convert the response to string and append as paragraph
def response_to_string(response):    
    output = " "
    for i in response:
        output = output + " " + i
    return output

# Get the response from GPT3
GPT3response =  GPT3(input_string) 

#Convert the response into string format and append as paragraph
output = response_to_string(GPT3response) 
print(output)