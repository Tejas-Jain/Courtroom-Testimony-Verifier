import requests
from dotenv import load_dotenv
import os
import pandas as pd
import torch
load_dotenv()

model_id = os.getenv("model_id")
hf_token = os.getenv("hf_token")
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def getEmbeddings(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    embeddedData = response.json()
    return torch.FloatTensor(embeddedData)


# #  Preparing Embeddings from the text and converting it to CSV for UI uploading
texts = ["How do I get a replacement Medicare card?",
        "What is the monthly premium for Medicare Part B?",
        "How do I terminate my Medicare Part B (medical insurance)?",
        "How do I sign up for Medicare?",
        "Can I sign up for Medicare Part B if I am working and have health insurance through an employer?",
        "How do I sign up for Medicare Part B if I already have Part A?",
        "What are Medicare late enrollment penalties?",
        "What is Medicare and who can get it?",
        "How can I get help with my Medicare Part A and Part B premiums?",
        "What are the different parts of Medicare?",
        "Will my Medicare premiums be higher because of my higher income?",
        "What is TRICARE ?",
        "Should I sign up for Medicare Part B if I have Veterans' Benefits?"]
# dataset_embeddings = getEmbeddings(texts)


question = ["How can Medicare help me?", 
            "What are the benefits of Insurance", 
            "What is Medicare and who can get it?"]
# query_embeddings = getEmbeddings(question)

from sentence_transformers.util import semantic_search
def mis_matches(dataset, queryset, threshold=0.9):
    dataset_embeddings = getEmbeddings(dataset)
    query_embeddings = getEmbeddings(queryset)
    ans = []
    for index, embedding in enumerate(query_embeddings):
        hits = semantic_search(embedding, dataset_embeddings, top_k=1)
        if(hits[0][2]>threshold):
            ans.append([index, hits[0][0]['corpus_id'], hits[0][0]['score']])
            print([dataset[hits[i]['corpus_id']] for i in range(len(hits))])
    print("Ans:", ans)
    
mis_matches(text, questions, 0.5)