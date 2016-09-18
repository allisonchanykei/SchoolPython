

def divide(x):
    rem = x % 2
    div = x // 2
    bin.append(str(rem))
    print div, rem
    if div == 0:
        return
    else:
        divide(div)

n=int(raw_input())
bin=[]
divide(n)
print "".join(bin[::-1])
