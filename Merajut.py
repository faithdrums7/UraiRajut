# # Use the function
# print(rajut('CCoCodCode'))
# print(rajut('PPyPytPythPythoPython'))
# print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# # Output:
# Code
# Python
# Purwadhika

def rajut(terurai):                     #Saya mendefine suatu function dengan nama rajut dan parameternya adalah terurai
    lst_kosong = []                     #Dimbuat list kosong untuk menampung hasil final yang masih dalam bentuk list
    pecah = list(terurai)               #Saya membuat parameter menjadi list
    final = ''                          #Str kosong untuk menampung hasil final dalam bentuk string               
    lst_kosong.append(pecah[0])         #Saya menambahkan value index ke 0 dari listterurai kedalam lst_kosong karena sudah pasti index[0] termasuk dalam final         
    for i in terurai:                   #i menampung semua element / huruf dari parameter terurai
        if i not in lst_kosong:         #Masuk if condition yang mengecek apakah i terdapat dalam lst_kosong? 
            lst_kosong.append(i)        #Jika ga ada maka huruf tersebut akan masuk kedalam lst_kosong
    final = final.join(lst_kosong)      #function join digunakan untuk menggabung semua element yang terdapat pada lst_kosong
    return final
            
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))