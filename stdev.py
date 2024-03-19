import math as m 

lst = []
total = 0
meanlst = []
sqrlist = []
totaltodiv = 0

n = int(input("Enter number of elements: "))

#making the list
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

#adding each value in list
for x in lst:
    total += x

#mean
sdmean = total/n

#subtracting mean from each item
for z in lst:
    meanlst.append(z-sdmean)

#squaring each item
for y in meanlst:
    sqrlist.append(pow(y,2))

#summing the new list
for a in sqrlist:
    totaltodiv += a

#calculating standard deviation
stdev = m.sqrt(totaltodiv/n)

print(stdev)

#printing bell curve labels from -3stdev to +3stdev
print("Your deviations are: " + str(round(sdmean-(stdev*3),3)) + ", " + str(round(sdmean-(stdev*2),3)) + ", " + str(round(sdmean-stdev,3)) + ", " + str(round(sdmean,3)) + ", " + str(round(sdmean+stdev,3)) + ", " + str(round(sdmean+(stdev*2),3)) + ", " + str(round(sdmean+(stdev*3),3)))