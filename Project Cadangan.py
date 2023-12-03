def simulasi_elo_chess():
    x = int(input("Masukkan ELO yang anda inginkan berapa = "))
    y = x // 7
    print(f"Anda perlu memenangkan sekitar {y} match secara beruntun untuk dapat meraih ELO yang anda inginkan")
    pilihan = input("Apakah anda ingin mengetahui kasus yang lebih realistis lagi ? ketik Iya jika anda mau, jawab = ").lower()
    while pilihan == "iya":
        pilihan_2 = int(input("Dalam skala 1-5 seberapa hebat anda dalam bermain catur??? jawaban kami akan mengikuti dengan seberapa hebatnya anda dalam bermain :), jawab = "))
        if pilihan_2 == 1:
            z = y // pilihan_2
            r = z * (pilihan_2 + 1)
            print(f"Jika berfikir lebih realistis anda perlu memenangkan sekitar {r} match dan akan mengalami kekalahan sekitar {z}")
            break
        elif pilihan_2 == 2:
            z = y // pilihan_2
            r = z * (pilihan_2 + 1)
            print(f"Jika berfikir lebih realistis anda perlu memenangkan sekitar {r} match dan akan mengalami kekalahan sekitar {z}")
            break       
        elif pilihan_2 == 3:
            z = y // pilihan_2
            r = z * (pilihan_2 + 1)
            print(f"Jika berfikir lebih realistis anda perlu memenangkan sekitar {r} match dan akan mengalami kekalahan sekitar {z}")
            break
        elif pilihan_2 == 4:
            z = y // pilihan_2
            r = z * (pilihan_2 + 1)
            print(f"Jika berfikir lebih realistis anda perlu memenangkan sekitar {r} match dan akan mengalami kekalahan sekitar {z}")
            break
        elif pilihan_2 == 5:
            z = y // pilihan_2
            r = z * (pilihan_2 + 1)
            print(f"Jika berfikir lebih realistis anda perlu memenangkan sekitar {r} match dan akan mengalami kekalahan sekitar {z}")
            break
        else:
            print("Hmm sepertinya anda salah memasukkan input yang sesuai")
    while not pilihan == "iya":
        print("Terima kasih telah menggunakan jasa kami")
        break
simulasi_elo_chess()        
