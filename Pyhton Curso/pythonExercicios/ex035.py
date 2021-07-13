#Leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

num1 = float(input('Primeiro segmento: '))
num2 = float(input('Segundo segmento: '))
num3 = float(input('Terceiro segmento: '))

if num1 < num2 + num3 and num2 < num2 + num3 and num3 < num1 + num2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO FORMAR um triângulo!')

