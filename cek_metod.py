
from PIL import Image

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

# plainteks = "coba pesAn ini!"
# enkripsiteks = enkripsi_rot13(plainteks)
# print(f"plainteks: {plainteks}")
# print(f"hasil enkripsi: {enkripsiteks}")


def embed_pesan_lsb_simple(gambar_input, pesan):
    """Versi super sederhana"""
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
                    img.save("hasil.bmp", "BMP")
                    print("??????")
                    return True, "Sukses!"
        
    except Exception as e:
        return False, f"Error: {str(e)}"
    



embed_pesan_lsb_simple("images.jpeg","ini Adl Pesan.,")

