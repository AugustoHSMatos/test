# 1 – Dado o seguinte vetor [1,2,4,16,32,64,-128] implemente um procedimento que indique menor e
# o maior elemento do vetor
tam = 7
vetor_numero = [int] * tam
for i in range(len(vetor_numero)):
    vetor_numero[i] = int(input('Digite o valor \t'))
valor_a=vetor_numero[0]
valor_b=vetor_numero[0]
for i in range(len(vetor_numero)):
    if vetor_numero[i] > valor_a:
        valor_a = vetor_numero[i]
    if vetor_numero[i] < valor_b:
        valor_b = vetor_numero[i]
print('-'*50)
print(vetor_numero)
print('Quantidade de numeros no vetor:', len(vetor_numero))
print('O resultado de Maior', valor_a)
print('O resultado do Menor', valor_b)
