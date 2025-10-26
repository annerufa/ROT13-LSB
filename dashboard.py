# dashboard.py
import FreeSimpleGUI as sg
from metode import rot13, stego_embed, stego_extract

def create_window():
    sg.theme("Material2")

    # ====== Header ======
    header_frame = [
        [sg.Text("🔐 Aplikasi Enkripsi & Steganografi", font=("Segoe UI", 14, "bold"))],
        [sg.HorizontalSeparator()]
    ]

    # ====== Frame Embed ======
    embed_frame = [
        [sg.Text("Pilih metode input teks:")],
        [
            sg.Radio("Input manual", "INPUT_MODE", True, key="-MODE_MANUAL-", enable_events=True),
            sg.Radio("Upload file .txt", "INPUT_MODE", key="-MODE_FILE-", enable_events=True)
        ],
        [
            sg.Multiline("Masukkan teks...", size=(50, 5), key="-PLAINTEXT-", text_color="gray", disabled=False)
        ],
        [
            sg.Input(key="-TXT_FILE-", visible=False, enable_events=True),
            sg.FileBrowse("Pilih file .txt", key="-BROWSE_TXT-", file_types=(("Text Files","*.txt"),), visible=False)
        ],
        [sg.Text("Pilih gambar carrier:")],
        [
            sg.Input(key="-IMG_FILE-", enable_events=True),
            sg.FileBrowse("Pilih Gambar", file_types=(("Images", "*.png *.bmp"),))
            # sg.FileBrowse("Pilih Gambar", file_types=(("Images","*.png;*.bmp","*.png;*.bmp"),))
        ],
        [sg.Image(key="-PREVIEW-", size=(200, 200))],
        [sg.Button("Embed", key="-EMBED-"), sg.Button("Reset", key="-RESET1-")],
        [sg.Text("", key="-STATUS1-", text_color="green")]
    ]

    # ====== Frame Extract ======
    extract_frame = [
        [sg.Text("Pilih gambar yang mengandung pesan:")],
        [
            sg.Input(key="-IMG_EXTRACT-", enable_events=True),
            sg.FileBrowse("Pilih Gambar", file_types=(("Images", "*.png *.bmp"),))
            # sg.FileBrowse("Pilih Gambar", file_types=(("Images","*.png;*.bmp","*.png;*.bmp"),))
        ],
        [sg.Image(key="-PREVIEW_EXTRACT-", size=(200, 200))],
        [sg.Button("Ekstrak", key="-EXTRACT-"), sg.Button("Reset", key="-RESET2-")],
        [sg.Multiline(size=(50,5), key="-OUTPUT-", disabled=True)],
        [sg.Text("", key="-STATUS2-", text_color="green")]
    ]

    layout = [
        [sg.Frame("", header_frame, expand_x=True, relief="flat", pad=(0,5))],
        [sg.TabGroup([[sg.Tab("Embed", embed_frame), sg.Tab("Ekstraksi", extract_frame)]])]
    ]

    return sg.Window("Aplikasi Enkripsi & Steganografi", layout, size=(520,560), finalize=True)

def run_app():
    window = create_window()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        # ==== Placeholder behaviour untuk Multiline ====
        if event == "-PLAINTEXT-":
            if values["-PLAINTEXT-"] == "Masukkan teks...":
                window["-PLAINTEXT-"].update("", text_color="black")

        # ==== Radio button ====
        if event in ("-MODE_MANUAL-", "-MODE_FILE-"):
            manual = values["-MODE_MANUAL-"]
            window["-PLAINTEXT-"].update(visible=manual, disabled=not manual)
            window["-BROWSE_TXT-"].update(visible=not manual)
            window["-TXT_FILE-"].update(visible=not manual)

        # ==== Preview gambar ====
        if event in ("-IMG_FILE-", "-IMG_EXTRACT-"):
            try:
                img_key = "-PREVIEW-" if event == "-IMG_FILE-" else "-PREVIEW_EXTRACT-"
                window[img_key].update(filename=values[event])
            except Exception:
                pass

        # ==== Embed ====
        elif event == "-EMBED-":
            if values["-MODE_FILE-"] and values["-TXT_FILE-"]:
                with open(values["-TXT_FILE-"], "r", encoding="utf-8") as f:
                    text_data = f.read()
            else:
                text_data = values["-PLAINTEXT-"]
                if text_data.strip() == "Masukkan teks...":
                    text_data = ""

            if not text_data.strip():
                window["-STATUS1-"].update("⚠️ Teks kosong!", text_color="red")
                continue
            if not values["-IMG_FILE-"]:
                window["-STATUS1-"].update("⚠️ Gambar belum dipilih!", text_color="red")
                continue

            cipher = rot13(text_data)
            stego_embed(values["-IMG_FILE-"], cipher, "output.png")
            window["-STATUS1-"].update("✅ Pesan disisipkan (output.png)", text_color="green")

        # ==== Ekstraksi ====
        elif event == "-EXTRACT-":
            if not values["-IMG_EXTRACT-"]:
                window["-STATUS2-"].update("⚠️ Gambar belum dipilih!", text_color="red")
                continue

            hidden = stego_extract(values["-IMG_EXTRACT-"])
            plain = rot13(hidden)
            window["-OUTPUT-"].update(plain)
            window["-STATUS2-"].update("✅ Pesan berhasil diekstrak!", text_color="green")

        # ==== Reset tombol ====
        elif event in ("-RESET1-", "-RESET2-"):
            for key in ("-PLAINTEXT-", "-TXT_FILE-", "-IMG_FILE-", "-IMG_EXTRACT-", "-OUTPUT-"):
                if key in window.AllKeysDict:
                    if key == "-PLAINTEXT-":
                        window[key].update("Masukkan teks...", text_color="gray")
                    else:
                        window[key].update("")
            for key in ("-STATUS1-", "-STATUS2-", "-PREVIEW-", "-PREVIEW_EXTRACT-"):
                if key in window.AllKeysDict:
                    window[key].update("")

    window.close()
