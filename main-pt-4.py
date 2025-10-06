import os
os.system('cls')

username = 'Adrian'
pw = '032'
# Login
print('Silahkan Login dengan username dan password.')
percobaan = 5
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
            print('Username atau password salah! Silahkan coba lagi.')
            print(f"Tersisa {percobaan}x percobaan")
        else:
            print('Anda salah memasukkan username atau password sebanyak 5x.')
    
print('Program dihentikan.')