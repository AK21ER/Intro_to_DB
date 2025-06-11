weather = ["sunny","rainy","cold"]
answer = input(" What's the weather like today? (sunny/rainy/cold):")
if answer == weather[0] :
    print("wear a t-shirt and sunglass")
elif answer == weather[1] :
    print("Don't forget your umbrella and a raincoat")
elif answer == weather[2] :
    print(" Make sure to wear a warm coat and a scarf")
else :
    print(" Sorry, I don't have recommendations for this weather.")
