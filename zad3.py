
lista = []
suma = 0

while True:
    try:
        br = input("Unesite broj u listu, napišite Done za prestanak:\n")
        if(br == "Done"):
            break
        else:
            lista.append(int(br))
            suma += int(br)
    except:
        print("Došlo je do pogrešnog unosa")

print("Uneseno je:", len(lista), "brojeva")
print("Srednja vrijednost liste je:", (suma/len(lista)))
print("Minimalna vrijednost liste je:", min(lista))
print("Maksimalna vrijednost liste je:", max(lista))

thislist = lista
thislist.sort()
print(thislist)
