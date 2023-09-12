import random

# Clase Carta
class Carta:
    def __init__(self, pinta, valor):
        self.pinta = pinta
        self.valor = valor

# Clase Baraja
class Baraja:
    def __init__(self):
        pintas = ['CORAZÓN', 'TRÉBOL', 'DIAMANTE', 'ESPADA']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cartas = [Carta(pinta, valor) for pinta in pintas for valor in valores]
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()

# Clase Mano
class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def calcular_valor(self):
        valor = 0
        ases = 0
        for carta in self.cartas:
            if carta.valor in ['K', 'Q', 'J']:
                valor += 10
            elif carta.valor == 'A':
                valor += 11
                ases += 1
            else:
                valor += int(carta.valor)

        while valor > 21 and ases > 0:
            valor -= 10
            ases -= 1

        return valor

# Clase Jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fichas = 100
        self.mano = Mano()

    def apostar(self, cantidad):
        if cantidad <= self.fichas:
            self.fichas -= cantidad
            return cantidad
        else:
            return 0

    def mostrar_mano(self):
        for carta in self.mano.cartas:
            print(f'Carta: {carta.valor} de {carta.pinta}')

# Clase Blackjack
class Blackjack:
    def __init__(self, nombre_jugador):
        self.jugador = Jugador(nombre_jugador)
        self.casa = Jugador("Casa")
        self.baraja = Baraja()

    def jugar(self):
        print(f"Bienvenido, {self.jugador.nombre}!")
        while self.jugador.fichas > 0:
            apuesta = int(input(f'Saldo actual: {self.jugador.fichas} fichas. Realiza tu apuesta: '))
            if apuesta <= 0:
                print('La apuesta debe ser mayor que cero.')
                continue

            self.iniciar_juego(apuesta)

    def iniciar_juego(self, apuesta):
        self.jugador.mano = Mano()
        self.casa.mano = Mano()

        for _ in range(2):
            self.jugador.mano.agregar_carta(self.baraja.repartir_carta())
            self.casa.mano.agregar_carta(self.baraja.repartir_carta())

        print(f'\nTus cartas:')
        self.jugador.mostrar_mano()

        while True:
            decision = input('¿Deseas plantarte  (P) o pedir una carta (C)? ').upper()
            if decision == 'P':
                break
            elif decision == 'C':
                carta = self.baraja.repartir_carta()
                self.jugador.mano.agregar_carta(carta)
                print(f'\nRecibiste una carta:')
                print(f'Carta: {carta.valor} de {carta.pinta}')
                print(f'Valor de tu mano: {self.jugador.mano.calcular_valor()}')

                if self.jugador.mano.calcular_valor() > 21:
                    print('Te has pasado de 21. Has perdido.')
                    self.jugador.fichas -= apuesta
                    return

        while self.casa.mano.calcular_valor() < 17:
            carta = self.baraja.repartir_carta()
            self.casa.mano.agregar_carta(carta)

        print('\nCartas de la Casa:')
        self.casa.mostrar_mano()

        valor_jugador = self.jugador.mano.calcular_valor()
        valor_casa = self.casa.mano.calcular_valor()

        if valor_jugador > 21:
            print('Has perdido.')
            self.jugador.fichas -= apuesta
        elif valor_casa > 21 or valor_jugador > valor_casa:
            print('¡Has ganado!')
            self.jugador.fichas += apuesta * 2
        elif valor_jugador == valor_casa:
            print('Empate. Recibes tu apuesta de vuelta.')
            self.jugador.fichas += apuesta

        print(f'Saldo actual: {self.jugador.fichas} fichas.')
        continuar = input('¿Deseas jugar otra mano (S/N)? ').upper()
        if continuar != 'S':
            print(f'Gracias por jugar, {self.jugador.nombre}!')
            exit()

# Ejecutar el juego
nombre_jugador = input('Por favor, ingresa tu nombre: ')
juego = Blackjack(nombre_jugador)
juego.jugar()













































































































