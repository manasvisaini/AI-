def chatbot():
    print("AI Chatbot (Demo Version)")
    print("Type 'exit' to stop\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if "ai" in user_input.lower():
            print("Bot: AI means Artificial Intelligence.")
        else:
            print("Bot: This is a demo AI response.")

if __name__ == "__main__":
    chatbot()
