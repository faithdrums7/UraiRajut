# # Use the function
# print(urai('Code'))
# print(urai('Python'))
# print(urai('Purwadhika'))

# Output:
# CCoCodCode -> ccocodcode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika


def urai(kata):                    #saya define suatu function bernama urai dengan parameter kata
    pecah = list(kata)             #digunakan function list untuk memecah argument kata menjadi suatu list ditampung pada variabel pecah
    kosong = ''                    #str kosong untuk menampung nilai join dari slicing yang dilakukan melalui loop
    final = ''                     #str kosong yang digunakan untuk menggabungkan string yang ada pada variabel kosong
    for i in range(len(pecah)):    #i menandakan index yang terdapat pada range panjang kata, jika kata kita adalah 'Code' maka lengthnya adalah 4
        temp = pecah[:i+1]         #variabel temp akan menampung value yang dikeluarkan tersebut namun bentuknya masih LIST
        kosong = ''.join(temp)     #variabel kosong akan menampung value temp dalam bentuk string. untuk membuat list menjadi string digunakan function join
        final += kosong            #setelah menjadi string kemudian saya pindahkan ke variabel final
    return final

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))