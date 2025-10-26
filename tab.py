import FreeSimpleGUI as sg

# # --- BAGIAN HEADER ---
# --- KONFIGURASI WARNA & UKURAN (bebas kamu ubah) ---
HEADER_BG =  "#FFFFFF"  # Biru
isi_header = [[
    sg.Text("KEL 2 - TI C 22", justification='left', expand_x=True, text_color="black",background_color='#FFFFFF'),
    sg.Text("ROT13 & STEGANOGRAFI LSB", font=("Any", 14, "bold"), text_color="black", justification='center', expand_x=True, background_color='#FFFFFF'),
    sg.Text("KRIPTOGRAFI", justification='right', expand_x=True, background_color='#FFFFFF', text_color="black"),
]]

layout = [
    [sg.Frame("", isi_header,size=(None, 35), background_color=HEADER_BG, border_width=0, expand_x=True, relief="flat",vertical_alignment='center')],
    [sg.TabGroup([[
        sg.Tab('Embeded', [
            [sg.Text('PENGATURAN APLIKASI', font=('Arial', 14, 'bold'))],
            [sg.HorizontalSeparator()],
            [sg.Frame('Plainteks', [
                [sg.Text('Pilih jenis plainteks:')],
                [sg.Radio('Upload file.txt','inputteks',  key='-FILETXT-'),sg.Radio('Ketik manual','inputteks', key='-MANUAL-')],
                # [sg.Checkbox('Tampilkan Notifikasi', key='-NOTIF-', default=True)],
                [sg.Text('Upload plainteks:')],
                [
                    sg.FileBrowse("Pilih file .txt", key="-BROWSE_TXT-", file_types=(("Text Files","*.txt"),)),
                    sg.Input(key="-TXT_FILE-", enable_events=True,size=(20, 1))
                ],
                [sg.Text('Ketikkan plainteks:')],
                [sg.Multiline("", size=(50, 5), key="-PLAINTEXT-", disabled=False)],
                [sg.Text('Ukuran Font:'), sg.Slider(range=(8, 24), default_value=12, orientation='h', key='-FONTSIZE-', expand_x=True)]
            ], expand_x=True)],
            [sg.Frame('Umum', [
                [sg.Text('Bahasa:'), sg.Combo(['Indonesia', 'English', 'Japanese'], default_value='Indonesia', key='-LANGUAGE-')],
                [sg.Text('Theme:'), sg.Combo(['System Default', 'Light', 'Dark', 'Blue'], default_value='System Default', key='-THEME-')]
            ], expand_x=True)],
            [sg.Button('Simpan Pengaturan', expand_x=True), sg.Button('Reset', expand_x=True)]
        ], expand_x=True, expand_y=True),
        
        sg.Tab('Ekstraksi', [
            [sg.Text('TENTANG APLIKASI', font=('Arial', 14, 'bold'))],
            [sg.HorizontalSeparator()],
            [sg.Multiline('Aplikasi Contoh dengan FreeSimpleGUI\n\n'
                         'Versi: 1.0.0\n'
                         'Dibuat dengan Python dan FreeSimpleGUI\n'
                         '© 2024 Contoh Company\n\n'
                         'Fitur:\n'
                         '• Dua tab full frame\n'
                         '• Responsive layout\n'
                         '• Mudah dikustomisasi',
                         size=(70, 15), 
                         expand_x=True, 
                         expand_y=True,
                         disabled=True)],
            [sg.Button('Website', expand_x=True), sg.Button('Bantuan', expand_x=True)]
        ], expand_x=True, expand_y=True),
        
        sg.Tab('Tentang', [
            [sg.Text('TENTANG APLIKASI', font=('Arial', 14, 'bold'))],
            [sg.HorizontalSeparator()],
            [sg.Multiline('Aplikasi Contoh dengan FreeSimpleGUI\n\n'
                         'Versi: 1.0.0\n'
                         'Dibuat dengan Python dan FreeSimpleGUI\n'
                         '© 2024 Contoh Company\n\n'
                         'Fitur:\n'
                         '• Dua tab full frame\n'
                         '• Responsive layout\n'
                         '• Mudah dikustomisasi',
                         size=(70, 15), 
                         expand_x=True, 
                         expand_y=True,
                         disabled=True)],
            [sg.Button('Website', expand_x=True), sg.Button('Bantuan', expand_x=True)]
        ], expand_x=True, expand_y=True)
    ]], expand_x=True, expand_y=True)]
]

window = sg.Window('Dua Tab - Settings & About', layout, resizable=True, finalize=True, size=(700, 500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Simpan Pengaturan':
        sg.popup('Pengaturan disimpan!', title='Sukses')
    elif event == 'Website':
        sg.popup('Membuka website...', title='Info')

window.close()