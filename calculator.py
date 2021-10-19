"""
Basic calulator that abides by BODMAS
Some scenarios:

2+2-3
2*9/3

8+(6*(16/4))
    = 8+(6*4)
    = 8*32
    = 256

9/(27/3)
    = 9/9
    = 1
"""
def retNumbers(equat, ope, op):
    num = []
    num1 = ""
    num2 = ""
    if op == "n":
        for x in equat[equat.find(ope) - 1::-1]:
            try:
                num1 += str(int(x))
            except:
                break
        num.append(int(num1[::-1]))

        for x in equat[equat.find(ope) + 1:]:
            try:
                num2 += str(int(x))
            except:
                break
        num.append(int(num2))
    else:
        pos1 = 0
        pos2 = 0
        for x in equat[equat.find(ope) - 1::-1]:
            try:
                num1 += str(int(x))
                pos1 -= 1
            except:
                break
        num.append(pos1)

        for x in equat[equat.find(ope) + 1:]:
            try:
                num2 += str(int(x))
                pos2 += 1
            except:
                break
        num.append(pos2)
    return num


def calculate(equat):
    brack = equat
    while type(brack) is str:

        if "/" in brack:
            # do operation
            # replace section of equation
            num = retNumbers(brack, "/", "n")
            answer = int(num[0] / num[1])
            brack = brack.replace(brack[brack.find("/") + retNumbers(equat, "/", "p")[0]:
                                        brack.find("/") + retNumbers(equat, "/", "p")[1]+1], str(answer))
            print(brack)

        if "*" in brack:
            num = retNumbers(brack, "*", "n")
            print(num)
            answer = num[0] * num[1]
            brack = brack.replace(brack[brack.find("*") + retNumbers(equat, "*", "p")[0]:
                                        brack.find("*") + retNumbers(equat, "*", "p")[1]+1], str(answer))
            print(brack)

        if "+" in brack:
            num = retNumbers(brack, "+", "n")
            answer = num[0] + num[1]
            brack = brack.replace(brack[brack.find("+") + retNumbers(equat, "+", "p")[0]:
                                        brack.find("+") + retNumbers(equat, "+", "p")[1]+1], str(answer))
            print(brack)

        if "-" in brack:
            num = retNumbers(brack, "-", "n")
            answer = num[0] - num[1]
            brack = brack.replace(brack[brack.find("-") + retNumbers(equat, "-", "p")[0]:
                                        brack.find("-") + retNumbers(equat, "-", "p")[1]+1], str(answer))
            print(brack)
        try:
            answer = int(brack)
            break
        except Exception:
            pass

    return brack


def brackets(equat):
    brack = equat[equat.rfind("(") + 1:equat.find(")")]
    outer = equat[equat.rfind("("):equat.find(")") + 1]
    answer = calculate(brack)
        # answer = equat.replace(equat[equat.rfind("("):equat.find(")")+1], str(answer))
    equat = equat.replace(outer, str(answer))
    return equat


def calculator(equat):
    answer = equat.strip(" ")
    test = ""

    if "(" in answer:
        test = brackets(answer)
    else:
        test = calculate(test)
    try:
        test = int(test)
        return test
    except Exception:
        while type(test) is str:
            print("calc", test)
            if "(" in test:
                test = brackets(test)
            else:
                test = calculate(test)
            try:
                test = int(test)
                break
            except Exception:
                pass

    return test





# equation = input("Enter your equation")
equation = "2+2"
print("Answer: ", calculator(equation))

# print(brackets("8*(4+(3+9)-3)"))


