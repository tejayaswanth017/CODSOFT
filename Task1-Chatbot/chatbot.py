print("Welcome to Codsoft Chatbot!")
user_name = input("Enter your name: ")
print("Welcome", user_name)
while True:
   question = input("What are your plans today? ").lower()
   if "coding" in question:
    print("Oh thats wonderful! ")
   elif "learn" in question:
    print("Nice try to learn python and ace that skill!")
   elif "sleep" in question:
    print("I apreciate that but please be some productive!!")
   elif "bye" in question:
    print("bye")
    break
   else:
    print("Have a nice day!!")