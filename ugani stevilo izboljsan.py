import random

def main ():
    secret = random.randint (1, 30)

    loop_count = 0

    if secret < 15:
        print "vecje od 15"
    else:
        print "manjse od 15"

    while loop_count <5:
        guess = int(raw_input("Ugani stevilo od 0-30: "))

        if guess == secret:
            print "Uganil si! Skrita stevilka je {}:".format (secret)
            break
        else:
            print "Poskusi se enkrat! Skrita stevilka ni {}".format (guess)
            if guess < secret:
                print "Izberi visjo stevilko"
            else:
                print "Izberi manjso stevilo"
        loop_count += 1 #loop_count = loop_count + 1

if __name__ == '__main__':
    main()
