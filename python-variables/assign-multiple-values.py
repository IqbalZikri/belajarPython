"""Banyaknya nilai untuk beberapa variable"""
"""Python memperbolehkan anda untuk memasukkan nilai ke beberapa variable di satu baris"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

"""Satu nilai untuk beberapa variable"""
x = y = z = "Orange"
print(x)
print(y)
print(z)

"""Membuka Koleksi / Unpack a Collection"""
"""Jika Anda memiliki kumpulan nilai dalam bentuk daftar, tuple, dsb. Python memungkinkan Anda untuk mengekstrak nilai ke dalam variabel. Ini disebut unpacking."""
fruits = ["apple","banana","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)