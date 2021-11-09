nama = input('Nama Lengkap: ')
dd = input('Tanggal lahir (DD): ')
mm = input('Nama Bulan: ')
yy = input('yyyy: ')
if 2021 - int(yy) < 17:
    print('Anda terlalu muda untuk menjadi anggota')
    
gaji = eval(input('Penghasilan per Bulan: '))
if gaji <= 5000000:
    level = 'Silver'
elif gaji <= 10000000:
    level = 'Gold'
else:
    level = 'Diamond'
    
email = input('Masukan email Anda: ')
S = '@'
adaKarakterSpesial1 = False
for email in S:
    if email in '@':
        adaKarakterSpesial1 = True
        
adaKarakterSpesial2 = False        
for email in S:
    if email in 'gmail':
        adaKarakterSpesial2 = True
        
adaKarakterSpesial3 = False
for email in S:
    if email in '.com':
        adaKarakterSpesial3 = True
        
isValidEmail = adaKarakterSpesial1 and adaKarakterSpesial2 and adaKarakterSpesial3
print(isValidEmail)

print('Nama: ', str(nama))
print('Email: ', str(email))
print('Level: ', str(level))


        
