HW4-2
=====
def isprime(startnumber):
     startnumber*=1.0
     for divisor in range(2,int(startnumber**0.5)+1):
         if startnumber/divisor==int(startnumber/divisor):
             return False
     return True
    
for i in range(10**7+1):
    if isprime(i) == True:
        a = i
        b = mod(i,15)
        return b
        

stats.TimeSeries([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]).plot_histogram(b)
