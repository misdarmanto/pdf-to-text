from dotenv import load_dotenv
import os

load_dotenv()

weaviate_configs = {
    "weaviate_instance_url": os.getenv("WEAVIATE_INSTANCE_URL"),
    "weaviate_api_key":  os.getenv("WEAVIATE_API_KEY"),
    "openai_api_key":  os.getenv("OPENAI_API_KEY"),
}

