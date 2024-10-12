#Copyright: Mohammad Nasucha, Ph.D. (Please use this program but do not remove this recognition).

print("\033c")       #To close all
import numpy as np
import matplotlib.pyplot as plt
import time
#%matplotlib inline

###########################################################################
####### MEMBANDINGKAN METODE NUMERIK DASAR DAN METODE FALSE POSITION #######
###########################################################################
# Persamaan Polinomial Kubik: y = ax^3 + bx^2 + cx + d.
# Ingin diketahui titik potong kurva dengan sumbu x.
###########################################################################
# ALGORITMA KOMPUTASI UNTUK METODE NUMERIK UMUM (DASAR)
###########################################################################
# (1)  Masukkan dan simpan nilai a, b, c, d
# (2)  Tampilkan kurva persamaan.
#      Berdasarkan gambar kurva tersebut, perkirakan domain akar pertama
#      yang akan dicari. (Masukkan dan simpan nilai x_awal_1 dan x_akhir_1)
# (3)  Masukkan dan simpan nilai dx.
# (4)  Masukkan dan simpan nilai error margin (err_m),
# (5)  Tetapkan x= x_awal_1 dan x_akhir = x_akhir_1
# (6)  Tetapkan delta_x = dx.
# (6)  Tetapkan inisiasi nomor iterasi dengan: i = 0;
# (7)  Lakukan loop (iterasi) sepanjang |y| > err_m dan x < x_akhir
#      Hitung i = i + 1.
#      Hitung x = x + delta_x.
#      Hitung nilai y untuk nilai x ini, yaitu y = ax^3 + bx^2 + cx + d.
#      Cek apakah apakah |y| < err_m.
#      Jika false, kembali ke langkah (4)
#      Jika true, lanjutkan ke langkah berikutnya.
# (8) Cetak (“Akar 1 = x =“,  x) dan cetak (“y1 =“, y).
# (9) Ulangi langkah (5) s.d. (8) untuk pencarian akar kedua dan ketiga.

###########################################################################
# ALGORITMA KOMPUTASI UNTUK METODE FALSE POSITION
###########################################################################
# -----Semua langkah sama kecuali bahwa delta_x tidak sama dengan dx-------
# --(tidak konstan) melainkan dihitung berdasarkan rumus False Position. --
#-------------- delta_x = (y_x *(x_akhir-x))/ (y_x - y_x_akhir) -----------

###########################################################################
# PENERAPAN PERBANDINGAN DUA ALGORITMA
###########################################################################
#y = a*x**3 + b*x**2 + c*x + d
#Masukkan Nilai Variabel (Input), contoh:
a = 0.3
b = 1.3
c =  -7.5
d =  -22
dx    = 1e-4
err_m = 1e-3
x_awal_1 =  -7
x_akhir_1 = -5
x_awal_2 =  -3.0
x_akhir_2 = -2.0
x_awal_3 =   4.5
x_akhir_3 =  6.0

##### Mencari Akar Pertama dengan Metode Dasar #####
x = x_awal_1
x_akhir = x_akhir_1
delta_x = dx
y = a*x**3 + b*x**2 + c*x + d
i = 0
while(x < x_akhir and abs(y) > err_m):
    i = i + 1
    x = x + delta_x
    y = a*x**3 + b*x**2 + c*x + d
    print("Mencari akar pertama, iterasi ke-", i)
    print("x1 =", x)
    print("y1 =", y)

#Report
x1_u = x; y1_u = y; i1_u = i
print(" ")
print("Metode Dasar")
if(y1_u**2<err_m**2):
    print("Pencarian akar pertama dengan Metode Dasar berhasil.")
else:
    print("Pencarian akar pertama dengan Metode Dasar gagal.")
    print("Silahkan perkecil dx, perbesar error margin, atau sesuaikan x_awal dan x_akhir.")
print("x1 =", x1_u, ", y1 =", y1_u, ", #Iterasi =", i1_u)
print(" ")
time.sleep(5)

##### Mencari Akar Pertama dengan Metode False Position #####
x = x_awal_1
x_akhir = x_akhir_1
y_x = a*x**3 + b*x**2 + c*x + d
y_x_akhir = a*x_akhir**3 + b*x_akhir**2 + c*x_akhir + d
i = 0
while(x < x_akhir and y_x**2 > err_m**2):
    i = i + 1
    y_x = a * x ** 3 + b * x ** 2 + c * x + d
    delta_x = (y_x *(x_akhir-x))/ (y_x - y_x_akhir)
    x = x + delta_x
    print("Mencari akar pertama, iterasi ke-", i)
    print("x1 =", x)
    print("y1 =", y_x)

