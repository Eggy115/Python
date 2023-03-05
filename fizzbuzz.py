a = 0
for i in range(100):
  a = a + 1
  d = a
  
  b = a % 3
  if b == 0:
    d = "Fizz"
    b = a % 5
    if b == 0:
      d = "FizzBuzz" 
      
  b = a % 5
  if b == 0:
    d = "Buzz"
    b = a % 3
    if b == 0:
      d = "FizzBuzz" 
  
  print(d)
  d = a
