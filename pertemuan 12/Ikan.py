from Animal import * 

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.jenis = jenis
    def cetak_ikan(self):
        super().cetak
        print("Design\t\t:",self.design,
              "\nJenis\t\t:",self.jenis,
              "\n-------------------------------")
              
        
teri = Ikan("Teri", "Plankton", "Air", "Bertelur", "Corak Batik", "Karnivora")
teri.cetak()
teri.cetak_ikan()
hiu = Ikan("Hiu", "Daging", "Air", "Bertelur", "Corak Batik", "Karnivora")
hiu.cetak()
hiu.cetak_ikan()


