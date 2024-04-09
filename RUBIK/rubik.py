class CuboRubik:
    def __init__(self):
        self.cara = {
            'U': [['n', 'n', 'n'], ['n', 'n', 'n'], ['n', 'n', 'n']],
            'D': [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']],
            'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
            'B': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
            'L': [['v', 'v', 'v'], ['v', 'v', 'v'], ['v', 'v', 'v']],
            'R': [['z', 'z', 'z'], ['z', 'z', 'z'], ['z', 'z', 'z']]
        }

    def rotar_cara(self, cara, direccion):
        if direccion == 'horario':
            self.cara[cara] = [list(fila)
                               for fila in zip(*self.cara[cara][::-1])]
        else:
            self.cara[cara] = [list(fila)
                               for fila in zip(*self.cara[cara])][::-1]

    def rotar_U(self, direccion):
        self.rotar_cara('U', direccion)
        if direccion == 'horario':
            temp = self.cara['F'][0][:]
            self.cara['F'][0] = self.cara['L'][0]
            self.cara['L'][0] = self.cara['B'][0][::-1]
            self.cara['B'][0] = self.cara['R'][0]
            self.cara['R'][0] = temp
        else:
            temp = self.cara['R'][0][:]
            self.cara['R'][0] = self.cara['B'][0][::-1]
            self.cara['B'][0] = self.cara['L'][0]
            self.cara['L'][0] = self.cara['F'][0]
            self.cara['F'][0] = temp

    def rotar_D(self, direccion):
        self.rotar_cara('D', direccion)
        if direccion == 'horario':
            temp = self.cara['F'][2][:]
            self.cara['F'][2] = self.cara['R'][2]
            self.cara['R'][2] = self.cara['B'][2][::-1]
            self.cara['B'][2] = self.cara['L'][2]
            self.cara['L'][2] = temp
        else:
            temp = self.cara['L'][2][:]
            self.cara['L'][2] = self.cara['B'][2][::-1]
            self.cara['B'][2] = self.cara['R'][2]
            self.cara['R'][2] = self.cara['F'][2]
            self.cara['F'][2] = temp

    def rotar_F(self, direccion):
        self.rotar_cara('F', direccion)
        if direccion == 'horario':
            pass
        else:
            fila_superior = [self.cara['U'][2][0], self.cara['U']
                             [2][1], self.cara['U'][2][2]]
            self.cara['U'][2][0], self.cara['U'][2][1], self.cara['U'][2][
                2] = self.cara['R'][0][0], self.cara['R'][1][0], self.cara['R'][2][0]
            self.cara['R'][0][0], self.cara['R'][1][0], self.cara['R'][2][
                0] = self.cara['D'][0][0], self.cara['D'][0][1], self.cara['D'][0][2]
            self.cara['D'][0][0], self.cara['D'][0][1], self.cara['D'][0][
                2] = self.cara['L'][0][2], self.cara['L'][1][2], self.cara['L'][2][2]
            self.cara['L'][0][2], self.cara['L'][1][2], self.cara['L'][2][2] = fila_superior

    def rotar_B(self, direccion):
        self.rotar_cara('B', direccion)
        if direccion == 'horario':
            temp = self.cara['U'][0][:]
            self.cara['U'][0] = self.cara['L'][0][::-1]
            self.cara['L'][0] = self.cara['D'][2]
            self.cara['D'][2] = self.cara['R'][0][::-1]
            self.cara['R'][0] = temp
        else:
            temp = self.cara['R'][0][:]
            self.cara['R'][0] = self.cara['D'][2][::-1]
            self.cara['D'][2] = self.cara['L'][0]
            self.cara['L'][0] = self.cara['U'][0]
            self.cara['U'][0] = temp

    def rotar_L(self, direccion):
        self.rotar_cara('L', direccion)
        if direccion == 'horario':
            temp = self.cara['U'][0][:]
            self.cara['U'][0] = self.cara['F'][0]
            self.cara['F'][0] = self.cara['D'][0][::-1]
            self.cara['D'][0] = self.cara['B'][0]
            self.cara['B'][0] = temp
        else:
            temp = self.cara['B'][0][:]
            self.cara['B'][0] = self.cara['D'][0]
            self.cara['D'][0] = self.cara['F'][0][::-1]
            self.cara['F'][0] = self.cara['U'][0]
            self.cara['U'][0] = temp

    def rotar_R(self, direccion):
        self.rotar_cara('R', direccion)
        if direccion == 'horario':
            pass  # Aquí va tu código para la rotación en sentido horario
        else:
            columna_superior = [self.cara['U'][0][2], self.cara['U']
                                [1][2], self.cara['U'][2][2]]
            self.cara['U'][0][2], self.cara['U'][1][2], self.cara['U'][2][
                2] = self.cara['B'][2][0], self.cara['B'][1][0], self.cara['B'][0][0]
            self.cara['B'][0][0], self.cara['B'][1][0], self.cara['B'][2][
                0] = self.cara['D'][0][2], self.cara['D'][1][2], self.cara['D'][2][2]
            self.cara['D'][0][2], self.cara['D'][1][2], self.cara['D'][2][
                2] = self.cara['F'][0][2], self.cara['F'][1][2], self.cara['F'][2][2]
            self.cara['F'][0][2], self.cara['F'][1][2], self.cara['F'][2][2] = columna_superior

    def imprimir_cubo(self):
        for fila in range(3):
            for col in range(3):
                print(self.cara['U'][fila][col], end="")
            print()
        print()
        for fila in range(3):
            for cara in ['L', 'F', 'R', 'B']:
                for col in range(3):
                    print(self.cara[cara][fila][col], end="")
                print(" ", end="")
            print()
        print()
        for fila in range(3):
            for col in range(3):
                print(self.cara['D'][fila][col], end="")
            print()


def imprimir_menu():
    print("Opciones:")
    print("1. Rotar blanco (U) sentido horario")
    print("2. Rotar blanco (U) sentido antihorario")
    print("3. Rotar amarillo (D) sentido horario")
    print("4. Rotar amarillo (D) sentido antihorario")
    print("5. Rotar rojo (F) sentido horario")
    print("6. Rotar rojo (F) sentido antihorario")
    print("7. Rotar azul (B) sentido horario")
    print("8. Rotar azul (B) sentido antihorario")
    print("9. Rotar verde (L) sentido horario")
    print("10. Rotar verde (L) sentido antihorario")
    print("11. Rotar naranja (R) sentido horario")
    print("12. Rotar naranja (R) sentido antihorario")
    print("13. Salir")


cubo_rubik = CuboRubik()

while True:
    cubo_rubik.imprimir_cubo()
    imprimir_menu()
    eleccion = input("Ingrese el número de la opción que desea ejecutar: ")
    if eleccion == '1':
        cubo_rubik.rotar_U('horario')
    elif eleccion == '2':
        cubo_rubik.rotar_U('antihorario')
    elif eleccion == '3':
        cubo_rubik.rotar_D('horario')
    elif eleccion == '4':
        cubo_rubik.rotar_D('antihorario')
    elif eleccion == '5':
        cubo_rubik.rotar_F('horario')
    elif eleccion == '6':
        cubo_rubik.rotar_F('antihorario')
    elif eleccion == '7':
        cubo_rubik.rotar_B('horario')
    elif eleccion == '8':
        cubo_rubik.rotar_B('antihorario')
    elif eleccion == '9':
        cubo_rubik.rotar_L('horario')
    elif eleccion == '10':
        cubo_rubik.rotar_L('antihorario')
    elif eleccion == '11':
        cubo_rubik.rotar_R('horario')
    elif eleccion == '12':
        cubo_rubik.rotar_R('antihorario')
    elif eleccion == '13':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor ingrese un número válido.")
