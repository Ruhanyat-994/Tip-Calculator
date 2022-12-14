def calculateFoodTotal(food_amount,tip_percentage):
  
  tip_amount=food_amount * (tip_percentage / 100)
  
  total_amount= tip_amount+food_amount
  print("-------------------------")
  print(f"🍔 Food_Amount : ${food_amount}\n ")

  print(f"🍽️  Tip_Percentage : ${ tip_percentage}\n")

  print(f"❤️ Tip_Amount : ${tip_amount}\n")

  print(f"💵 Total_Amount : ${total_amount}")
  print("-------------------------")
  
  return total_amount
  
calculateFoodTotal(100,20)