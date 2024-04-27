l = input("enter the elements : ").split(',')
n = int(input("enter element to delete all its occerace : "))
for i in range(len(l)):
    l[i] = int(l[i])
# print(l)
# count = l.count(n)
# print(count)
# for j in range(count):
#     l.remove(n)
# print(l)

r = []
for i in range(len(l)):
    if n != l[i]:
        r.append(l[i])
    else:
        pass

print(*r,sep=',')
