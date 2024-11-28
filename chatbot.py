import requests

# Set up your Gemini API endpoint and API key
GEMINI_API_URL = '''https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY
'''
API_KEY = 'AIzaSyAZ6uVvPoLek51VPD2DSdf3Wh6alcbPhTA'  # Use your actual API key

def get_gemini_response(user_input):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Set up the payload for the Gemini API request
    payload = {
        "messages": [
            {"role": "user", "content": user_input}  # Send user input
        ]
    }

    # Make the API call
    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        # Parse the response from Gemini API
        data = response.json()
        # Assuming the response contains a 'content' field with the chatbot's reply
        return data['responses'][0]['content']
    else:
        return "Sorry, I couldn't understand that."

def chat():
    print("Welcome to the Gemini Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        # Get chatbot response from Gemini API
        bot_response = get_gemini_response(user_input)
        print(f"Gemini Bot: {bot_response}")

if __name__ == "__main__":
    chat()
