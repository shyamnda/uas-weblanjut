from django.contrib import admin
from berita.models import Artikel, Kategori
# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['nama']
admin.site.register(Kategori, KategoriAdmin)

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['judul', 'isi', 'kategori', 'author']
    search_fields = ['judul']
admin.site.register(Artikel, ArtikelAdmin)