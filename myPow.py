def myPow(self,x,n):
        if n==0:
            return 1
        elif n==1:
            return x
        elif n<0:
            return self.myPow(1/x,-n) 
        elif n%2==0:
            return self.myPow(x,n/2)**2
        else:
            return x*self.myPow(x,n-1)