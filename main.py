import os
from google import genai

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyAxcJHONyYRi-QahuR2ZOV_uin30mplD6Y")

# Naruto persona prompt
naruto_prompt = """
You are Naruto Uzumaki from the Hidden Leaf Village.
You are cheerful, optimistic, and never give up. 
Speak in an energetic, friendly way, and often end sentences with 'Dattebayo!'.
Talk about your dream of becoming Hokage, your friends, and your love for ramen.
Encourage others to follow their dreams, like Naruto would.
"""

def get_naruto_reply(user_message):
    full_prompt = f"{naruto_prompt}\nUser: {user_message}\nNaruto:"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    return response.text

# Chat loop
print("🍜 Naruto Chatbot is ready! Type 'exit' to leave.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Naruto: Believe in yourself and keep going, Dattebayo! See ya!")
        break
    naruto_reply = get_naruto_reply(user_input)
    print(f"Naruto: {naruto_reply}")