class televisao:
    def __init__(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
            c=('__TV desligada.\n')
            print(c)
        else:
            self.ligada = True
            c = ('__TV ligada.\n')
            print(c)

class outras:
    def volume(seta,valor):
        if seta == 'aumentar':
            print('Aumentando o volume. ')
            volume=valor+1
            print('Volume: {}\n\n'.format(volume))
        else:
            print('Diminuindo o volume. ')
            volume=valor-1
            print('Volume: {}\n\n'.format(volume))
        return volume
    
    def canal(seta,numCanal):
        if seta == 'aumentar':
            while numCanal>=9:
                print('\n------------\n---OS CANAIS VÃO ATÉ 9.---')
                numCanal=8
            canal=numCanal+1
            print('Aumentando o canal. {}'.format(canal))
            print('\n\n')
        else:
            canal=numCanal-1
            print('Diminuindo o canal. {}'.format(canal))
            print('\n\n')
        return (canal)

    def op():
        print('\n---------------------------------------\n')
        print('Opções:\n'
                '1- Ligar ou desligar\n'
                '\n2- Aumentar volume'
                '\n3- Diminuir volume'
                '\n\n4- Aumentar canal'
                '\n5- Diminuir canal'
                '\n6- Escolher Canal')



                
                



    
