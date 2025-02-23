l = []

l.append(15)
l.append(55)
l.append(95)
print(l)

temp = l.pop()
print(f"last poped element : {temp}")
print(l)

l.append(62)
print(l)

print("First element in stack",l[-1])

print("Is stack empty? :",len(l) == 0)  