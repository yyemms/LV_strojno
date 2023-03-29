radni_sati = input("Unesite broj radnih sati: ")
zarada = input("Unesite placu po satu: ")



def total_euro(x, y):

    return x * y


print("Radnik je zaradio", total_euro(int(radni_sati), int(zarada)), "eura")
