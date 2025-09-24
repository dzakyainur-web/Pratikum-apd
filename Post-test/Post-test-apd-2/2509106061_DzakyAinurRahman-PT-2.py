list = (27, 33, 46, 55, 67, 92)
print("list data Celcius =", list[0:])
print("list data yang dikonversi")
suhuf1 = (list[0] * 9/5) + 32
suhuf2 = (list[1] * 9/5) + 32
suhuk3 = list[-4] + 273.15
suhuk4 = list[-3] + 273.15
suhur5 = list[-2] * 4/5
suhur6 = list[-1] * 4/5
jumlah = suhuf1 + suhuf2 + suhuk3 + suhuk4 + suhur5 + suhur6
rata2  = jumlah/6
NIM    = 61
Boolean= NIM < rata2
print("suhu 1 =", suhuf1, "Farenheit")
print("suhu 2 =", suhuf2, "Farenheit")
print("suhu 3 =", suhuk3, "Kelvin")
print("suhu 4 =", suhuk4, "Kelvin")
print("suhu 5 =", suhur5, "Reamur")
print("suhu 6 =", suhur6, "Reamur")

print("Jumlah =", jumlah)
print("Banyak data = 6")
print("Rata - rata =", rata2)

print("NIM =", NIM)
print("Boolean =", Boolean)

