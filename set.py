class Set:
    def __init__(self , set):
        self.set = set

    def __and__(self , other):
        return self.set & other.set

    def __or__(self , other):
        return self.set | other.set
    
    def __xor__(self , other):
        return self.set ^ other.set


s1 = Set({1 ,2 ,5 ,7})
s2 = Set({1 ,2 ,13 ,24})
s3 = Set({1 , 5 , 17 , 69 , 43})
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)