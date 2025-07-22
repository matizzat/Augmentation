import csv as csv
import requests
import json 
import pandas as pandas

__all__ = [
    "get_file_content", "save_as_csv",
    "call_llm"
]

def get_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content 

def save_as_csv(dictionary, path):
    dataframe = pandas.DataFrame(dictionary)
    dataframe.to_csv(path, index=False)

def call_llm(llm_data, prompt):
    payload = {
        "model": llm_data['llm_name'],
        "messages": [
            {"role": "user", "content": prompt} 
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }  

    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(
            llm_data['url'], 
            headers = headers,
            data = json.dumps(payload)
    )

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"