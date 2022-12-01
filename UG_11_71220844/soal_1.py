
def add(angka1,angka2):

    return angka1 + angka2

def subtract(angka1,angka2):
    return angka1 - angka2

def multiply(angka1,angka2):
    return angka1 * angka2

def divide(angka1,angka2):
    return angka1 / angka2

def hasil(pilihan,angka1,angka2):
    if pilihan == 1:
        # return add(angka1,angka2)
        print("hasil",angka1,"+",angka2,"=",add(angka1,angka2))
    elif pilihan == 2:
        # return subtract(angka1,angka2)
         print("hasil",angka1,"-",angka2,"=",subtract(angka1,angka2))
    elif pilihan == 3:
        # return multiply(angka1,angka2)
         print("hasil",angka1,"*",angka2,"=",multiply(angka1,angka2))
    else :
        # return divide(angka1,angka2)
         print("hasil",angka1,"/",angka2,"=",divide(angka1,angka2))
print("Select operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

pilihan =int(input("Masukkan pilihan : "))
angka1 = int(input("masukkan angka1 : "))
angka2 = int(input("Masukan angka 2 : "))
# print("hasil dari kalkulator adalah : ", hasil(pilihan,angka1,angka2))
print(hasil(pilihan,angka1,angka2))