from flask import Flask # digunakan untuk mengimport atau memanggil sebuah framework bernama flask

app = Flask(__name__) # Digunankan untuk membuat sebuah variabel yang didalamnya menyimpan instance dari aplikasi flask, __name__ adalah variable khusus dalam python yang berisi nama modul saat ini
""" 
Tujuan __name__ dalam flask :
-> Flask menggunakan nilai ini untuk mengetahui di mana letak aplikasi utama.
-> Berguna untuk menemukan file statis, template, dan sumber daya lainnya.
-> Jika file ini dijalankan langsung (python nama_file.py), __name__ bernilai "__main__", tetapi jika diimpor sebagai modul, bernilai nama modulnya.
"""

@app.route('/')
def index():
    return '<h1>Home</h1>'

@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'

@app.route('/profile', defaults = {'username': 'guest'})
@app.route('/profile/<string:username>')
def profile_name(username):
    return '<h1>Hello %s!</h1>' % username