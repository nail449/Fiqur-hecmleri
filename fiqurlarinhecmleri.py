def nailhesab():
    print("hesablamaq istediyiniz fiquru yazin: \n"
    "meselen: kub, prizma, kure ")
    hesab = input("hesablamaq istediyiniz fiquru yazin:")

    if hesab == "kub":
        a = int(input("bir kenar uzunlugu yazin"))
        hecm = (a**3)
        return (hecm)
    elif hesab == "prizma":
        a = int(input("a kenar uzunlugunu yazin"))
        b = int(input("b kenar uzunlugunu yazin"))
        c = int(input("c kenar uzunlugunu yazin"))
        hecm = (a*b*c)
        return (hecm)
    elif hesab == "kure":
        r = int(input("r radiusunu yazin"))
        hecm = ((4/3)*3.14*(r**3))
        return (hecm)
    else:
        print("zehmet olmasa duzgun fiqur girin")


print (nailhesab())