string = input("Insira a string: ")

# criando uma lista vazia para armazenar os caracteres invertidos
string_invetida = []

# iterando sobre cada caractere da string a partir do último até o primeiro
for i in range(len(string)-1, -1, -1):
    string_invetida.append(string[i])

# juntando a lista invertida de caracteres em uma nova string
nova_string = ''.join(string_invetida)

# imprimindo a nova string invertida
print(nova_string)
