x = int(input("Silahkan input nomor anda >> "))
print(' '*(x -1),"*")
for y in range ((x-1),0,-1):
    print(' '*(y-1),"*")
print("**"*x)