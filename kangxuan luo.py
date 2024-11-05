homework13
def quadraticFormula1(a,b,c):
    z = b**2-4*a*c
    if z>=0:
        return((-b+z**0.5)/2*a)
    else :
        print("error")

def quadraticFormula2(a,b,c):
    z = b**2-4*a*c
    if z>=0:
        return((-b-z**0.5)/2*a)
    else :
        print("error")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

print("root1:",quadraticFormula1(a,b,c))
print("root2:",quadraticFormula2(a,b,c))

homework14
def bio(name, born, pronoun):
    age = 2024 - born
    agee = born + 67
    print(name, "was born in", born)
    print(pronoun, "will turn", age, "years old this year")
    print(pronoun, "will be 67 in the year", agee)


bio("stephen", 1984, "he")
bio("mary", 1990, "she")
bio("jane", 2000, "she")


quit()
