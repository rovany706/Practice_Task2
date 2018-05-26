numA = input()
numB = input()

maxA = numA

for i in range(0, len(numA)):
    numA = numA[1:] + numA[0]
    maxA = max(maxA, numA)

minB = numB

for i in range(0, len(numB)):
    numB = numB[1:] + numB[0]
    if(numB[0] != '0'):
        minB = min(minB, numB)

print(int(maxA) - int(minB))