class Num:
    def __init__(self , num):
        self.num = num

    def __add__(self , other):
        return self.num + other.num
    
    def __sub__(self , other):
        return self.num - other.num
    
    def __abs__(self):
        if self.num >= 0:
            return self.num
        
        else:
            return -self.num
        
    def __mul__(self , other):
        return self.num * other.num
    
    def __truediv__(self , other):
        return self.num / other.num
    
    def __eq__(self , other):
        return self.num == other.num
    
    def __lt__(self , other):
        return self.num < other.num
    

    def __pow__(self , other):
        return self.num ** other.num
    

    



n1 = Num(-10)
n2 = Num(5)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 ** n2)
print(n1 == n2)
print(n1 < n2)
print(abs(n1))
