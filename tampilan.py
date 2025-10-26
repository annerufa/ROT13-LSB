import FreeSimpleGUI as sg
from PIL import Image
import io, os
from metode1 import ekstrak_pesan_lsb, embed_pesan_lsb
# --- Warna Tema ---
BG_COLOR = '#F8FAFC'
COLOR_1 = '#EFF5F5'
COLOR_2 = '#D6E4E5'
COLOR_3 = '#497174'
COLOR_4 = "#E24216"
COLOR_5 = "#274547"

def create_window():
    

    # --- Header (menu bar) ---
    menu_bar = [
        [
            sg.Button("Home", key="-HOME-", expand_x=True, size=(10, 2),border_width=0, button_color=(sg.theme_text_color(), COLOR_5)),
            sg.Button("Embed Pesan", key="-EMBED-", expand_x=True, size=(10, 2),border_width=0,button_color=(COLOR_5, COLOR_2)),
            sg.Button("Ekstrak Pesan", key="-EKSTRAK-", expand_x=True, size=(10, 2),border_width=0,button_color=(COLOR_5, COLOR_2)),
        ]
    ]

    # --- Layout untuk setiap halaman ---
    # home
    home_layout = [
        [sg.Text("ENKRIPSI ROT13 DAN STEGANOGRAFI LSB", font=("Roboto", 18), background_color=COLOR_2, text_color=COLOR_5, pad=((0,0), (100,10)))],
        [sg.Text("UAS KRIPTOGRAFI TI C 22", font=("Roboto", 14), background_color=COLOR_2, text_color=COLOR_5, pad=((0,0), (0,100)))],
        [sg.Text("KELOMPOK 2:", font=("Roboto", 12), background_color=COLOR_2, text_color=COLOR_5, pad=(0,0))],
        [sg.Text("22104410023 | ANNE RUFAEDAH", font=("Roboto", 10), background_color=COLOR_2, text_color=COLOR_5, pad=(0,0))],
        [sg.Text("22104410019 | LATIFAH HABIBITA ALIF", font=("Roboto", 10), background_color=COLOR_2, text_color=COLOR_5, pad=(0,0))],
        [sg.Text("21104413004 | HEPPY INDAH KUMALASARI", font=("Roboto", 10), background_color=COLOR_2, text_color=COLOR_5, pad=(0,0))]
    ]

    # embed
    embed_right = [
        [sg.Text("Masukkan Teks:", font=("Arial", 12),  text_color=COLOR_5, background_color=COLOR_2)],
        [sg.Multiline(size=(40, 8), key="-TEXT_INPUT-", background_color="white")],
        [sg.Text("Pilih Gambar untuk Disisipkan:", font=("Arial", 12),  text_color=COLOR_5,background_color=COLOR_2)],
        [sg.Input(key="-IMG_INPUT-", visible=False, enable_events=True),
        sg.FileBrowse("Pilih Gambar",file_types=(("Gambar BMP/JPG", "*.bmp;*.jpg;*.jpeg"),),size=(36, 2), pad=(7,2),button_color=("white", COLOR_5))],
        [sg.Button("Proses Embed", key="-PROSES-", button_color=(sg.theme_text_color(), COLOR_4),size=(36, 2), pad=(7,5))]
    ]

    embed_left = [
        [sg.Image(key="-IMG_PREVIEW-", size=(320, 320), background_color="gray")],
        [sg.Text("Preview Gambar", key="-INFO-", size=(50, 2), font=("Arial", 10), background_color=COLOR_2, text_color=COLOR_5)]
    ]

    embed_layout = [
        [sg.Text("Enkripsi ROT13 dan Embeded Steganografi LSB", font=("Roboto", 16),pad=(0,30),background_color=COLOR_2, text_color=COLOR_5)],
        [
            sg.Column(embed_left, size=(300, None), expand_x=True, expand_y=True, background_color=COLOR_2, justification="center"),
            sg.VSeparator(),
            sg.Column(embed_right, size=(300, None), expand_x=True, expand_y=True, background_color=COLOR_2, justification="center"),
        ]
    ]

    # ekstraksi
    ekstraksi_layout = [
        [sg.Text("Ekstraksi Steganografi LSB dan Dekripsi ROT13", font=("Roboto", 16),pad=(0,30),text_color=COLOR_5, background_color=COLOR_2)],
        [sg.HorizontalSeparator(color=COLOR_5, pad=(0,20))],

        [sg.Text("Masukkan gambar:", font=("Arial", 12),  text_color=COLOR_5,background_color=COLOR_2)],
        [sg.Input(key="-IMG_EKSTRAK_INPUT-",font=("Roboto", 12),size=(None,3),  
                enable_events=True,
                expand_x=True,
                background_color="white",
                text_color="black"),
        sg.FileBrowse("Pilih Gambar",
                    file_types=(("Images", "*.png *.bmp *.jpg"),),
                    target="-IMG_EKSTRAK_INPUT-",    # otomatis isi input dengan nama file
                    button_color=(sg.theme_text_color(), COLOR_5),
                    size=(15, 2),
                    pad=(5, 2))],

        # ✅ Tombol proses juga full lebar
        [sg.Button("Proses Ekstrak",key="-PROSESEKSTRAK-",button_color=(sg.theme_text_color(), COLOR_4),expand_x=True,pad=(5, 10),size=(None,3))],

        [sg.HorizontalSeparator(color=COLOR_5, pad=(0,20))],
        [sg.Text("Isi pesan teks:", text_color=COLOR_5,background_color=COLOR_2)],
        [sg.Multiline(key="-TEXT_HASIL-", background_color="white",size=(None, 6),expand_x=True, expand_y=False,disabled=True )]
    ]

    # --- footer ---
    footer_layout = [
        [sg.Text("© 2025 KEL 2 | UAS KRIPTOGRAFI", background_color=COLOR_2, text_color=COLOR_5,expand_x=True,justification="center")]
    ]


    # --- Layout utama (menu bar + konten dinamis) ---
    layout = [
        [sg.Column(menu_bar, expand_x=True,background_color=COLOR_2)],
        [
            sg.Column(home_layout, key="-PAGE_HOME-", expand_x=True, expand_y=True, element_justification="center",background_color=COLOR_2),
            sg.Column(embed_layout, visible=False, key="-PAGE_EMBED-", expand_x=True, expand_y=True, element_justification="center",background_color=COLOR_2),
            sg.Column(ekstraksi_layout, visible=False, key="-PAGE_EKSTRAK-", expand_x=True, expand_y=True, element_justification="center",background_color=COLOR_2),
        ],
        [sg.Frame("",footer_layout, expand_x=True, size=(None, 30), element_justification="center",background_color=COLOR_2)]
    ]

    return sg.Window("ROT13 & LSB", layout, size=(700, 600),background_color=BG_COLOR, finalize=True)


