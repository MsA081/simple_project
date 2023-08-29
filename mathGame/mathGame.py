import random , operator

def random_operator() :
    operators = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "//" : operator.truediv
    }

    first_number = random.randint(1,100)
    second_number = random.randint(1,100)
    operator_chosen = random.choice(list(operators.keys()))

    result = operators.get(operator_chosen)(first_number,second_number)
    print(f"{first_number} {operator_chosen} {second_number}")
    return result

def ask_question () :
    result = random_operator()
    answer = float(input("please enter your answer : "))
    return result == answer

score = 0
while True:
    if ask_question():
        score += 1
        print('True')
    else:
        print('false')
        break
print("Game Over!!!")
print(f"your score : {score}")