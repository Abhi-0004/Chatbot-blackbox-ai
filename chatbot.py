import requests
import json

def send_message(message):
    url = 'https://blackbox.ai/api/inference'
    headers = {
        'Content-Type': 'application/json',
        'key': '*Black-box API Key*' #replace with your API key
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return json.loads(response.content)['message']['content']
    else:
        return None

def chatbot():
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'quit':
            break

        response = send_message(user_message)
        if response:
            print("Blackbox AI: " + response)
            print("\n\n")

if __name__ == "__main__":
    chatbot()