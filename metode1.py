from PIL import Image


def enkripsi_rot13(teks):
    """
    Melakukan enkripsi ROT13 pada teks
    """
    hasil = ""
    for karakter in teks:
        if 'a' <= karakter <= 'z':
            hasil += chr((ord(karakter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= karakter <= 'Z':
            hasil += chr((ord(karakter) - ord('A') + 13) % 26 + ord('A'))
        else:
            hasil += karakter
    return hasil

def dekripsi_rot13(teks):
    """
    Melakukan dekripsi ROT13 pada teks
    ROT13 adalah cipher simetris, jadi enkripsi = dekripsi
    """
    return enkripsi_rot13(teks)



def embed_pesan_lsb(gambar_input, pesan, gambar_output):
    try:
        img = Image.open(gambar_input).convert('RGB')
        lebar, tinggi = img.size
        
        pesan_full = enkripsi_rot13(pesan) + "###"

        pesan_biner = ''.join(format(ord(c), '08b') for c in pesan_full)

        # Jika biner pesan lebih banyak dibanding total channel pada gambar
        if len(pesan_biner) > lebar * tinggi * 3:
            return False, "Pesan terlalu panjang!"
        
        # Embed
        pixels = img.load()
        bit_index = 0

        for y in range(tinggi):
            for x in range(lebar):
                r, g, b = pixels[x, y]

                for i, channel in enumerate([r, g, b]):
                    if bit_index < len(pesan_biner):
                        new_val = (channel & 0xFE) | int(pesan_biner[bit_index])
                        if i == 0: r = new_val
                        elif i == 1: g = new_val
                        else: b = new_val
                        bit_index += 1

                pixels[x, y] = (r, g, b)
                print(f"pixel terbaru: {pixels[x, y]}")

                if bit_index >= len(pesan_biner):
                    img.save(gambar_output, "BMP")
                    return True, "Pesan berhasil diembed ke gambar BMP!"
        
    except Exception as e:
        return False, f"Error saat embedding: {str(e)}"

def ekstrak_pesan_lsb(gambar_input):
    """Berhenti begitu menemukan delimiter - lebih efisien"""
    # Buka gambar
    gambar = Image.open(gambar_input)
    gambar = gambar.convert('RGB')

    pixels = list(gambar.getdata())
    # 1. LIST UNTUK MENYIMPAN KARAKTER YANG SUDAH DIKONVERSI
    pesan_terekstrak = []
    
    # 2. BUFFER UNTUK MENYIMPAN BIT SEBELUM DIKONVERSI KE KARAKTER
    buffer_biner = []

    for pixel in pixels: 
        r, g, b = pixel
            
        buffer_biner.extend([str(r & 1), str(g & 1), str(b & 1)])

        # cek jika sudah terkumpul minimal 8 bit
        while len(buffer_biner) >= 8:
            # Ambil 8 bit pertama dari buffer
            byte = ''.join(buffer_biner[:8])

            # Hapus 8 bit yang sudah diambil dari buffer
            buffer_biner = buffer_biner[8:]
            
            # Konversi 8 bit menjadi karakter ASCII
            karakter = chr(int(byte, 2))
            pesan_terekstrak.append(karakter)
            
            # cek jika sudah mencapai akhir pesan
            if len(pesan_terekstrak) >= 3 and ''.join(pesan_terekstrak[-3:]) == "###":
                pesan_akhir = ''.join(pesan_terekstrak[:-3])
                return True, dekripsi_rot13(pesan_akhir)
    
    return False, "Tidak ditemukan pesan"