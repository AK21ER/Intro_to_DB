task = input("Enter your task: ")
priority = input("Enter your priority (high, medium, low): ")
timeBound = input("Is it time-bound? (yes/no): ") 
if timeBound.lower() == "yes":
    match priority.lower():
        case "high":
         print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        case "medium":
          print(f"Reminder: '{task}' is a {priority} priority task that requires attention today!")
        case "low":
          print(f"Reminder: '{task}' is a {priority} priority task that can be done at")
elif timeBound.lower() == "no":
   match priority.lower():
      case "high":
         print(f"Note: '{task}' is a {priority} task. that requires immediate attention!")
      case "medium":
         print(f"Note: '{task}' is a {priority} task. that requires attention!")
      case "low":
          print (f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
else : print("Invalid input")
