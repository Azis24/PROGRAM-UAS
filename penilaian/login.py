print('\n==================================================')
print('\tSELAMAT DATANG DI PROGRAM INI')
print('\n==================================================')

def login () :
   print(' \SILAHKAN MASUK TERLEBIH DAHULU')
   print('===============================================')
   username = input("/n/tMASUKAN USERNAME ANDA : ")
   password = getpass.petpass("MASUKAN PASSWORD ANDA : ***** ")
   if   (username == 'AZIS MAULANA' and Passsword == '12345') :
           print ('======================================= ')
           print ('\======AKHIRNYA SUCCESFULL LOGIN======== ')
           print ('======================================= ')
           menu()
           exit
       
    else :
        
           print('\PASSWORD DAN USERNAME SALAH')

           login()
           exit

