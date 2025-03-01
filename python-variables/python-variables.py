## Python Variable
x = 5
y = "hello World"
print(x)
print(y)

# isi variable bisa berubah ketika anda mengisinya lagi dengan nilai yang berbeda
x = 5
x = "Sally" # sekarang variable x akan berisi Sally
print(x) 

# Casting
x = str(3) # x akan berisi '3'
y = int(3) # y akan berisi angka 3
z = float(3) # z akan berisi 3.0

# Get The Type
x = 5
y = "John"
print(type(x))
print(type(y))

# single or double quotes?
# variable string bisa di deklarasikan dengan menggunakan single quotes atau double quotes
x = "John"
# sama saja dengan
y = 'John'

# perbedaan "" dengan '' adalah
# a. menggunakan "" jika ada tanda kutip tunggal di dalam string
kalimat = "Hari ini adalah hari Jum'at."
print(kalimat) # Benar

# Jika menggunakan ', maka harus menggunakan escape (\')
kalimat = 'Hari ini adalah hari Jum\'at.'
print(kalimat)

# b. menggunakan '' jika ada tanda kutip dua di dalam string
kalimat = 'Dia berkata, "Halo apa kabar?"'
print(kalimat)
# JIka menggunakan tanda "", harus meenggunakan escape (\")
kalimat = "Dia berkata, \"Halo apa kabar?\""
print(kalimat)

# Case Sensitive
# nama variable itu berpengatuh dengan huruf besar atau kecil
a = 4
A = "Sally" # A tidak akan menggantikan a