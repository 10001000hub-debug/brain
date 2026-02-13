import sys
import json
import requests

# Ollamaの設定
OLLAMA_URL = "http://100.64.180.83:11434/api/chat"
MODEL_NAME = "llama3:latest"

def chat_with_ollama(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Answer concisely."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        # 初回ロード対策でタイムアウトを300秒(5分)に延長
        response = requests.post(OLLAMA_URL, headers=headers, json=data, timeout=300)
        response.raise_for_status()
        result = response.json()
        return result['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 local_chat.py <prompt>")
        sys.exit(1)
    
    prompt = sys.argv[1]
    print(chat_with_ollama(prompt))
