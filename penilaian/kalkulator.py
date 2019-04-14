''' Program kalkulator sederhana untuk menjumlah, mengurang, mengali, dan membagi bilangan dengan menggunakan fungsi '''
def kalkulator():
   from texttable import Texttable
    
   
# fungsi penjumlahan
   def add(x, y):
      return x + y
# fungsi pengurangan
   def subtract(x, y):
      return x - y
# fungsi perkalian
   def multiply(x, y):
      return x * y
# fungsi pembagian
   def divide(x, y):
      return x / y
# menu operasi

   print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\t")
   print("\n~~~~~~~~SELAMAT DATANG DI PROGRAM KALKULATOR~~~~~~~~~\t")
   print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\t")
   print("Pilih Operasi.")
   print("1.Jumlah")
   print("2.Kurang")
   print("3.Kali")
   print("4.Bagi")
# Meminta input dari user
   

   choice = input("Masukkan pilihan(1/2/3/4): ")
   print('\n---------------------------------------------------\t')
   print('\n---------------------------------------------------\t')
   num1 = int(input("\nMasukkan bilangan pertama\t: "))
   num2 = int(input("\nMasukkan bilangan kedua\t: "))
   print('\n---------------------------------------------------\t')
   print('\n---------------------------------------------------\t')
   if choice == '1':
      print(num1,"+",num2,"=", add(num1,num2))
   elif choice == '2':
      print(num1,"-",num2,"=", subtract(num1,num2))
   elif choice == '3':
      print(num1,"*",num2,"=", multiply(num1,num2))
   elif choice == '4':
      print(num1,"/",num2,"=", divide(num1,num2))
   else:
      print("Input salah")


