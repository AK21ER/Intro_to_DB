
def display_menu() :
    print("Shopping List Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"Item {item} added to the list.")
        elif choice == "2" :
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else : 
                print("the  item is not founded in the list")
        elif choice == "3" :
            for item in shopping_list :
                print(item)
                print("")
        elif choice == "4" :
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
