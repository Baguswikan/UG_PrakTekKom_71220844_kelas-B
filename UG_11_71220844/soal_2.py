x = input("masukan kata: ")
palindrome = True
panjang_x = len(x)
for i in range(panjang_x//2):
    if (x[i] != x[panjang_x-i-1]):
        palindrome = False
        break
if palindrome:
    print("yes")
    print("jika dibalik",x)
else:
    print("no")
    print("jika dibalik: ",x)