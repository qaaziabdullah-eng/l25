class parrot:
    sp="bi"
    def __init__(self,n,a):
     self.n=n
     self.a=a

c=parrot("cherry",6)
t=parrot("tom",5)

print("cherry and tom are", c.sp)
print("{} is {}year old".format(c.n, c.a) )
print("{} is {}year old".format(t.n, t.a) )