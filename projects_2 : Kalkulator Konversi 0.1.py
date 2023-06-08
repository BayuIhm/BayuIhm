import math

class Temperature:
    def __init__(self):
        self.celsius = 5
        self.reamur = 4
        self.fahrenheit = 9
        self.kelvin = 5
    def to_celsius(self, dif, result):
        return float(result) * 5 / dif
    def to_reamur(self, dif, result):
        return float(result) * 4 / dif
    def to_fahrenheit(self, dif, result):
        return float(result) * 9 / dif + 32
    def to_kelvin(self, dif, result):
        return result * 5/int(dif) + 273
    def get_unit_div(self, unit):
        unit_div = {
        1 : "celsius",
        2 : "reamur",
        3 : "fahrenheit",
        4 : "kelvin"
        }
        return unit_div[unit]
    def run(self):
        strip = "_"
        dot = "."
        strip1 = "—"
        title = "KALKULATOR KONVERSI SUHU"
        print()
        print(f"{strip:_^60}")
        print(f"{title:.^60}")
        print(f"{strip1:—^60}")
        print()
        print('''Silahkan masukan satuan sesuai angka berikut :
            1. Celsius
            2. Reamur
            3. Fahrenheit
            4. Kelvin''')
        print(f"{strip1:—^30}")
        unit_in = int(input("Masukan satuan awalnya (1 ~ 4)! : "))
        temp_in = int(input("Masukan suhu awalnya! : "))
        unit_out = int(input("Masukan satuan akhirnya (1~4)! : "))
        if unit_in in [1, 2]:
            result = temp_in
        elif unit_in == 3:
            result = float(temp_in) - 32
        elif unit_in == 4:
            result = float(temp_in) - 273
        else:
            print("Input Tidak Valid")
            
        dif = getattr(self, self.get_unit_div(unit_in))
            
        if unit_out == 1:
            unt = "celsius"
            conv = self.to_celsius(dif, result)
        elif unit_out == 2:
            unt = "reamur"
            conv = self.to_reamur(dif, result)
        elif unit_out == 3:
            unt = "fahrenheit"
            conv = self.to_fahrenheit(dif, result)
        elif unit_out == 4:
            unt = "kelvin"
            conv = self.to_kelvin(dif, result)
        else:
            print("input tidak valid! ")
            
        print(f"Hasil konversinya adalah {conv} derajat {unt}")
        
class Length:
    def __init__(self):
        self.kilo = 0.001
        self.hekto = 0.01
        self.deka = 0.1
        self.meter = 1
        self.desi = 10
        self.centi = 100
        self.mili = 1000
        self.mikro = 1000000
        self.nano = 1000000000
    def convert(self, base_length, unit1, unit2):
        return float(base_length) * unit2 / unit1
    def get_unit_div(self, unit):
        unit_div = {
            1 : self.kilo,
            2 : self.hekto,
            3 : self.deka,
            4 : self.meter,
            5 : self.desi,
            6 : self.centi,
            7 : self.mili,
            8 : self.mikro,
            9 : self.nano
        }
        return unit_div[unit]
    def get_unit_names(self, names):
        unit_name = {
            1 : "Kilometer",
            2 : "Hektometer",
            3 : "Dekameter",
            4 : "Meter",
            5 : "Desimeter",
            6 : "Centimeter",
            7 : "Milimeter",
            8 : "Micrometer",
            9 : "Nanometer"
        }
        return unit_name[names]
    def run(self):
        strip = "_"
        strip1 = "—"
        dot = "."
        title = "KALKULATOR KONVERSI PANJANG"
        print()
        print(f"{strip:_^60}")
        print(f"{title:.^60}")
        print(f"{strip1:—^60}")
        print()
        print('''Silahkan masukan satuan sesuai angka berikut :
            1. Kilometer
            2. Hektometer
            3. Dekameter
            4. Meter
            5. Desimeter
            6. Centimeter
            7. Milimeter
            8. Micrometer
            9. Nanometer''')
        print(f"{strip1:—^60}")
        unit_in = int(input("Masukan satuan awalnya! :"))
        base_length = float(input("Masukan panjang awalnya! :"))
        unit_out = int(input("Masukan satuan akhirnya! :"))
        unit1 = self.get_unit_div(unit_in)
        unit2 = self.get_unit_div(unit_out)
        unit_names = self.get_unit_names(unit_out)
        if unit_in not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Input tidak ditemukan!")
            return
        if unit_out not in [1, 2, 3, 4, 5, 6, 7, 8 ,9]:
            print("Output tidak ditemukan!")
            return
        result = self.convert(base_length, unit1, unit2)
        print(f"Hasil konversinya adalah {result} {unit_names}")
        
