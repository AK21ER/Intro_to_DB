pattern = int(input("Enter the size of the pattern :"))
starter= 0
while starter < pattern:
    for i in range(0,pattern) :
        print("*" , end="/")
        i+1
    print()
    starter += 1