#Report
x1_f = x; y1_f = y_x; i1_f = i
print(" ")
print("Metode False Position")
if(y1_f**2<err_m**2):
    print("Pencarian akar pertama dengan metode False Position berhasil.")
else:
    print("Pencarian akar pertama dengan metode False Position gagal.")
    print("Silahkan perbesar error margin, atau sesuaikan x_awal dan x_akhir.")
print("x1 =", x1_f, ", y1 =", y1_f, ", #Iterasi =", i1_f)
print(" ")
time.sleep(5)


##### Mencari Akar Kedua dengan Metode Dasar #####
x = x_awal_2
x_akhir = x_akhir_2
delta_x = dx
y = a*x**3 + b*x**2 + c*x + d
i = 0
while(x < x_akhir and y**2 > err_m**2):
    i = i + 1
    x = x + delta_x
    y = a*x**3 + b*x**2 + c*x + d
    print("Mencari akar kedua, iterasi ke-", i)
    print("x2 =", x)
    print("y2 =", y)

#Report
x2_u = x; y2_u = y; i2_u = i
print(" ")
print("Metode Dasar")
if(y2_u**2<err_m**2):
    print("Pencarian akar kedua dengan Metode Dasar berhasil.")
else:
    print("Pencarian akar kedua dengan Metode Dasar gagal.")
    print("Silahkan perkecil dx, perbesar error margin, atau sesuaikan x_awal dan x_akhir.")
print("x2 =", x2_u, ", y2 =", y2_u, ", #Iterasi =", i2_u)
print(" ")
time.sleep(5)

##### Mencari Akar Kedua dengan Metode False Position #####
x = x_awal_2
x_akhir = x_akhir_2
y_x = a*x**3 + b*x**2 + c*x + d
y_x_akhir = a*x_akhir**3 + b*x_akhir**2 + c*x_akhir + d
i = 0
while(x < x_akhir and y_x**2 > err_m**2):
    i = i + 1
    y_x = a * x ** 3 + b * x ** 2 + c * x + d
    delta_x = (y_x *(x_akhir-x))/ (y_x - y_x_akhir)
    x = x + delta_x
    print("x2 =", x2_u, ", y2 =", y2_u, ", #Iterasi =", i2_u)

#Report
x2_f = x; y2_f = y_x; i2_f = i
print(" ")
print("Metode False Position")
if(y2_f**2<err_m**2):
    print("Pencarian akar kedua dengan metode False Position berhasil.")
else:
    print("Pencarian akar kedua dengan metode False Position gagal.")
    print("Metode ini seharusnya konvergen. Silahkan periksa coding.")
print("x2 =", x2_f, ", y2 =", y2_f, ", #Iterasi =", i2_f)
print(" ")
time.sleep(5)


##### Mencari Akar Ketiga dengan Metode Dasar #####
x = x_awal_3
x_akhir = x_akhir_3
delta_x = dx
y = a*x**3 + b*x**2 + c*x + d
i = 0
while(x < x_akhir and y**2 > err_m**2):
    i = i + 1
    x = x + delta_x
    y = a*x**3 + b*x**2 + c*x + d
    print("Mencari akar ketiga, iterasi ke-", i)
    print("x3 =", x)
    print("y3 =", y)

#Report
x3_u = x; y3_u = y; i3_u = i
print(" ")
print("Metode Dasar")
if(y3_u**2<err_m**2):
    print("Pencarian akar ketiga dengan Metode Dasar berhasil.")
else:
    print("Pencarian akar ketiga dengan Metode Dasar gagal.")
    print("Silahkan perkecil dx, perbesar error margin, atau sesuaikan x_awal dan x_akhir.")
print("x3 =", x3_u, ", y3 =", y3_u, ", #Iterasi =", i3_u)
print(" ")
time.sleep(5)

##### Mencari Akar Ketiga dengan Metode False Position #####
x = x_awal_3
x_akhir = x_akhir_3
y_x = a*x**3 + b*x**2 + c*x + d
y_x_akhir = a*x_akhir**3 + b*x_akhir**2 + c*x_akhir + d
i = 0
while(x < x_akhir and y_x**2 > err_m**2):
    i = i + 1
    y_x = a * x ** 3 + b * x ** 2 + c * x + d
    delta_x = (y_x *(x_akhir-x))/ (y_x - y_x_akhir)
    x = x + delta_x
    print("Mencari akar ketiga, iterasi ke-", i)
    print("x3 =", x)
    print("y3 =", y_x)

