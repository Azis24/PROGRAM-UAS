from penilaian.penilaian import penilaian
from penilaian.jabatan import jabatan
from penilaian.kalkulator import kalkulator
from penilaian.bayar import bayar
def pilihan():
    print("==============PILIHAN PROGRAM============")
    print("\n\t========PILIHAN======\n\t1 PROGRAM NILAI\n\t2 PROGRAM GAJI\n\t3 PROGRAM PEMBAYARAN\n\t4 PROGRAM KALKULATOR\n\t5 AKHIR")

    pilih = input("\n\tSILAHKAN PILIH PROGRAMNYA :")
    if pilih == "1" :
        penilaian()
        lagi()
    elif pilih == "2" :
        jabatan()
        lagi()
    elif pilih == "3" :
        
        bayar()
        lagi()
    elif pilih == "4" :
        kalkulator()
        lagi()

    elif pilih == "5" :
        print("\n\t================TERIMAKASIH===========")
        lagi()
    
    else :
        print("\n\t================THANKS YOU===========")
        lagi()
        
def lagi() :
    tanya = input("\nKEMBALI LAGI KE PILIHAN PROGRAM (y/t)?")
    if tanya == "y":
        pilihan()
    elif tanya == "t":
       exit
    else:
        print("\n\tSALAH MASUKAN PROGRAM............!!!")
        exit
def login () :

   import getpass

   username = input("MASUKAN USERNAME ANDA : ")
   password = getpass.getpass()
   if   (username == 'AZIS MAULANA' and password == '12345') :
           print ('\======AKHIRNYA SUCCESFULL LOGIN======== ')
           print ('======================================= ')
           pilihan()
       
   else :
         print('\PASSWORD DAN USERNAME SALAH')
         exit
login()


        
