from tokenize import String


def perform_operation(num1:float ,num2:float,operation:String) :
      if operation == "add" :
            return num1 + num2
      elif operation == "substract" :
            return num1 - num2
      elif operation == "multiply" :
            return num1 * num2
      elif operation == "divide" :
            if num2 != 0 :
                  return num1 / num2
            else :
                  return "Error : Division by zero is not allowed"
      else :
        return "Invalid operation"
