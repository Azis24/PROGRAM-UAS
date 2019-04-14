def jabatan () :
    
    from texttable import Texttable
    table1 = Texttable ()
    no1 = 0
    nama1 = []
    jabatan = []
    gaji = []
    jawab1 = "ya"

    while (jawab1 == 'ya'):
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\t")
        print("\n~~~~~~~~SELAMAT DATANG DI PROGRAM JABATAN~~~~~~~~~\t")
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\t")
        nama1.append (input("masukan nama: "))
        
        jab = input("Jabatan : ")
        jabatan.append(jab)
        if  (jab == 'PROGRAMER') :
            gaji.append(3000000)
            
        
            
            
        elif (jab == 'Kasir') :
            gaji.append(200000)
            
            
        
            
            
        elif (jab == 'Satpam') :
            gaji.append(500000)
            
    
            
            
        else:
            break
        no1+=1
        jawab1 = input("\n tambah lagi : ")
        
    for i1 in range (no1) :

        table1.add_rows([['No','Nama','Jabatan','Gaji'], [i1+1, nama1[i1],jabatan[i1],gaji[i1]]])                      
    print(table1.draw())


