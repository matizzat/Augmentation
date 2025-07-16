from setfit import SetFitModel
from sklearn.metrics import classification_report
import pandas as pandas
import csv as csv
import requests
import json 
import re

def get_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content 

def save_as_csv(dictionary, path):
    dataframe = pandas.DataFrame(dictionary)
    dataframe.to_csv(path, index=False)

def load_dataset(path, labels):
    dataset = {}
    for label in labels:
        dataset[label] = []
    
    with open(path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataset[row['label']].append(row['question'])

    return dataset

def extract_samples(labels, dataset):
    samples = [{'label': 'temporal', 
                'question': dataset['entidad'][0]}
              ]
    return samples

def create_prompt(template, sample):
    return template.format(label = sample['label'],
                           question = sample['question']) 

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

def add_answer(llm_answers, sample, answer): 
    llm_answers.append({
        'answer': answer, 
        'label': sample['label']
    })

def ask_llm_to_augment(labels, dataset, template, llm_data):
    llm_answers = []

    samples = extract_samples(labels, dataset)
    for sample in samples: 
        prompt = create_prompt(template, sample)  
        answer = call_llm(llm_data, prompt)  
        add_answer(llm_answers, sample, answer)

    return llm_answers 

def extract_questions(llm_answer):
    re_query = re.compile(r'¿.*?\?')
    lowercase_answer = llm_answer.lower()
    question_list = re_query.findall(lowercase_answer)
    return question_list

def parse_llm_answers(llm_answers):
    augmented_set = []
    
    for row in llm_answers:
        llm_answer = row['answer'] 
        label = row['label'] 

        question_list = extract_questions(llm_answer)
        for question in question_list:
            augmented_set.append({
                 'question': question, 
                 'label': label
                })
            
    return augmented_set   

def load_augmented_set(path):
    augmented_set = {'question':[], 'label':[]}
    
    with open(path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            augmented_set['question'].append(row['question'])
            augmented_set['label'].append(row['label'])

    return augmented_set

def ask_classifier_to_predict(model_path, labels, questions):
    model = SetFitModel.from_pretrained(model_path)
    model.labels = labels  
    predictions = model.predict(questions)
    return predictions
    
def eval_augmented_set(augmented_labels, predictions):
    class_report = classification_report(augmented_labels,
                                         predictions,
                                         zero_division=0)

    
    print(class_report)
