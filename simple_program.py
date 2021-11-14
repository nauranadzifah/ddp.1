nama = input('1.  Nama Lengkap: ')
dd = input('2.  Tanggal lahir (DD): ')
mm = input('    Nama Bulan: ')
yy = input('    yyyy: ')
if 2021 - int(yy) < 17:
    print('Anda terlalu muda untuk menjadi anggota')
    
gaji = eval(input('3.  Penghasilan per Bulan: '))
if gaji <= 5000000:
    level = 'Silver'
elif gaji <= 10000000:
    level = 'Gold'
else:
    level = 'Diamond'
    
while True:
    N = input(str('4.  Masukan email Anda: '))
    if '@gmail' and '.com' in N:
        break
    else:
        print('Email anda tidak valid')
        
while True :
    pw = input(str("5.  Masukan Password Anda: "))
    Panjang = len(pw)

    karakter = False 
    for i in pw :
        if i in "!@#$" :
            karakter = True 

    Capslk = False 
    for i in pw :
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
            Capslk = True    

    hrfkecil = False 
    for i in pw :
        if i in "abcdefghijklmnopqrstuvwxyz" :
            hrfkecil = True 
            
    angka = False 
    for i in pw :
        if i in "1234567890" :
            angka = True 
    
    if Panjang >= 8 and karakter and Capslk and hrfkecil and angka:
        True 
        pw1 = input(str('    Konfirmasi Password: '))
        break
    else : 
        print("Password tidak valid. Ulangi.")
        
  
print('         ')
print('Pendaftaran Berhasil. Berikut Data Anda:')    
print('Nama: ', str(nama))
print('Email: ', str(N))
print('Level: ', str(level))


        
