import random

def getDigit(randomNum):
    return[int(i) for i in str(randomNum)]

def noDuplicate(randomNum):
    numList = getDigit(randomNum)
    if len(numList)==len(set(numList)):
        return True
    else:
        return False

def generateNum():
    randomNum=0
    while True:
        randomNum = random.randint(1000,9999)
        if noDuplicate(randomNum):
            return randomNum

def getBullsCows(userNum,randomNum):
    userInput =getDigit(userNum)
    randomInput = getDigit(randomNum)
    # print(userInput)
    # print(randomInput)
    bull_cow=[0,0]
    for i,j in zip(randomInput,userInput):
        if j in randomInput:
            if i==j:
                bull_cow[0]=+1
            else:
                bull_cow[1]=+1
    return bull_cow

#Generate random number
num=generateNum()
# print("Random number is{1}",num)
tries=int(input("Enter number of tries:"))
count=0
while tries >0:
    userinput=int(input("Guess:"))
    if not noDuplicate(userinput):
        print("Number should not have repeated digits. Try again.")
        continue
    if userinput<1000 or userinput >9999:
        print("Number should be between 1000 and 9999.")
        continue
    bull_cow = getBullsCows(userinput,num)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    if bull_cow[1]==0:
        print("You Guessed It Right!")
        break
    tries=+1