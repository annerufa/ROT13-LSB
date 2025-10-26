from PIL import Image
import os
import io

# ===============================
# FUNGSI ROT13
# ===============================

def enkripsi_rot13(teks):
    """
    Melakukan enkripsi ROT13 pada teks
    """
    hasil = ""
    for karakter in teks:
        if 'a' <= karakter <= 'z':
            # Untuk huruf kecil
            hasil += chr((ord(karakter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= karakter <= 'Z':
            # Untuk huruf besar
            hasil += chr((ord(karakter) - ord('A') + 13) % 26 + ord('A'))
        else:
            # Untuk karakter non-alphabet
            hasil += karakter
    return hasil

def dekripsi_rot13(teks):
    """
    Melakukan dekripsi ROT13 pada teks
    ROT13 adalah cipher simetris, jadi enkripsi = dekripsi
    """
    return enkripsi_rot13(teks)

# ===============================
# FUNGSI STEGANOGRAFI LSB
# ===============================

def embed_pesan_lsb(gambar_input, pesan, gambar_output):
    try:
        img = Image.open(gambar_input).convert('RGB')
        lebar, tinggi = img.size
        
        # Siapkan pesan
        print(f"Teks pesan: {pesan}")
        pesan_full = enkripsi_rot13(pesan) + "###"
        print(f"Teks terenkripsi + tanda akhir pesan: {pesan_full}")

        pesan_biner = ''.join(format(ord(c), '08b') for c in pesan_full)
        print(f"Pesan diubah menjadi biner: {pesan_biner}")
        print(f"Panjang biner: {len(pesan_biner)} bit")
        print(f"Total karakter: {len(pesan_full)}")
        # Cek kapasitas
        if len(pesan_biner) > lebar * tinggi * 3:
            return False, "Pesan terlalu panjang!"
        
        # Embed

        # pixels = list(img.getdata())
        print(f"list data pixel pada gambar")
        pixels = img.load()
        bit_index = 0
        print("Proses embeding: . . . . . . .")

        for y in range(tinggi):
            for x in range(lebar):
                r, g, b = pixels[x, y]

                print(f"\npixel asli: {pixels[x, y]}")
                for i, channel in enumerate([r, g, b]):
                    # print(f"penyematan bit ke rbg")
                    if bit_index < len(pesan_biner):
                        # print(f"nilai channel: {channel}\nbiner pesan: {pesan_biner[bit_index]}")
                        new_val = (channel & 0xFE) | int(pesan_biner[bit_index])
                        # print(f"nilai channel baru: {new_val}")
                        if i == 0: r = new_val
                        elif i == 1: g = new_val
                        else: b = new_val
                        bit_index += 1

                pixels[x, y] = (r, g, b)
                # pixel = (r, g, b)
                # print("Simpan pixel terbaru")
                print(f"pixel terbaru: {pixels[x, y]}")
                # print(f"bit yang diubah: {bit_index}")

                if bit_index >= len(pesan_biner):
                    # img.save(gambar_output, "JPG", quality=100)
                    img.save(gambar_output, "BMP")
                    # img.save("gambar_output.bmp", "BMP")
                    return True, "Pesan berhasil diembed ke gambar BMP!"
        
    except Exception as e:
        return False, f"Error saat embedding: {str(e)}"

def ekstrak_pesan_lsb(gambar_input):
    """Berhenti begitu menemukan delimiter - lebih efisien"""
    # Buka gambar
    print(f"🔍 Membuka gambar: {gambar_input}")
    gambar = Image.open(gambar_input)
    print(f"✅ Gambar berhasil dibuka: {gambar.size}, mode: {gambar.mode}")
    gambar = gambar.convert('RGB')
    print("🔄 Gambar dikonversi ke RGB")

    pixels = list(gambar.getdata())
    # 1. LIST UNTUK MENYIMPAN KARAKTER YANG SUDAH DIKONVERSI
    pesan_terekstrak = []
    
    # 2. BUFFER UNTUK MENYIMPAN BIT SEBELUM DIKONVERSI KE KARAKTER
    buffer_biner = []

    # Dapatkan semua pixel sekaligus (seperti teman Anda)
    # 3. LOOP MELALUI SETIAP PIXEL
    for pixel in pixels:  # Lebih cepat akses pixel-nya
        # Ambil nilai RGB dari pixel (x, y)
        r, g, b = pixel
            
        # 4. EKSTRAK LSB DARI SETIAP CHANNEL
        # r & 1 → ambil bit terakhir (LSB)
        # str(...) → ubah ke string '0' atau '1'
        # extend → tambahkan ke buffer
        buffer_biner.extend([str(r & 1), str(g & 1), str(b & 1)])
        print(f"3 bit di 1 pixel ditambahkan\n - buffer_biner: {buffer_biner} ")

        # 5. KONVERSI BIT KE KARAKTER SETIAP 8 BIT
        while len(buffer_biner) >= 8:
            # Ambil 8 bit pertama dari buffer
            byte = ''.join(buffer_biner[:8])
            print(f"8 bit untuk 1 karakter: {byte} ")

            # Hapus 8 bit yang sudah diambil dari buffer
            buffer_biner = buffer_biner[8:]
            print(f"8 bit dihapus\n - buffer_biner: {buffer_biner} ")
            
            # Konversi 8 bit menjadi karakter ASCII
            karakter = chr(int(byte, 2))
            print(f"karakter yang didapat: {karakter} ")

            pesan_terekstrak.append(karakter)
            print(f"pesan yang didapat: {pesan_terekstrak} ")
            
            # 6. CEK DELIMITER - EARLY TERMINATION
            print("cek jika sudah menemukan 3 karakter ### sebagai tanda akhir pesan")
            if len(pesan_terekstrak) >= 3 and ''.join(pesan_terekstrak[-3:]) == "###":
                print("yup pesan berakhir")
                # Gabungkan semua karakter kecuali 3 terakhir (delimiter)
                pesan_akhir = ''.join(pesan_terekstrak[:-3])
                # Dekripsi dan kembalikan hasil
                return True, dekripsi_rot13(pesan_akhir)
    
    # 7. JIKA SAMPAI SINI, PESAN TIDAK DITEMUKAN
    return False, "Tidak ditemukan pesan"