import google.generativeai as genai
import time

time.clock = time.time()

GeminiKey = "AIzaSyD52HdH7tqGJCPntv0A3dj5UbTqYrcKdRY"
genai.configure(api_key = GeminiKey)
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

chat = model.start_chat(history=[])

while True :
    message = input("User>>> ")
    response = chat.send_message(message)
    print(f"Chat>>> {response.text}")