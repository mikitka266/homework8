# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
#В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода)
from log2 import number_init, reverse_string

N = int(input('Введите число N:'))
N_string = (input('Введите N последовательность чисел:'))
number_init(N, N_string)
reverse_string(N_string) 
print("".join(reversed(N_string)))