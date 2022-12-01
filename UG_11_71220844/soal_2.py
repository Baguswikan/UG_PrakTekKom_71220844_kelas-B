x = input("masukan kata")
palindrome = True
panjang_y = len(x)
for i in range(panjang_y//2):
    if (x[i]) != x([panjang_y-i-1]):
        palindrome = False
        break
if palindrome:
    print("yes")
    print("jika dibalik",x)
else:
    print("no")
    print("jika dibalik: ",x)