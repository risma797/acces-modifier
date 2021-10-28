class Mixer:
  kecepatan_sekarang = 0
  fungsi = []
  __activeFungsi = None

  #fungsi construktor
  def __init__ (self, nama_merk, jumlah_tungkai_pengaduk, kecepatan_mixer):
    self.nama_merk = nama_merk
    self.jumlah_tungkai_pengaduk = jumlah_tungkai_pengaduk
    self.kecepatan_mixer = kecepatan_mixer
    
  def nyalakanMixer(self):
    print('Mixer menyala ', self.nama_merk)

  def matikanMixer(self):
    print('Mixer dimatikan ', self.nama_merk)

  def menambahKecepatan(self):
    self.kecepatan_sekarang = self.kecepatan_sekarang + 3
    print('kecepatan_sekarang ', self.kecepatan_sekarang)

 
  def _scan(self):
    print('fungsi')
    self.__fungsi = ['Mengaduk', 'Mencampur', 'Menguleni']

  def _setFungsi(self):
    print('set fungsi')
    self.__activefungsi = self.__fungsi[0]

  def getActiveFungsi(self):
    self.__activefungsi = self.__fungsi[0]
    return self.__activefungsi

class Mixer2(Mixer):
    def __init__(self, nama_merk, jumlah_tungkai_pengaduk, kecepatan_mixer):
        super(Mixer2, self).__init__(nama_merk, jumlah_tungkai_pengaduk, kecepatan_mixer)
        self._scan()
        self._setFungsi()
        
    def menambahKecepatan(self, kec):
        self.kecepatan_sekarang = self.kecepatan_sekarang + kec
        print('kecepatan_sekarang ', self.kecepatan_sekarang)

carMixer = Mixer2('A', 'B', 'C')
print(carMixer.getActiveFungsi())