def run_app():
    window = create_window()

    # --- Fungsi bantu untuk ganti halaman ---
    def show_page(page_key):
        pages = ["-PAGE_HOME-", "-PAGE_EMBED-", "-PAGE_EKSTRAK-"]
        for p in pages:
            window[p].update(visible=(p == page_key))

    # --- Fungsi warna menu ---
    def highlight_button(active_key):
        for key in ["-HOME-", "-EMBED-", "-EKSTRAK-"]:
            if key == active_key:
                window[key].update(button_color=(sg.theme_text_color(), COLOR_5))
            else:
                window[key].update(button_color=(COLOR_5, COLOR_2))

    # --- Event Loop ---
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event in ("-HOME-", "-EMBED-", "-EKSTRAK-"):
            show_page({
                "-HOME-": "-PAGE_HOME-",
                "-EMBED-": "-PAGE_EMBED-",
                "-EKSTRAK-": "-PAGE_EKSTRAK-"
            }[event])
            highlight_button(event)
        
        if event == "-IMG_INPUT-":
            filename = values["-IMG_INPUT-"]
            if filename:
                try:
                    ext = os.path.splitext(filename)[1].lower()

                    image = Image.open(filename)
                    img_w, img_h = image.size

                    # ✅ Cek ukuran minimum
                    if img_w < 128 or img_h < 128:
                        sg.popup(f"Ukuran gambar terlalu kecil. Minimal 128x128px.\nSilakan pilih file lain.",title="Peringatan")
                        window.Element("-IMG_PREVIEW-").update(filename=None)
                        window.Element("-INFO-").update("❌ Gambar tidak valid")
                        continue
                    
                    # preview input gambar
                    max_size = (320, 320)
                    image.thumbnail(max_size, Image.Resampling.LANCZOS)
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    window["-IMG_PREVIEW-"].update(data=bio.getvalue())
                    window["-INFO-"].update(f"✅ Gambar valid: {img_w}x{img_h}px")
                    print("✅ Gambar valid, memproses thumbnail...")

                except Exception as e:
                    sg.popup_error(f"Gagal membuka gambar! Gambar terlalu Kecil")
                    window["-IMG_PREVIEW-"].update(filename=None)

        # --- EVENT PROSES EMBED ---
        if event == "-PROSES-":
            teks_pesan = values["-TEXT_INPUT-"].strip()
            Path_gambar = values["-IMG_INPUT-"]
                
            if not teks_pesan:
                sg.popup("Masukkan teks pesan terlebih dahulu!")
                continue
            
            if not Path_gambar:
                sg.popup("Pilih gambar terlebih dahulu!")
                continue
                    
            # Generate nama file dengan timestamp, simpan path 
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nama_file_output = f"Gambar_Embedded_{timestamp}.bmp"
            path_output = os.path.join("hasil", nama_file_output)
            
            try:
                berhasil, pesan_hasil = embed_pesan_lsb(Path_gambar, teks_pesan, path_output)
                
                if berhasil:
                    sg.popup_ok(
                        f"✅ PROSES EMBED BERHASIL!\n\n"
                        f"File disimpan sebagai:\n{nama_file_output}\n"
                        f"Di folder: {"hasil"}",
                        title="Sukses"
                    )
                else:
                    sg.popup_error(f"❌ GAGAL!\n{pesan_hasil}")
            
            except Exception as e:
                sg.popup_error(f"Error saat proses embed: {str(e)}")


        # --- EVENT PROSES EKSTRAK ---
        if event == "-PROSESEKSTRAK-":
            Path_gambar_ekstrak = values["-IMG_EKSTRAK_INPUT-"]
            
            if not Path_gambar_ekstrak:
                sg.popup_error("Pilih gambar terlebih dahulu!")
                continue
            
            # Proses ekstraksi
            berhasil, hasil_ekstrak = ekstrak_pesan_lsb(Path_gambar_ekstrak)
            
            if berhasil:
                window["-TEXT_HASIL-"].update(hasil_ekstrak)
                sg.popup_ok("Pesan berhasil diekstrak dan didekripsi!")
            else:
                window["-TEXT_HASIL-"].update("")
                sg.popup_error(f"Gagal mengekstrak pesan:\n{hasil_ekstrak}")

    window.close()