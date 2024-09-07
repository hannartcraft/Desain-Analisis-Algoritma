# 1. KPK dari 3 dan 4
def kpk(bilangan1, bilangan2):
    """Mencari KPK dari dua bilangan."""
    kpk = max(bilangan1, bilangan2)
    while kpk % bilangan1 != 0 or kpk % bilangan2 != 0:
        kpk += max(bilangan1, bilangan2)
    return kpk

print(kpk(3, 4))

# 2. Menukar dua variabel
def tukar(a, b):
    """Menukar nilai dua variabel."""
    temp = a
    a = b
    b = temp

# Contoh penggunaan
manggis = "piring 1"
pisang = "piring 2"
tukar(manggis, pisang)
print(manggis, pisang)

# 3. Luas segitiga
def luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga."""
    luas = 0.5 * alas * tinggi
    return luas

print(luas_segitiga(25, 30))

# 4. Luas jajar genjang
def luas_jajar_genjang(panjang, tinggi):
    """Menghitung luas jajar genjang."""
    luas = panjang * tinggi
    return luas

print(luas_jajar_genjang(5, 3))

# 5. Volume tabung
def volume_tabung(jari_jari, tinggi):
    """Menghitung volume tabung."""
    import math
    luas_alas = math.pi * jari_jari**2
    volume = luas_alas * tinggi
    return volume

print(volume_tabung(3, 5))

# 6. Volume kerucut
def volume_kerucut(diameter, tinggi):
    """Menghitung volume kerucut."""
    import math
    jari_jari = diameter / 2
    luas_alas = math.pi * jari_jari**2
    volume = (1/3) * luas_alas * tinggi
    return volume

print(volume_kerucut(5, 4))
