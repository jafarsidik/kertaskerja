import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class DaftarSasaran(models.Model):
    unitkerja = models.ForeignKey('masterdata.Masterunitusaha', on_delete=models.CASCADE)
    penanggungjawab = models.ForeignKey('masterdata.Masterpimpinanunitkerja', on_delete=models.CASCADE)
    indikatorkinerja = models.ForeignKey('masterdata.Masterindikatorkinerja', on_delete=models.CASCADE)
    perspektifbsc = models.ForeignKey('masterdata.Masterperspektifbsc', on_delete=models.CASCADE)
    sasaran = models.TextField()
    targetkinerja = models.IntegerField()
    def __str__(self):
        return self.sasaran

class DaftarKegiatan(models.Model):
    sasaran = models.ForeignKey(DaftarSasaran, on_delete=models.CASCADE)
    kegiatan = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    penanggung_jawab_kegiatan = models.CharField(max_length=100)
    akuncoa = models.ForeignKey('masterdata.Masterakuncoa', on_delete=models.CASCADE)
    anggaran_biaya = models.IntegerField()
    
    def __str__(self):
        return self.kegiatan