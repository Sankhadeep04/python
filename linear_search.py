pos = 0
def search(l,n):
    i = 0
    while(i < len(l)):
        if(l[i] == n):
            globals()['pos'] = i
            return True
        i+=1
    return False    

l = [1,2,3,4,9,8,6,7]
n = 7

if search(l,n):
    print("Found at: {pos}")
else:
    print("Not found")