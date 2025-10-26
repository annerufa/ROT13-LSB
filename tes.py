import FreeSimpleGUI as sg

# --- KONFIGURASI WARNA & UKURAN (bebas kamu ubah) ---
HEADER_BG =  "#FFFFFF"  # Biru
CONTENT_BG = "#F5F5F5"  # Abu muda
FOOTER_BG = "#424242"   # Abu gelap

WINDOW_SIZE = (700, 550)

HEADER_HEIGHT = 50
FOOTER_HEIGHT = 30

# Lebar masing-masing kolom di header (dalam proporsi, bukan pixel)
HEADER_COL_WIDTHS = [0.2, 0.6, 0.2]  # 30%, 40%, 30%


# --- BAGIAN HEADER ---
header_layout = [
    [
        sg.Column(
            [[sg.Text("KEL 2 - TI C 22", background_color=HEADER_BG, text_color="black")]],
            background_color=HEADER_BG,
            element_justification="left",
            key="-HEADER_LEFT-",
            expand_x=True,
            pad=(0, 0)
        ),
        sg.Column(
            [[sg.Text("ROT13 & STEGANOGRAFI LSB", background_color=HEADER_BG, text_color="black", font=("Any", 16, "bold"))]],
            background_color=HEADER_BG,
            element_justification="center",
            key="-HEADER_CENTER-",
            expand_x=True,
            pad=(0, 0)
        ),
        sg.Column(
            [[sg.Text("KRIPTOGRAFI", background_color=HEADER_BG, text_color="black", justification="right")]],
            background_color=HEADER_BG,
            element_justification="right",
            vertical_alignment="center",
            key="-HEADER_RIGHT-",
            expand_x=True,
            pad=(0, 0)
        ),
    ]
]

# --- BAGIAN CONTENT ---
# Lebar masing-masing kolom di header (dalam proporsi, bukan pixel)
CONTENT_COL_WIDTHS = [0.6, 0.4]  # 30%, 40%, 30%
content_layout = [
    [
        sg.Column(
            [sg.Frame("Preview Gambar", [[sg.Image(key="-IMAGE-", size=(420,470))]])]

            # [[sg.Text("KEL 2 - TI C 22", background_color=HEADER_BG, text_color="black")]],
            # background_color=HEADER_BG,
            # element_justification="left",
            # key="-HEADER_LEFT-",
            # expand_x=True,
            # pad=(0, 0)
        ),
        sg.Column(
            [[sg.Text("🔐ROT13 & STEGANOGRAFI LSB", background_color=HEADER_BG, text_color="black", font=("Any", 18, "bold"))]],
            background_color=HEADER_BG,
            element_justification="center",
            key="-HEADER_CENTER-",
            expand_x=True,
            pad=(0, 0)
        ),
    ]
    # [sg.Text("Ini area konten utama", background_color=CONTENT_BG, font=("Any", 14))],
    # [sg.Multiline(size=(70, 15), background_color="white", text_color="black", key="-CONTENT-")]
]

# --- BAGIAN FOOTER ---
footer_layout = [
    [sg.Text("© 2025 UAS KRIPTOGRAFI | KEL 2", background_color=FOOTER_BG, text_color="white", justification="center", expand_x=True)]
]


# --- SUSUN SEMUA FRAME ---
layout = [
    [sg.Frame("", header_layout, size=(None, HEADER_HEIGHT), background_color=HEADER_BG, pad=(0, 0), expand_x=True)],
    [sg.Frame("", content_layout, background_color=CONTENT_BG, pad=(0, 0), expand_x=True, expand_y=True)],
    [sg.Frame("", footer_layout, size=(None, FOOTER_HEIGHT), background_color=FOOTER_BG, pad=(0, 0), expand_x=True)],
]

# --- BUAT WINDOW ---
window = sg.Window(
    "UAS KRIPTOGRAFI - KEL 2",
    layout,
    size=WINDOW_SIZE,
    resizable=True,
    finalize=True,
    background_color="#E7E7E7",
)

# --- LOOP UTAMA ---
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
