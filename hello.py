import math
def rumus_abc (a, b, c):
    x_1 = -1*b + math.sqrt(pow(b,2) - 4*a*c )/2*a

    x_2 = -1*b - math.sqrt(pow(b,2) - 4*a*c )/2*a

    print ("Hasilnya adalah "+ str(x_1) + " dan " +  str(x_2) + " ")

rumus_abc(1,2,1)
rumus_abc(2,-5,-3) 

nama_depan = "Aldi"
nama_tengah = "Yanto"
nama_belakang = "Siswoyo"
nama_lengkap = nama_depan +" " + nama_tengah +" " + nama_belakang
print(nama_lengkap)

import hex
def rumus_a1 a2 :
    a1 = 6
    a2 = 12
    print(hex(a1*a2)