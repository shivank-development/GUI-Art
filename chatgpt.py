import openai

# Set your OpenAI API key
openai.api_key = "api-key-here"

# Function to interact with ChatGPT
def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)
