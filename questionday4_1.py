# gcd and lcm program
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
a=int(input())
b=int(input()) 
print(gcd(a, b))
print(lcm(a,b))
       





    
    





 
