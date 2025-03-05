class Node:
    def __init__(self,coeff,exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

class Polinomial:
    def __init__(self):
        self.head = None
    def insert(self,coeff,exp):
        new_node = Node(coeff,exp)

        if not self.head or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next and temp.next.exp >= exp:
                temp = temp.next
            if temp.exp == exp:
                temp.coeff+=coeff
            else:
                new_node.next = temp.next
                temp.next = new_node
    def display(self):
        temp = self.head
        l = []

        while(temp):
            l.append(f"{temp.coeff}x^{temp.exp}" if temp.exp != 0 else f"{temp.coeff}")
            temp = temp.next
        print("+".join(l) if l else "0")


    def add(pol1,pol2):
        result = Polinomial()
        p1 = pol1.head
        p2 = pol2.head
        while p1 and p2:
            if p1.exp > p2.exp:
                result.insert(p1.coeff,p1.exp)
                p1 = p1.next
            elif p1.exp < p2.exp:
                result.insert(p2.coeff,p2.exp)
                p2 = p2.next
            else:
                result.insert(p1.coeff+p2.coeff,p1.exp)
                p1 , p2 = p1.next,p2.next
        while p1:
            result.insert(p1.coeff,p1.exp)
            p1 = p1.next
        while p2:
            result.insert(p2.coeff,p2.exp)
            p2 = p2.next

        return result



def get_poli():
    pol = Polinomial()
    n = int(input("Enter the number of terms : "))
    for i in range(n):
        print(f"Enter terms {i+1}:")
        coeff = int(input("Coeff : "))
        exp = int(input("Exponent : " ))
        pol.insert(coeff,exp)
    return pol 

    
if __name__ == "__main__":
    print("Enter details of first polinomial")
    pol1 = get_poli()
    print("Enter details of second polinomial")
    pol2 = get_poli()
        
    res = Polinomial.add(pol1,pol2)
    print("Result after polinomial addition : ")
    res.display()