import controle

televisao = controle.televisao()
res = 'x'
numVolume=10
numCanal=5

c = ('__TV desligada.\n')
x = ('__TV desligada.\n')

def tela(numVolume,numCanal):
    numCanal=str(numCanal)
    car = (numCanal+' ')
    linhaCompleta = car*int(numVolume)

    meio =numVolume-2
    linhaMeio = car+'  '*meio+car

    print(linhaCompleta)
    cont=0
    while cont<meio:
        print(linhaMeio)
        cont+=1
    print(linhaCompleta)
    numCanal=int(numCanal)
        

controle.outras.op()

while res != '0':
    print('\n---------------------------------------\n')
    res = input('Digite a opção desejada (7- ver opções):  ')
    for x in range (0,20):
            print('\n')
    

    if res == '1':
        televisao.power()
        print('')

    elif res == '2':
        volume = controle.outras.volume('aumentar',numVolume)
        numVolume=volume
        tela(numVolume,numCanal)

    elif res =='3':
        if numVolume>4:
            volume = controle.outras.volume('diminuir',numVolume)
            numVolume=volume
            tela(numVolume,numCanal)
        else:
            print('Não é possível diminuir mais o volume')
            
    elif res == '4':
        canal = controle.outras.canal('aumentar', numCanal)
        numCanal=canal
        tela(numVolume,numCanal)
        
    elif res == '5':
        canal = controle.outras.canal('Diminuit', numCanal)
        numCanal=canal
        tela(numVolume,numCanal)
    
    elif res == '6':
        canal = int(input('Digite o canal desejado:'))
        while canal>=10:
            print('Os canais vão até 9.')
            canal = int(input('Digite o canal desejado:'))
        numCanal = canal
        tela(numVolume,numCanal)

    elif res == '7':
        controle.outras.op()

    else:
        print('Opção incorreta, digite novamente! ')
