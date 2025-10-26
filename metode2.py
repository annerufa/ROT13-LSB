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

    """Versi super sederhana"""
    try:
        img = Image.open(gambar_input).convert('RGB')
        lebar, tinggi = img.size
        
        # Siapkan pesan
        pesan_full = enkripsi_rot13(pesan) + "###"
        pesan_biner = ''.join(format(ord(c), '08b') for c in pesan_full)
        
        # Cek kapasitas
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
                
                if bit_index >= len(pesan_biner):
                    img.save(gambar_output, "JPEG", quality=95)
                    return True, "Sukses!"
        
        img.save(gambar_output, "JPEG", quality=95)
        return True, "Sukses!"
        
    except Exception as e:
        return False, f"Error: {str(e)}"