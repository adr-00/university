from lib.array_stack import ArrayStack


def validez_parentesis(cadena):
    S = ArrayStack()
    for i in cadena:
        if i == "(":
            S.push("(")
        elif i == ")":
            if len(S) == 0:
                return False
            else:
                S.pop()
    

    if len(S) == 0:
        return True
    elif len(S) != 0:
        return False

if validez_parentesis("(a + (b*c) – 5*(a+b+c)))"):
    print("Correcto")
else:
    print("Incorrecto")  