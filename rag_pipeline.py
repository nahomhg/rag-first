from langchain_core.prompts import ChatPromptTemplate
from config import get_model

def get_prompt():
    template = """
You're an expert in pizza restaurant reviews.

Here are some relevant reviews: {reviews}

Here's the question to answer: {question}
"""
    return ChatPromptTemplate.from_template(template)

def build_rag_chain():
    prompt = get_prompt()
    model = get_model()
    return prompt | model
