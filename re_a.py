try:                                                    #requirements check
    import groq
    import dotenv
    print("All required packages are installed.")
except ImportError as e:
    print("Missing package:", e.name)


import os
from dotenv import load_dotenv
from groq import Groq

if os.path.exists(".env"):                          #env file check
     pass 
else:
    api_key = input("Enter your Groq API key: ")

    with open(".env", "w") as f:
        f.write(f"GROQ_API_KEY={api_key}\n")

    print(".env file created and API key saved.")

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))



print("Hello, welcome to the basic chatbot. How can I assist you today?")       #chatbot loop
while True:
    a = input("Enter your request (type 'finish' or 'exit' to quit): ")
    if a.lower() in ["finish", "exit"]:
        print("Conversation ended. Have a nice day!")
        break
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages = [{"role": "user", "content": str(a)}]
    )
    print(response.choices[0].message.content)
