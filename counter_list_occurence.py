#from collections import Counter
#list1=['apple','egg','apple','banana','egg','apple']
#counts = Counter(list2)
#print(counts)

char = 'gvzmyfhhebpwauvgvdnqvbohojcmlnvhcixxwntrrwialvzdtibtohouihaxzwiddbqjrbrzvtonzgidfqjndrbosgrzdvobbvpvnqddsfzvnnbtdgxbfvnmrwitrraddcgcabvnqfsongjfsatdnsgmvnnvhracacomonbotrnhrecucplnictaqrtvr'
charX=''
charY=''
charZ=''
charK=''
charJ=''
charL=''
charM=''
charN=''
charO=''
charI=''

for x in range(1,190,1):
    if (x%5 == 1): #in X
        charX=charX+char[x-1]

    if (x%5 == 2): #in Y
        charY=charY+char[x-1]
        
    if (x%5 == 3): #in Z
        charZ=charZ+char[x-1]

    if (x%5 == 4): #in L
        charL=charL+char[x-1]
        
    if (x%5 == 0): #in M
        charM=charM+char[x-1]

    #if (x%9 == 6): #in N
     #   charN=charN+char[x-1]

    #if (x%9 == 7): #in O
    #    charO=charO+char[x-1]
        
    #if (x%9 == 8): #in I
    #    charI=charI+char[x-1]
        
    #if (x%9 == 0): #in J
    #    charJ=charJ+char[x-1]

    #if (x%10 == 0): #in K
    #    charK=charK+char[x-1]
        

print(charX)
print(charY)
print(charZ)
print(charL)
print(charM)
print(charN)
print(charO)
print(charI)
print(charJ)
print(charK)

    
