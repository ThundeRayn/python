a = 476219007220973994303455600579
d = 113087485233248996526571115482
p = 669379343040372993112682310767
b = 46068278352860145239739472275
Ke = 291905782067546206475817580403
Ke_inverse = 237244748633151472946335322384
x = 621822214279358881560423056296
r = 117212702825613395455875546701
s = 467903002855476878700153000716
xt = 435774528075745568404129942557
xr = 177713884672348018778214374286
xs = 648290288896956791824851873445
p1=79387461981461589274553230681
p2=72789827710040175797007602490
t = 56446820283656945637266465730
ax = 218754521513540549784295590658

A=a
B=d
P=p


#modulus exponential
#- cannot calculate inverse
#- cannot calculate large expo
'''result_exp=(A**B)%P
print(str(A**B))
#print(str(A)+"^"+str(B) +" mod "+str(P)+" is = "+str(result_exp))'''

C=p1
D=p2

#modulus mutiplication
result_multi=(C*D)%P
print(str(C)+"*"+str(D) +" mod "+str(P)+" is = "+str(result_multi))

E=Ke
#modulus inverse
'''result_inv = pow(E, -1, P)
print(str(E)+" ^(-1) mod"+str(P)+" is "+str(result_inv))
print(result_inv==Ke_inverse)'''
