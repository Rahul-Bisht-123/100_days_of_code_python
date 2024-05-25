num = int(input("Enter the number to be checked for prime : "))
def isPrime(number):
  prime = True
  for i in range(2, number):
    if(number % i == 0):
      prime = False
      break
  
  if prime:
    print(f"{number} is prime")
  else:
    print(f"{number} is not prime")

isPrime(num)