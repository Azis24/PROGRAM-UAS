
def bayar () :
        
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\t")
        print("\n~~~~~~~~SELAMAT DATANG DI PROGRAM PEMBAYARAN MAHASISWA~~~~~~~~~\t")
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\t")
        print("1. PROGRAM PEMBAYARAN UTS")
        print("2. PROGRAM PEMBAYARAN UAS")
        sasa = input ('Mau bayaran y atau t ?')
        if sasa == 'y' :
                print('\n============================================\n\t')
                print('---------------SILAHKAN INPUT LAGI-----------------')
                print('\n============================================\n\t')
                pembayaran()
        elif sasa == 't':
                    print (' Eror ')
                    exit
        elif sasa == '' :
                    exit
        else :
                    print('PILIHAN ANDA TIDAK ADA KANG/MBA')
                    exit

def pembayaran() :       
    pilihan = input("\nMASUKAN PILIHAN BAYARAN 1. UTS / 2. UAS : ")
    if   pilihan == '1' :
        uts() 
    elif pilihan == '2' :
        uas()
    else :
        akhir()
   
        
        
def uts():
        from texttable import Texttable
        table = Texttable()
        jawab = "y"

        no = 0
        nama =[]
        nim = []
        kelas = []
        jum_matkul_uts_bayar = []
        bulan_bayar = []
        seminar_bayar = []
        kas_bayar = []
        print('\n********************************\t')
        print("\n**********BAYARAN UTS*********\t")
        print('\n********************************\t')
        
        while(jawab == "y") :
            nama.append(input(" Nama  : "))
            nim.append(input(" NIM    : "))
            kelas.append(input(" Kelas : "))
            print('\n===================================================================\n\t')
            print('\n===================================================================\n\t')
            jum_matkul_uts_bayar.append(input("\nMATA KULIAH YANG DI BAYAR BUAT UTS : "))
            bulan_bayar.append(input("JUMLAH BULAN BIAYA YANG DIBAYAR : "))
            pil = input("MAU BAYAR SEMINAR SAYANG [Y/T]  ? ")
            if pil == 'y' :
                    bayar_seminar = 100000
            else :
                    bayar_seminar = 0

            pil = input("MAU BAYAR KAS SAYANG [Y/T]  ? ")
            if pil == 'y' :
                    bayar_kas = 200000
            else :
                    bayar_kas = 0
                

                    
            jawab = input (" INGIN BAYAR LAGI ATAU TIDAK SAYANG (Y/T) : ")
            no +=1
            
        
        for i in range (no):
            bayar_uts = int(jum_matkul_uts_bayar[i])*90000
            bayar_spp = int(bulan_bayar[i])*500000
            admin = int(5000)
            akhir = bayar_uts + bayar_spp + bayar_seminar+ bayar_kas + admin
            table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
            table.set_cols_align(["i", "c", "c", "c", "c","c","c","c","c","c"])
            table.set_cols_width([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
            table.add_rows([['No','NAMA',' NIM ','KELAS','BIAYA UTS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uts,bayar_spp,bayar_seminar,bayar_kas,admin,akhir]])
        print (table.draw())

        

def uas():
        from texttable import Texttable
        table = Texttable()
        jawab = "y"
        no = 0
        nama =[]
        nim = []
        kelas = []
        jum_matkul_uas_bayar = []
        bulan_bayar = []
        seminar_bayar = []
        kas_bayar = []
        print('\n********************************\t')
        print("\n**********BAYARAN UAS*********\t")
        print('\n********************************\t')
        while(jawab == "y") :
            nama.append(input(" NAMA : "))
            nim.append(input(" NIM   : "))
            kelas.append(input("KELAS : "))
            print('\n**********************************************************************\t')
            print('\n**********************************************************************\t')
            jum_matkul_uas_bayar.append(input("MATA KULIAH YANG DI BAYAR UNTUK UAS : "))
            bulan_bayar.append(input("JUMLAH BULAN BIAYA YANG DIBAYAR : "))
            print('\n**********************************************************************\t')
            

            
            
            pil = input("MAU BAYAR SEMINAR SAYANG [Y/T]  ? ")
            
            if pil == 'y' :
                    bayar_seminar = 100000
            else :
                    bayar_seminar = 0

            pil = input("MAU BAYAR KAS SAYANG [Y/T]  ? ")

                  
            if pil == 'y' :
                    bayar_kas = 200000
            else :
                    bayar_kas = 0
                
            jawab = input ("INGIN BAYAR LAGI ATAU TIDAK SAYANG (Y/T) : ")
            no += 1
        
        for i in range (no):
            bayar_uas = int(jum_matkul_uas_bayar[i])*50000
            bayar_spp = int (500000)
            bayar_seminar = int (100000)
            bayar_kas = int(20000)
            admin = int("5000")
            akhir = bayar_uas + bayar_spp + bayar_seminar + bayar_kas + admin
            table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
            table.set_cols_align(["i", "c", "c", "c", "c","c","c","c","c","c"])
            table.set_cols_width([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
            
            table.add_rows([['No','NAMA','NIM','KELAS','BIAYA UAS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uas,bayar_spp,bayar_seminar,bayar_kas,admin,akhir]])
        print (table.draw())
    
        exit