class Dimensions:
    def square(self):
        s = int(input("Masukan panjang sisinya"))
        area = int(s)**2
        return area
    def rectangular(self):
        p = int(input("Masukan panjangnya! "))
        l = int(input("Masukan lebarnya!"))
        area = int(p) * int(l)
        return area
    def rectangle(self):
        a = input("Masukan panjang alasnya! :")
        t = input("Masukan tingginya! : ")
        area = int(a) * int(t) / 2
        return area
    def parallelogram(self):
        a = int(input("Masukan panjang alasnya! : "))
        t = int(input("Masukan tingginya! : "))
        area = int(a) * int(b)
        return area
    def trapezoid(self):
        s1 = int(input("Masukkan panjang sisi pertama! : "))
        s2 = int(input("Masukkan panjang sisi kedua! : "))
        t = int(input("Tinggi : "))
        area = (int(s1) + int(s2)) * int(t) / 2
        return area
    def circle(self):
        r = int(input("Masukkan jari jarinya! : "))
        if r %7 == 0:
            π = 22/7
        elif r %7 != 0:
            π = math.pi
        else:
            print("Input tidak valid!")
        area = float(π) * int(r)**2
        return area
    def run(self):
        strip = "_"
        strip1 = "—"
        title = "KALKULATOR LUAS BANGUN DATAR"
        print()
        print(f"{strip:_^60}")
        print(f"{title:.^60}")
        print(f"{strip1:—^60}")
        print()
        print('''Silahkan pilih bangun datar yang akan dihitung :
            1. Persegi
            2. Persegi Panjang
            3. Segitiga
            4. Jajargenjang
            5. Trapesium
            6. Lingkaran''')
        print(f"{strip1:—^60}")
        user = int(input("Masukan pilihan sesuai angka diatas! : "))
        unit = input("Masukan satuannya! : ").lower().strip()
        if user == 1:
            luas = self.square()
        elif user == 2:
            luas = self.rectangular()
        elif user == 3:
            luas = self.rectangle()
        elif user == 4:
            luas = self.parallelogram()
        elif user == 5:
            luas = self.trapezoid()
        elif user == 6:
            luas = self.circle()
        print(f"Luasnya = {luas} {unit}²")
        
temperature = Temperature()
length = Length()
dimensions = Dimensions()
NAMA = "KALKULATOR KONVERSI BETA"
strip = "_"
strip1 = "—"
dot = "."
print(f"{strip:_^60}")
print(f"{NAMA:.^60}")
print(f"{strip1:—^60}")
print('''Kalkulator ini masih dalam tahap beta, jadi mohon maaf jika ada beberapa bug atau error yang terjadi :
    1. Open
    2. Exit
    ''')
option = int(input("Masukan nomor diatas! :"))
if option == 1:
    while True:
        print(f"{strip:_^60}")
        print("Selamat datang, silahkan pilih!")
        print('''Menu :
           1. Konversi Suhu
           2. Konversi panjang
           3. Luas Bangun datar
           4. Exit
                   ''' )
        menu = int(input("Masukan pilihnamu! :"))
        if menu == 1:
                temperature.run()
        elif menu == 2:
            length.run()
        elif menu == 3:
            dimensions.run()
        elif menu == 4:
            print("Terima Kasih!")
            break
        else:
            print("Input tidak valid")
else:
    thanks = "TERIMA KASIH"
    print(f"{strip:_^60}")
    print(f"{dot:.^60}")
    print(f"{thanks:.^60}")
    print(f"{dot:.^60}")
    print(f"{strip1:—^60}")                