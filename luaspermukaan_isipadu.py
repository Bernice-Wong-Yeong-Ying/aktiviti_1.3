#Atur cara mengira jumlah luas permukaan dan isi padu silinder
#Isytihar pemalar
pi=3.142


#Input
jejari=float(input("Masukkan jejari:"))
tinggi=float(input("Masukkan tinggi:"))

#Proses
jumlahluaspermukaan=(2*pi*jejari*tinggi)+(2*pi*jejari*jejari)
isipadusilinder=pi*jejari*jejari*tinggi

#Output
print("Jumlah luas permukaan silider ialah",jumlahluaspermukaan,"dan isi padu silinder ialah isi padu silinder ialah",isipadusilinder)
