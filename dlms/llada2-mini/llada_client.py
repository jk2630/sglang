import requests

SERVER_URL = "http://localhost:30000/v1/chat/completions"
MODEL = "inclusionAI/LLaDA2.0-mini"


def generate(prompt):
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": 0,
        "max_tokens": 256,
    }

    response = requests.post(
        SERVER_URL,
        json=payload,
        timeout=300,
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    prompt = input("Enter prompt: ")

    try:
        output = generate(prompt)

        print("\n--- LLaDA2 Response ---")
        print(output)

    except requests.exceptions.ConnectionError:
        print("Could not connect to SGLang server at localhost:30000")
        print("Make sure server.py is running.")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")