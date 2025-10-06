import os
# Clear Screen
os.system('cls')

print('===Selamat datang dalam program mengidentifikasi Segitiga dan hasil Luasnya===')
print('')
# Sign up
print('Silahkan Sign Up terlebih dahulu dengan membuat username dan password')
username = input("Masukkan username [nama panggilan]: ")
pw = (input("Masukkan password [3 digit NIM terakhir]: "))

print('')
print('Akun berhasil dibuat!')
print('')
# Login
print('Silahkan Login dengan username dan password anda')
percobaan = 5
pengurangan_percobaan = 1
while percobaan > 0:
    print('')
    login_username = input("Masukkan username: ")
    login_pw = (input("Masukkan password: "))
    print('')
    if (login_username == username) and (login_pw == pw):
        print('Login berhasil!')
        print('')
        #Identifikasi Segitiga
        coba_lagi = 'y'
        while coba_lagi == 'y':
            print("=== Mengidentifikasi Segitiga dan luasnya ===")
            print(" ")
            sisi_a = int(input("Masukkan Sisi A: "))
            sisi_b = int(input("Masukkan Sisi B: "))
            sisi_c = int(input("Masukkan Sisi C: "))

            print(" ")
            # MENGHITUNG LUAS DENGAN RUMUS HERON
            setengah_luas = ((sisi_a + sisi_b) + sisi_c) / 2
            luas = (setengah_luas * (setengah_luas - sisi_a) * (setengah_luas - sisi_b) * (setengah_luas - sisi_c)) ** 0.5

            if (sisi_a + sisi_b > sisi_c) and (sisi_b + sisi_c > sisi_a) and (sisi_c + sisi_a > sisi_b) :
                if sisi_a == sisi_b == sisi_c:
                    print("Segitiga Sama Sisi")
                elif (sisi_a == sisi_b) or (sisi_a == sisi_c) or (sisi_b == sisi_c):
                    print("Segitiga Sama Kaki")
                elif sisi_a != sisi_b != sisi_c:
                    print("Segitiga Sembarang")
                print(f"Hasil luasnya adalah: {luas}")
            else:
                print("Bukan Segitiga.")
            print('')
            coba_lagi = input('Coba lagi? [y/n]: ')
            print('')
        break
    else:
        percobaan -= 1
        if percobaan >= 1:
            print('Username atau password yang anda masukkan salah. Silahkan coba lagi.')
            print(f"Tersisa {percobaan}x percobaan")
        else:
            print('Username atau password yang anda masukkan salah.')
    
print('Program dihentikan.')