def sum(a:int ,b:int ) -> int :

  return(a+b)
  

def test_sum():
  assert sum(-20,20)==0
  assert sum(450,450)==900
  assert sum(230,270)==500 
  
  print("Sum function: All Tests Passed (3/3) ✅")
  
test_sum()

