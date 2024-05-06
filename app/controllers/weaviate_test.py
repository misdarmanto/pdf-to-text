import requests
import json
import weaviate

from app.configs.app_configs import weaviate_configs

resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
data = json.loads(resp.text)  

client = weaviate.Client(
    url = weaviate_configs["weaviate_instance_url"],
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=weaviate_configs["weaviate_api_key"]),
    additional_headers = {
        "X-OpenAI-Api-Key": weaviate_configs["openai_api_key"] 
    }
)


class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {},
        "generative-openai": {} 
    }
}

client.schema.create_class(class_obj)

def add_object():
    client.batch.configure(batch_size=100) 
    with client.batch as batch: 
        for i, d in enumerate(data):
            print(f"importing question: {i+1}")
            properties = {
                "answer": d["Answer"],
                "question": d["Question"],
                "category": d["Category"],
            }
            batch.add_data_object(
                data_object=properties,
                class_name="Question"
            )   