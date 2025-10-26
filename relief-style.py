import FreeSimpleGUI as sg

layout = [
    [sg.Text("Perbandingan Relief Styles:")],
    [sg.Frame("relief='flat'", [[sg.Text("Tidak ada border")]], relief="flat")],
    [sg.Frame("relief='raised'", [[sg.Text("Border timbul")]], relief="raised")],
    [sg.Frame("relief='sunken'", [[sg.Text("Border tenggelam")]], relief="sunken")],
    [sg.Frame("relief='groove'", [[sg.Text("Border groove")]], relief="groove")],
    [sg.Frame("relief='ridge'", [[sg.Text("Border ridge")]], relief="ridge")],
]

window = sg.Window('Relief Styles', layout)
window.read()
window.close()