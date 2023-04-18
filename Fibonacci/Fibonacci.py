num = int(input("Informe um número: "))

# define os primeiros valores da sequência de Fibonacci
fib = [0, 1]

# calcula a sequência de Fibonacci
while fib[-1] < num:
    fib.append(fib[-2] + fib[-1])

# verifica se o número informado pertence à sequência de Fibonacci
if num in fib:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
