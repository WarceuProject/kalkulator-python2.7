#Saya membuat program kalkulator sederhana dengan python 2.7
import os,sys
def logo():
    os.system('clear')                                                          print """ Ini adalah program kalkulator sedernaha
    ______________________________________________
    """
def menu():
    print ""
    print "[menu]:"
    print "1.pejumlahan"
    print "2.pengurangan"
    #dua aja cukup untuk pemula :v seperyi saya
    print "0.keluar"
##===//program nya
def jumlah():
    logo()
    print "ini adalah program pejumlahan"
    print ""
    a = input("Angka pertama:")
    b = input("Angka kedua:")
    #kita buat fungsi nya
    hasil = ( a + b )
    print "Jumlah nya adalah:",hasil,

def kurangan():
    logo()
    print "ini adalah program pengurangan"
    x = input("Angka pertama:")
    y = input("Angka ke dua:")
    jadi = ( x - y )
    print "Hasil nya adalah:",jadi,

logo()
menu()
pil = input("pilih:")
if pil == 1:
    jumlah()
    #kelupaan :v
elif pil == 2:
    kurangan()
elif pil == 0:
    print "keluar"
    sys.exit()
else:
    print "wrong input !"