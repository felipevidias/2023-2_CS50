
n = int(input("Quantos termos? "))

# primeiro e segundo numero da sequencia
n1, n2 = 0, 1
count = 0

# checar se o numero e valido
if n <= 0:
   print("Digite um inteiro valido: ")
# se tiver so um termo, retornar 1
elif n == 1:
   print("Fibonacci : ",n,":")
   print(n1)
# gerar fibonacci
else:
   while count < n:
       nth = n1 + n2
       # atualizar valores
       n1 = n2
       n2 = nth
       count += 1

print(f"{n2}")
