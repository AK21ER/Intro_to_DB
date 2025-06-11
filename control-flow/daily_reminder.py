Task = input("Enter your task: ")
Priority = input("Enter your priority (high, medium, low): ")
TimeBound = input("Is it time-bound? (yes/no): ") 
if TimeBound.lower() == "yes":
    match Priority.lower():
        case "high":
         print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!")
        case "medium":
          print(f"Reminder: '{Task}' is a {Priority} priority task that requires attention today!")
        case "low":
          print(f"Reminder: '{Task}' is a {Priority} priority task that can be done at")
elif TimeBound.lower() == "no":
   match priority.lower():
      case "high":
         print(f"Note: '{Task}' is a {Priority} task. that requires immediate attention!")
      case "medium":
         print(f"Note: '{Task}' is a {Priority} task. that requires attention!")
      case "low":
          print (f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time.")
else : print("Invalid input")
