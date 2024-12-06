from crewai import LLM

# works, but dogshit using my personal machine

base_url = "http://localhost:11434"
model = "dolphin-llama3:8b"

def test_ollama_connection():
    """Test if Ollama LLM is responsive using direct request"""
    import requests

    print(f"Testing connection to {base_url} with model {model}")
    try:
        response = requests.post(
            f"{base_url}/api/generate",
            json={"model": model, "prompt": "test", "stream": False}
        )
        if response.status_code != 200:
            raise Exception(f"Server returned status code {response.status_code}")
        
        print("Ollama connection successful")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to Ollama server: {str(e)}")
        return False

def get_ollama_llm():
    """Configure and return Ollama LLM instance"""
    if not test_ollama_connection():
        raise Exception("Ollama LLM is not available")
    return LLM(
        model=f"ollama/{model}",
        base_url=base_url,
    )