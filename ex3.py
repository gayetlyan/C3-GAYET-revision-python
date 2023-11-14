nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))


def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division par zéro impossible"

print(f"Addition : {addition(nombre1, nombre2)}")
print(f"Soustraction : {soustraction(nombre1, nombre2)}")
print(f"Multiplication : {multiplication(nombre1, nombre2)}")
print(f"Division : {division(nombre1, nombre2)}")