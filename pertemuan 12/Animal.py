class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print("Nama\t\t:",self.nama,
              "\nMakanan\t\t:",self.makanan,
              "\nHidup\t\t:",self.hidup,
              "\nBerkembang_Biak\t:",self.berkembang_biak)
           