import ollama

class Chat():
    def __init__(self):
        self.history = []

    def ma(self):
        while True:
            self.uip = input("\nWhat do you wish to write (or type 'exit' to stop): ")
            if self.uip.lower() == "exit":
                break

            ai_ou = self.cr()

            self.history.append({"user": self.uip, "ai": ai_ou})

            print("\n---- Chat History ----")
            for turn in self.history:
                print(f"\nUser: {turn['user']}")
                print(f"Chat Bot: {turn['ai']}")
            print("\n----------------------")

    def cr(self):
        messages = [
            {
                "role": "system",
                "content": (
                    "how you want the model to behave" #replace this code here with what or how you want the chat bot to be
                )
            }
        ]

        for turn in self.history:
            messages.append({"role": "user", "content": turn["user"]})
            messages.append({"role": "assistant", "content": turn["ai"]})

        messages.append({"role": "user", "content": self.uip})

        stream = ollama.chat(model="Your ollama model name here", messages=messages, stream=True) #here write the name of your ollama model

        response = []
        for chunk in stream:
            text = chunk["message"]["content"]
            response.append(text)
            print(text, end="", flush=True)

        return "".join(response)

chat = Chat()
chat.ma()
