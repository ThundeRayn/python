# Python program to demonstrate working of extended 
# Euclidean Algorithm 
     
# function for extended Euclidean Algorithm 
def ExtendedEuclidean(r0, r1): 
    # Base Case 
    if r0 == 0 : 
        return r1,0,1
             
    gcd,s1,t1 = ExtendedEuclidean(r1%r0, r0) 
     
    # Update x and y using results of recursive call
    s = t1 - (r1//r0) * s1
    t = s1
     
    return gcd,s,t 


# Driver code 
r0 = 164554569211088430770706425287401139967
r1 = 316812464220963669296170073138677641820785101655675695
g, s, t = ExtendedEuclidean(r0, r1) 
print("gcd(", r0 , "," , r1, ") = ", g,", s=",s,", t=", t)

# the final answer is:
# gcd = r = 1 ,
# s= -124216592303027604861431220459683160012102867347860412,
# t= 64518950936973762243876029126244056779
