from groq import Groq

# Initialize client with your API key
client = Groq(api_key="GROQ_API_KEY")

def chat_with_bot(user_message):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # you can change to other available Groq models
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ] 
    )
    return response.choices[0].message.content

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    bot_reply = chat_with_bot(user_input)
    print("Bot:", bot_reply)
