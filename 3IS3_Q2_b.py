# ----------------
# ----3IS3 A2-----
# ----------------
# python program for extended Euclidean Algorithm
# ----------------


def ExtendedEuclidean(r0, r1): 
    s0=1
    s1=0
    t0=0
    t1=1
    i=1

    while (ri!=0):
        i=0
             
    #gcd,x1,y1 = ExtendedEuclidean(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    #x = y1 - (b//a) * x1 
    #y = x1 
     
    return gcd,s,t
     
 
# Driver code 
a, b = 625,110
g, x, y = ExtendedEuclidean(a, b) 
print("gcd(", a , "," , b, ") = ", g,", ") 
