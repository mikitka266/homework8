def number_init(number, str1):
    if number==int(len(str1)) and str1.isdigit()==1:
        print("длина последовательности подходит к условию задачи")
    else: print("длина последовательности не подходит к условию задачи")

def reverse_string(str1):
    return "".join(reversed(str1))

