data_panen = data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("seluruh data panen: ")
for lokasi, data in data_panen.items():
    nama_lokasi = data ['nama_lokasi']
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    kedelai = data['hasil_panen']['kedelai']
    print(f"{nama_lokasi}: padi: {padi}, jagung: {jagung}, kedelai: {kedelai}")

lokasi2_jagung = data_panen['lokasi2']['hasil_panen']['jagung']
print(f'\nHasil panen jagung dari {data_panen['lokasi2']['nama_lokasi']}: {lokasi2_jagung}')

lokasi3_nama = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {lokasi3_nama}")

padi_perlokasi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
kedelai_perlokasi = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print("\nJumlah hasil panen pagi per lokasi:", padi_perlokasi)
print("Jumlah hasil panen kedelai per lokasi:", kedelai_perlokasi)

print("\nKondisi lokasi")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")"Perubahan di master" 
