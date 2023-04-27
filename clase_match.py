a = int(input("escribe 1 o 2: "))

match a:
    case 1:
        print("escribisté 1")
    case 2:
        print("escribiste 2")
    case other:
        print("es diferente")