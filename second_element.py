import sys
def getSecondOrderElements(n,a):
    slargest=secondlargest(n,a)
    ssmallest=secondsmallest(n,a)
    return [slargest,ssmallest]
    



def secondlargest(n,a):
    largest=a[0]
    slargest=-1
    for i in range (n):
        if a[i]>largest:
            slargest=largest
            largest=a[i]
        elif a[i]<largest and a[i]>slargest:
            slargest=a[i]
    return slargest


def secondsmallest(n,a):
    smallest=a[0]
    ssmallest=sys.maxsize
    for i in range (n):
        if a[i]<smallest:
            ssmallest=smallest
            smallest=a[i]
        elif a[i]!=smallest and a[i]<ssmallest:
            ssmallest=a[i]
    return ssmallest
