# Tugas Latihan Algoritma dan Pseudocode

### 1. Cari nilai KPK dari 3 dan 4

**Algoritma:**
1. Mulai
2. Inisialisasi dua variabel, `bilangan1` dengan nilai 3 dan `bilangan2` dengan nilai 4.
3. Inisialisasi variabel `kpk` dengan nilai terbesar dari `bilangan1` dan `bilangan2`.
4. Lakukan perulangan selama `kpk` tidak habis dibagi `bilangan1` atau `bilangan2`:
   - Tambahkan `kpk` dengan nilai terbesar dari `bilangan1` dan `bilangan2`.
5. Tampilkan nilai `kpk`.
6. Selesai

**Pseudocode:**
```
BILANGAN1 <- 3
BILANGAN2 <- 4
KPK <- maks(BILANGAN1, BILANGAN2)

SELAMA (KPK MOD BILANGAN1 != 0 ATAU KPK MOD BILANGAN2 != 0)
    KPK <- KPK + maks(BILANGAN1, BILANGAN2)

TAMPILKAN KPK
```

### 2. Fungsi untuk menukar posisi dua variabel

**Algoritma:**
1. Mulai
2. Deklarasikan tiga variabel: `manggis`, `pisang`, dan `temp`.
3. Simpan nilai `manggis` ke dalam variabel `temp`.
4. Assign nilai `pisang` ke `manggis`.
5. Assign nilai `temp` ke `pisang`.
6. Selesai

**Pseudocode:**
```
PROSEDUR TUKAR(manggis, pisang)
    temp <- manggis
    manggis <- pisang
    pisang <- temp
```

**Penjelasan analogi:**
Misal:
* `manggis` adalah piring 1
* `pisang` adalah piring 2
* `temp` adalah piring 3 kosong

Prosesnya:
1. Isi piring 3 dengan isi piring 1.
2. Pindahkan isi piring 2 ke piring 1.
3. Pindahkan isi piring 3 (yang sebelumnya isi piring 1) ke piring 2.

### 3. Hitung luas segitiga

**Algoritma:**
1. Mulai
2. Deklarasikan variabel `alas` dengan nilai 25 dan `tinggi` dengan nilai 30.
3. Hitung luas dengan rumus `luas = 0.5 * alas * tinggi`.
4. Tampilkan nilai luas.
5. Selesai

**Pseudocode:**
```
ALAS <- 25
TINGGI <- 30
LUAS <- 0.5 * ALAS * TINGGI
TAMPILKAN LUAS
```

### 4. Hitung luas jajar genjang

**Algoritma:**
1. Mulai
2. Deklarasikan variabel `panjang` dengan nilai 5 dan `tinggi` dengan nilai 3.
3. Hitung luas dengan rumus `luas = panjang * tinggi`.
4. Tampilkan nilai luas.
5. Selesai

**Pseudocode:**
```
PANJANG <- 5
TINGGI <- 3
LUAS <- PANJANG * TINGGI
TAMPILKAN LUAS
```

### 5. Hitung volume tabung

**Algoritma:**
1. Mulai
2. Deklarasikan variabel `jari_jari` dengan nilai 3 dan `tinggi` dengan nilai 5.
3. Hitung luas alas lingkaran dengan rumus `luas_alas = π * jari_jari^2`.
4. Hitung volume dengan rumus `volume = luas_alas * tinggi`.
5. Tampilkan nilai volume.
6. Selesai

**Pseudocode:**
```
JARI_JARI <- 3
TINGGI <- 5
LUAS_ALAS <- PI * JARI_JARI^2
VOLUME <- LUAS_ALAS * TINGGI
TAMPILKAN VOLUME
```

### 6. Hitung volume kerucut

**Algoritma:**
1. Mulai
2. Deklarasikan variabel `diameter` dengan nilai 5 dan `tinggi` dengan nilai 4.
3. Hitung jari-jari dengan rumus `jari_jari = diameter / 2`.
4. Hitung luas alas lingkaran dengan rumus `luas_alas = π * jari_jari^2`.
5. Hitung volume dengan rumus `volume = (1/3) * luas_alas * tinggi`.
6. Tampilkan nilai volume.
7. Selesai

**Pseudocode:**
```
DIAMETER <- 5
TINGGI <- 4
JARI_JARI <- DIAMETER / 2
LUAS_ALAS <- PI * JARI_JARI^2
VOLUME <- (1/3) * LUAS_ALAS * TINGGI
TAMPILKAN VOLUME
```
