import random

def kolicina_stevil (izbira):
    seznam_stevil = []

    while True:
        if len(seznam_stevil) == izbira:
            break

        loto_stevila = random.randint (0,100)

        if loto_stevila not in seznam_stevil:
            seznam_stevil.append(loto_stevila)
    return seznam_stevil

def main ():
    print "Pozdravljen v generatorju stevil"
    while True:
        st_generirancev = raw_input("Vpisi zeljeno stevilo generiranih stevil: ")

        try:
            generiranci = int(st_generirancev)
            print "izbrali ste %s stevil" % generiranci
            print kolicina_stevil(generiranci)
        except ValueError:
            print "Prosim vnesi stevilo!"


        ponovno = raw_input("Zelis se generirati? (Da/Ne)")
        if ponovno.lower() == "ne":#mora bit isto! ce das .lower-ne more bit Ne!!
            print "Adijo"
            break


if __name__ == '__main__':
    main()

