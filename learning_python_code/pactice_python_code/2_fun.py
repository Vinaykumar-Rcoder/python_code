


def calculater(n1, n2 , operator):

    if operator == "+":
        print(n1 + n2)

    elif operator == "-":
        print(n1 - n2)

    elif operator == "*":
        print(n1 * n2)

    elif operator == "/":
        print(n1 / n2)

    else:
        print("invalid")

calculater(10,20,"*")

def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(250)

def chek_pass(pswd):
    upper_letter = False
    lower_letter = False
    Digit = False
    special_letter = False

    for ch in pswd:
        if ch.isupper():
            upper_letter = True
        elif ch.islower():
            lower_letter = True
        elif ch.isdigit():
            Digit = True
        else:
            special_letter = True
    
    if len(pswd)<8:
        return "Weak (length <8)"
    elif not upper_letter:
        return "Weak (no upper letter)"
    elif not lower_letter:
        return "Weak (no lower letter)"
    elif not Digit:
        return "no digit"
    else:
        return "Strong Password"
    
pswd = input(" Enter a strong password: ")
result = chek_pass(pswd)
print(result)
    
