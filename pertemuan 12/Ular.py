from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak
        print("Design\t\t:", self.design,
              "\nRacun\t\t:", self.racun,
              "\n-------------------------------")
              
        
anaconda = Ular ("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa")
anaconda.cetak()
anaconda.cetak_ular()
sanca = Ular ("Sanca", "Kambing", "Semak-Semak", "Bertelur", "Batik Solo", "Tidak Berbisa")
sanca.cetak()
sanca.cetak_ular()


    
