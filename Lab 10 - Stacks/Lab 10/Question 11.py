def evaluate_postfix(postfix):
    postfix_list = postfix.split()
    number_stack = Stack()
    for i in postfix_list:
        if i not in "*+-/":
            number_stack.push(i)
        else:
            number_1 = number_stack.pop()
            number_2 = number_stack.pop()
            if i == "*":
                result = int(number_1) * int(number_2)
                number_stack.push(result)
            elif i == "-":
                result = int(number_2) - int(number_1)
                number_stack.push(result)
            elif i == "+":
                result = int(number_1) + int(number_2)
                number_stack.push(result)
            else:
                result = int(number_2) // int(number_1)
                number_stack.push(result)
    final_result = number_stack.pop()
    return final_result






