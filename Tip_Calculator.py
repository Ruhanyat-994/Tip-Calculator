food_amount = float(input("Please enter your food amount: "))
tip_percentage = float(input("Enter the tip percentage :"))/100
tip_amount = food_amount * tip_percentage

total_amount= food_amount+tip_amount
print("-------------------------")
print(f"🍔 Food_Amount : ${food_amount}\n ")

print(f"🍽️  Tip_Percentage : ${ tip_percentage}\n")

print(f"❤️ Tip_Amount : ${tip_amount}\n")

print(f"💵 Total_Amount : ${total_amount}")
print("-------------------------")