#Report
x3_f = x; y3_f = y_x; i3_f = i
print(" ")
print("Metode False Position")
if(y3_f**2<err_m**2):
    print("Pencarian akar ketiga dengan metode False Position berhasil.")
else:
    print("Pencarian akar ketiga dengan metode False Position gagal.")
    print("Metode ini seharusnya konvergen. Silahkan periksa coding .")
print("x3 =", x3_f, ", y3 =", y3_f, ", #Iterasi =", i3_f)
print(" ")
time.sleep(5)


print("----------------------------------HASIL AKHIR-------------------------------------")
print("VARIABEL(INPUT)")
print("a =", a, ", b=", b, ", c=", c, ", d =", d)
print("dx =", dx, ", error margin =", err_m)
print("x_awal_1 =", x_awal_1, ", x_akhir_1 =", x_akhir_1)
print("x_awal_2 =", x_awal_2, ", x_akhir_2 =", x_akhir_2)
print("x_awal_3 =", x_awal_3, ", x_akhir_3 =", x_akhir_3)
print(" ")

#############################################################################################
print("Metode Dasar")

if(y1_u**2<err_m**2):
    print("Pencarian akar pertama dengan Metode Dasar berhasil.")
else:
    print("Pencarian akar pertama dengan Metode Dasar gagal.")
    print("Silahkan perkecil dx, perbesar error margin, atau sesuaikan x_awal dan x_akhir.")
print("x1 =", x1_u, ", y1 =", y1_u, ", #iterasi =", i1_u)

if(y2_u**2<err_m**2):
    print("Pencarian akar kedua dengan Metode Dasar berhasil.")
else:
    print("Pencarian akar kedua dengan Metode Dasar gagal.")
    print("Silahkan perkecil dx, perbesar error margin, atau sesuaikan x_awal dan x_akhir.")
print("x2 =", x2_u, ", y2 =", y2_u, ", #iterasi =", i2_u)

if(y3_u**2<err_m**2):
    print("Pencarian akar ketiga dengan Metode Dasar berhasil.")
else:
    print("Pencarian akar ketiga dengan Metode Dasar gagal.")
    print("Silahkan perkecil dx, perbesar error margin, atau sesuaikan x_awal dan x_akhir.")
print("x3 =", x3_u, ", y3 =", y3_u, ", #iterasi =", i3_u)

print("Total Iterasi = ", i1_u + i2_u + i3_u)

print(" ")


#############################################################################################
print("Metode False Position")

if(y1_f**2<err_m**2):
    print("Pencarian akar pertama dengan metode False Position berhasil.")
else:
    print("Pencarian akar pertama dengan metode False Position gagal.")
    print("Metode ini seharusnya konvergen. Silahkan periksa coding .")
print("x1 =", x1_f, ", y1 =", y1_f, ", #iterasi =", i1_f)
print(" ")

if(y2_f**2<err_m**2):
    print("Pencarian akar kedua dengan metode False Position berhasil.")
else:
    print("Pencarian akar kedua dengan metode False Position gagal.")
    print("Metode ini seharusnya konvergen. Silahkan periksa coding .")
print("x2 =", x2_f, ", y2 =", y2_f, ", #iterasi =", i2_f)
print(" ")

if(y3_f**2<err_m**2):
    print("Pencarian akar ketiga dengan metode False Position berhasil.")
else:
    print("Pencarian akar ketiga dengan metode False Position gagal.")
    print("Metode ini seharusnya konvergen. Silahkan periksa coding .")
print("x3 =", x3_f, ", y3 =", y3_f, ", #iterasi =", i3_f)

print("Total Iterasi = ", i1_f + i2_f + i3_f)

print(" ")

# ---------------------------Visualisasikan Kurva--------------------------
x = np.linspace(-12,10,10000)
plt.figure(figsize=(6,6.5))
sumbu_x   = x -x -0
y         = a*x**3  + b*x**2 + c*x + d
plt.plot(x,  sumbu_x,              '-k')
plt.plot(x,  (0.01-x**2)**0.5,     '-k')
plt.plot(x,  -((0.01-x**2)**0.5),  '-k')
plt.plot(x,  y,                    '-g', label='y')
plt.legend(loc='upper left')
plt.grid()
plt.show()
