"""
Basic calulator that abides by BODMAS. This calculator will only work with whole numbers and uses brackets

Issues:
Can't do simple calculations
Has issues replacing parts of the calculated equation
No error handling at the moment so it won't account for letters or lack of opening/closing brackets

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
    '''
    This function is to get the number of positions to replace or to get the whole number before the next non character.
    :param equat: the equation such as 2+222/45
    :param ope: the arithemetic operation such as +-/*
    :param op: whether to get the number or position. So either n or p should be supplied
    :return: either the two numbers or number of positions in an array
    '''

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
    """
    This will do the calculation based on the operation and then replace that part of the string with the answer
    :param equat: the equation to calculate
    :return: the calculated answer
    """
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
    """
    Determin that last set of brackets in the equatoin and then calculate and replace it. For example 2*(5+(17-7))
    should calculate and return 2*(5+10)
    :param equat: equation which should contain brackets
    :return: return the equation with the most inner brackets calculated and replaced
    """
    brack = equat[equat.rfind("(") + 1:equat.find(")")]
    outer = equat[equat.rfind("("):equat.find(")") + 1]
    answer = calculate(brack)
        # answer = equat.replace(equat[equat.rfind("("):equat.find(")")+1], str(answer))
    equat = equat.replace(outer, str(answer))
    return equat


def calculator(equat):
    """
    Base function to loop and call the other functions until an integer which would represent the answer is available.
    :param equat: the equation given by the user
    :return: the answer of the equation
    """
    answer = equat.strip(" ")
    test = ""

    if "(" in answer:
        test = brackets(answer)
    else:
        test = calculate(answer)
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
equation = "2+2 * (6/3)"
print("Answer: ", calculator(equation))

# print(brackets("8*(4+(3+9)-3)"))


