def shutdown(user_input):
  if user_input == "Yes" or user_input == "yes":
    print("Shutting down")
  elif user_input == "No":
    print("Abort shut down")
  else:
    pass


choice = input("Do you want to shut down the system? (Yes/No): ")
shutdown(choice)