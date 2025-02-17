pos = 0
def search(list,n):
    start  = 0
    end = len(list)-1
    while (start <= end):
        mid = (start+end) // 2

        if(n == list[mid]):
            globals()['pos'] = mid
            return True

        else:
            if list[mid] < n:
                start = mid
            else:
                end = mid
            

list = [1,2,3,5,6,7,9,10,15,16]
n = int(input("Enter the number :"))

if search(list,n):
    print(f"Found at:{pos}")
else:
    print("Not found")