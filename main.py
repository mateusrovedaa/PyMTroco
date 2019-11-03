import math
print('Máquina de dar troco')
print('Versão 1.0')
print('Máquina feita por: Mateus Roveda')
comecar = 's'
while comecar == 's':
    valid_valor = False
    while valid_valor == False: ##verifica o valor da conta
        valor = input('Digite o valor total da conta: R$')
        try:
            valor = float(valor)
            if valor <= 0:
                print('Digite um valor maior que 0.')
            else:
                valid_valor = True
        except:
            print('O formato digitado não é válido. Use apenas números e separe os decimais com ponto. (Ex. 15.5)')
    valid_pago = False
    while valid_pago == False: ##verifica o valor pago
        pago = input('Digite o valor pago: R$')
        try:
            pago = float(pago)
            if pago <= 0:
                print('Digite um valor maior que 0.')
            else:
                valid_pago = True
        except:
            print('O formato digitado não é válido. Use apenas números e separe os decimais com ponto. (Ex. 15.5)')
    troco = math.fabs(round(pago,2)-round(valor,2)) ##calcula o troco arredondado sempre para duas casas depois da virgula
    if pago<valor:
        print('Você ainda precisa pagar: R$'+str(troco))
    elif valor % pago == 0:
        print('Você pagou o preço exato da conta')
    else:
        print('Seu troco  será de: R$'+str(round(troco,2)))
        print('Calculando...')
        cedulas = [100, 50, 20, 10, 5, 2, 1]##notas
        centavos = [50, 25, 10, 5, 1]##centavos
        vlr = int(troco)
        i = 0
        while vlr != 0: ##calculando notas
            c = int(vlr/cedulas[i])
            if c != 0:
                if c>1 and cedulas[i]>1:
                    print(str(c)+' notas de R$'+str(cedulas[i])+' reais')
                    vlr = vlr % cedulas[i]
                elif c==1 and cedulas[i] > 1:
                    print(str(c)+' nota de R$'+str(cedulas[i])+' reais')
                    vlr = vlr % cedulas[i]
                elif c>1 and cedulas[i] == 1:
                    print(str(c)+' notas de R$'+str(cedulas[i])+' real')
                    vlr = vlr % cedulas[i]
                else:
                    print(str(c)+' moeda de R$'+str(cedulas[i])+' real')
                    vlr = vlr % cedulas[i]
            i += 1
        vlr = int(round((troco - int(troco))*100,2))
        i = 0
        while vlr != 0: ##calculando moedas
            c = int(vlr/centavos[i]) 
            if c != 0:
                if c>1 and centavos[i]>1:
                    print(str(c)+' moedas de R$'+str(centavos[i])+' centavos')
                    vlr = vlr % centavos[i]
                elif c==1 and centavos[i] > 1:
                    print(str(c)+' moeda de R$'+str(centavos[i])+' centavos')
                    vlr = vlr % centavos[i]
                elif c>1 and centavos[i] == 1:
                    print(str(c)+' moedas de R$'+str(centavos[i])+' centavo')
                    vlr = vlr % centavos[i]
                else:
                    print(str(c)+' moeda de R$'+str(centavos[i])+' centavo')
                    vlr = vlr % centavos[i]
            i += 1

    valid_comecar = False
    while valid_comecar == False:
        comecar = input('Deseja calcular outros valores? S ou N ').lower()
        if comecar == 's' or comecar == 'n':
            valid_comecar = True
        else:
            print('Digite apenas S ou N')

print('Obrigado por utilizar os nossos serviços, volte sempre.')
