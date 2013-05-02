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
        return a
        
v = finance.TimeSeries([1..10**7])
v.plot_histogram(bins=a)
v.plot_histogram(bins=50,normalize=False,aspect_ratio=1)
