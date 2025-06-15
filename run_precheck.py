import subprocess

def check_model_exists(model_name):
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    return model_name in result.stdout

def run_precheck():
    model = "llama3.2"
    embed_model = "mxbai-embed-large"

    for m in [model, embed_model]:
        if not check_model_exists(m):
            print(f"Missing model: {m}. Run: `ollama pull {m}`")
        else:
            print(f"✅ Model '{m}' is available.")

if __name__ == "__main__":
    run_precheck()
