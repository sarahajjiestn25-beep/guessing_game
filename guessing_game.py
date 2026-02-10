import random
print("🎲 Welcome to the number Guessing Game!")
secret_number=random.randint(1,10)
attempt=0

while True:
   guess=input("Guess a number between 1 and 10:")
   guess=int(guess)

   attempt+=1
   if guess == secret_number:
      
      print("🎉Correct you guessed the number in ",attempt,"tries") 
      break 
   elif guess>secret_number:
     print("Too high ! try again")
   else :
     print("Too low ! try again") 
   
