from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_burung(self):
        super().cetak
        print("Jenis\t\t:", self.jenis,
              "\nBunyi\t\t:", self.bunyi,
              "\n-------------------------------")
        
elang = Burung("Elang", "Kadal", "Pohon", "Bertelur", "Corak Batik", "Siulan")
elang.cetak()
elang.cetak_burung()
perkutut = Burung("Perkutut", "Buah-Buahan", "Pohon", "Bertelur", "Corak Batik", "Kicauan")
perkutut.cetak() 
perkutut.cetak_burung()
