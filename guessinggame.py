import random

print('number guessing game')

number=random.randint(1,10)
#print(number)
chances=0 
print('guess a number between 1 to 10')

while chances<5:
        guess=int(input("Enter your guess:"))
        if guess==number:
            print ("Congratulations! You guessed correctly")
            break
        elif (guess<number):
            print ("guess again with number greater than",guess)
        else:
            print ("guess again with number lesser than",guess) 
        
        chances+=1

if chances>=5 :
    print('you lost the number is :',number)