import random

while 1>0:
    people=input("Your name is:")
    task=input("you want to:")
    num=random.randint(1, 100)
    if num>=50 and num<90:
        res="Success"
    if num>=90:
        res="great success"
    if num <50 and num >10:
        res="failure"
    if num <=10:
        res="tragic failure"
    print(people+" wants to "+task+" and get a "+str(num) +", "+res+"!")
