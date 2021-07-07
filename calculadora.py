print('===== CALCULANDO IMC =====')

peso = float(input('Informe o seu peso: '))
altura = float(input('Agora informe a sua altura separada por ".": '))
n = int(input('Seu peso é {0} e sua altura é {1}. Correto? (responda 1 para SIM e 0 Para NÃO) '.format(peso, altura)))
if n==1:
    imc = peso/(altura*altura)
    print('Seu IMC é {}'.format(imc))
    if(imc>=18) and (imc<=25):
        print('Parabéns, o seu IMC está ideal!')
    else:
        print('Seu IMC está fora do padrão desejável, procure ajuda de um profissional.')
else:
    print('Informe seu peso e altura corretamente.')
    peso1 = float(input('Peso: '))
    altura1 = float(input('Altura: '))
    imc1 = peso1/(altura1*altura1)
    print('Seu IMC é {}'.format(imc1))
    if(imc1>=18) and (imc1<=25):
        print('Parabéns, o seu IMC está entre o ideal!')
    else:
        print('Seu IMC está fora do padrão desejável, procure ajuda de um profissional.')
