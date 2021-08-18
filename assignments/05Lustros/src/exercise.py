def main():
    #escribe tu código abajo de esta línea
    nacimiento = float(input("Dame el año de nacimiento: "))
    actual = float(input("Dame el año actual: "))
    lustros = (actual - nacimiento)/5
    print(f'Los lustros que has vivido son: {lustros}')



if __name__ == '__main__':
    main()
