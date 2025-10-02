print ("Kalkulator serba bisa")

username = (input("masukkan username anda : "))
password = (input("masukkan password anda : "))

if username == "Dzaky" and password == "061":
    print(""" 
        1. Konversi Panjang 
        2. Konversi Massa   
        3. Konversi Suhu    
        4. Konversi Waktu   
        5. Konversi Mata uang""")

    opsi = int(input("pilih no konversi yang di inginkan : "))

#konversi panjang 
    if opsi == 1:
        print("\n<KONVERSI PANJANG>")
        
        print("""
        1. feet ke meter       
        2. kilometer ke meter  
        3. centimeter ke meter 
        """)

        feet = int(input("masukkan angka (feet) :"))
        cm = int(input("masukkan angka (cm) :"))
        km = int(input("masukkan angka (km) :"))
        m1 = feet * 0.3048
        m2 = cm / 100
        m3 = km * 1000
        print("\n<Hasil Konversi>\n")
        print(feet, "feet", "ke", m1, "meter")
        print(cm, "cm", "ke", m2, "meter")
        print(km, "km", "ke", m3, "meter")

            

#konversi massa
    elif opsi == 2:
        print("\n<Konversi Massa>\n")
        massa =[
            int(input("Masukkan angka (pound)    : ")),
            int(input("Masukkan angka (ton)      : ")),
            int(input("Masukkan angka (gram)     : ")),         
            int(input("Masukkan angka (mg)  : ")),        
            int(input("Masukkan angka (ons)      : "))         
        ]
        print("\n<Hasil Konversi>\n")
        pound    = massa[0] * 0.45
        ton      = massa[1] * 1000
        gram     = massa[2] / 1000
        mg       = massa[3] * 0.000001
        ons      = massa[4] / 0.1

        print(massa[0], "pound", "ke", pound, "kilogram")
        print(massa[1], "ton", "ke", ton, "kilogram")
        print(massa[2], "gram", "ke", gram, "kilogram")
        print(massa[3], "mg", "ke", mg, "kilogram")
        print(massa[4], "gram", "ke", ons, "kilogram")

#konversi suhu
    elif opsi == 3:
        print("\n<Konversi Suhu>\n")
        suhu = [
            int(input("Masukkan suhu (Celcius)    ")),
            int(input("Masukkan suhu (Fahrenheit) ")),
            int(input("Masukkan suhu (Reamur)     "))          
        ]

        print("\n<Hasil Konversi>\n")

        celcius    = suhu[0] + 273.15
        fahrenheit = (suhu[1] + 459.67) * 5/9
        reamur     = (suhu[2] / 0.8) + 273.15

        print(suhu[0], "Celcius", "ke", celcius, "Kelvin")
        print(suhu[0], "Fahrenheit", "ke", fahrenheit, "Kelvin")
        print(suhu[0], "Reamur", "ke", reamur, "Kelvin")

#konversi waktu
    elif opsi == 4:
        print("\n<Konversi Waktu>\n")
        waktu = [
            int(input("Masukkan waktu(menit) ")),
            int(input("Masukkan wakrtu(jam)   "))        
        ]

        print("\n<Hasil Konversi>\n")

        menit = waktu[0] * 60
        jam   = waktu[1] * 3600

        print(waktu[0], "Menit", "ke", menit, "Detik")
        print(waktu[1], "Jam", "ke", jam, "Detik")
    
#konversi mata uang
    elif opsi == 5:
        print("\n<Konversi Mata uang>\n")
        uang = [
            int(input("Masukkan uang(Rupiah) ")),
            int(input("Masukkan uang(Dolar Amerika)) ")),
            int(input("Masukkan uang(Euro) ")),
            int(input("Masukkan uang(Poundsterling) ")),
            int(input("Masukkan uang(Yen Jepang) ")),
            int(input("Masukkan uang(Dolar Amerika) "))      
        ]

        print("\n<Hasil Konversi>\n")

        USD = uang[0]/15000
        IDR = uang[1]*15000
        GBP = uang[2]*0.85
        EUR = uang[3]/0.85
        USDJ= uang[4]/150
        JPY = uang[5]*150

        print(uang[0], "Rp", "ke", USD, "USD")
        print(uang[1], "USD", "ke",IDR, "Rp")
        print(uang[2], "EUR", "ke", GBP, "GBP")
        print(uang[3], "GBP", "ke", EUR, "EUR")
        print(uang[4], "USD", "ke", JPY, "JPY")
        print(uang[5], "JPY", "ke", USD, "USD")

    else:
        print ("TIDAK ADA OPSI")

elif username == "Dzaky":
    print ("Username benar, password salah")
elif password == "061":
    print ("Password benar, username salah")
else:
    print("TIDAK BISA LOGIN")