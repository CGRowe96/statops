import math as m 

usera = int(input("Please enter coeeficient a: "))
userb = int(input("Please enter coefficient b: "))
userc = int(input("Please enter constant c: "))

#square root of b^2 - 4ac
square = m.sqrt(abs(pow(userb,2)-(4*(usera*userc))))

#over 2a
divide = 2*usera

#negative b
negb = -abs(1)*userb

#negative b + or - the square root of b^2 - 4ac over 2a
firstroot = (negb+square)/divide
secondroot = (negb-square)/divide

print("Your roots are: " + str(firstroot) + " and " + str(secondroot))