import math as m 

usera = int(input("Please enter coeeficient a: "))
userb = int(input("Please enter coefficient b: "))
userc = int(input("Please enter constant c: "))
square = m.sqrt(abs(pow(userb,2)-(4*(usera*userc))))
divide = 2*usera
negb = -abs(1)*userb

firstroot = (negb+square)/divide
secondroot = (negb-square)/divide

print("Your roots are: " + str(firstroot) + " and " + str(secondroot))