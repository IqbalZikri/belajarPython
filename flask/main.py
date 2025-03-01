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

@app.route('/profile', defaults = {'_route': "home",'username': 'guest'})
@app.route('/profile/<string:username>', defaults = {'_route' : "profile"})
def profile_name(username, _route):
    if _route == "home" :
        return '<h1>Profile %s</h1>' % username
    elif _route == "profile" :
        return '<h1>Hello %s!</h1>' % username