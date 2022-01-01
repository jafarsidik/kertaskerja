import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Masterunitusaha(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterdirektorat(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterdivisi(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterpimpinanunitkerja(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterperspektifbsc(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterfungsi(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masteraspek(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterkategoririsiko(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterrisiko(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Mastertiperisiko(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterkreteriadampak(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterfaktorexternal(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterfaktorintenal(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterkriteriakemungkinan(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterindikatorkinerja(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Masterakuncoa(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

