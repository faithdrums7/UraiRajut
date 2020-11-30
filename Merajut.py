# # Use the function
# print(rajut('CCoCodCode'))
# print(rajut('PPyPytPythPythoPython'))
# print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# # Output:
# Code
# Python
# Purwadhika

def rajut(terurai):                                 #Saya mendefine suatu function dengan nama rajut dan parameternya adalah terurai
    lst_kosong = []                                 #Dibuat list kosong untuk menampung hasil final yang masih dalam bentuk list        
    final = ''                                      #Str kosong untuk menampung hasil final dalam bentuk string               
    lst_kosong.append(terurai[0])                   #Saya menambahkan value index ke 0 dari terurai kedalam lst_kosong karena sudah pasti index[0] dari terurai termasuk dalam final         
    for i in range (len(terurai)):                  #i menampung semua element / huruf dari parameter terurai
        if terurai[i] not in lst_kosong:            #Masuk if condition yang mengecek apakah i terdapat dalam lst_kosong?
            lst_kosong.append(terurai[i])           #Jika ga ada maka huruf tersebut akan masuk kedalam lst_kosong
    if lst_kosong[-1] != terurai[-1]:               # Kemudian masuk ke dalam if condition jika huruf terakhir pada lst_kosong tidak sama dengan huruf terakhir pada terurai
        lst_kosong.append(terurai[-1])              # jika tidak sama maka lst kosong akan ditambahkan huruf terakhir yang ada list terurai
    final = final.join(lst_kosong)                  #function join digunakan untuk menggabung semua element yang terdapat pada lst_kosong
    return final
            
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))