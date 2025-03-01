cars = ["honda","Toyota","Nissan"]

print(cars)
print(cars[1])
print(cars[2])

x = cars[0]
print(x)

"""Edit salah satu value pada array"""
cars = ["honda","Toyota","Nissan"]
cars[0] = "Hyundai"
print(cars)

"""Panjang Array / Length Array"""
x = len(cars)
print(x)

"""Looping Array"""
for x in cars:
    print(x)

"""Adding Array Elements / Menambahkan Nilai baru pada array"""
cars.append("Rolls Royce")
print(cars)

"""Removing Array Elements / Menghapus Elemen Array"""
cars.pop(0) # gunakan pop jika ingin menghapus berdasarkan index
print(cars)

cars.remove("Toyota") # gunakan remove jika ingin menghapus sesuai dengan nama dari elemen array tersebut
print(cars)

""" Array Methods """
""" Append() = digunakan untuk menambahkan elemen array baru ke dalam array """
""" clear() = digunakan untuk menghapus semua elemen pada array """
""" copy() = digunakan untuk mengembalikan salinan daftar """
""" count() = mengembalikan nomor dari elemen dengan """