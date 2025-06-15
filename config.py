from langchain_ollama.llms import OllamaLLM
# from langchain_openai import ChatOpenAI  # Uncomment if switching to OpenAI

def get_model():
    # return ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
    return OllamaLLM(model="llama3.2")
