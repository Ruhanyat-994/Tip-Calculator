def calculateFoodTotal(food_amount,tip_percentage):
  
  tip_amount=food_amount * (tip_percentage / 100)
  
  total_amount= tip_amount+food_amount
  
  return total_amount
  
print(calculateFoodTotal(100,20))