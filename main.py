import threading
import cliente
import sala

op = None


def menu():
    print('---CINEMA---')
    print('Informe uma das opções a seguir: ')
    print('\n 1 - Reservar assento\n', '2 - Cancelar reserva\n', '0 - Encerrar\n')


while op != 0:
    menu()
    op = int(input())
