c=0
J={1:1}
supern="110101010110000100001111011001001000001001101110"[::-1]
acu=0
check=0
for i in range(len(supern)):
    h=pow(2,2**i,123456789)
    c*=h
    c+=J[2**i]
    c=c%123456789
    J[2**(i+1)]=c
    if(supern[i]=='1'):
        check+=2**i
        acu*=h
        acu+=J[2**i]
        acu=acu%123456789


print(check,acu)
print(str(J))
