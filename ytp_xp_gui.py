import PySimpleGUI as sg

# Windows XP-style color scheme
sg.theme('SystemDefault1')

editors = [
    "LolmanXD444", "ApproximateOstrich", "RaymanChrome",
    "EmilianoYTP", "AygoMedia"
]
vegas_versions = [
    "Vegas Pro 7", "Vegas Pro 8", "Vegas Pro 13", "Vegas Pro 14", "Vegas Pro 18"
]
styles = [
    "YTP Tennis", "Classic YTP", "Modern YTP", "Sentence Mixing", "Random Collage"
]
ofx_plugins = [
    "BCC Glitch", "Sapphire", "HitFilm Ignite", "Red Giant Universe", "None"
]
vst_plugins = [
    "IL Vocodex", "dBlue Glitch", "OTT", "CamelCrusher", "None"
]

layout = [
    [sg.Text('IL Vocodex Video Generator', font=('Tahoma', 16, 'bold'), text_color='blue')],
    [sg.Text('Select YTP Editor Style:'), sg.Combo(editors, default_value=editors[0], key='editor')],
    [sg.Text('Select Vegas Pro Version:'), sg.Combo(vegas_versions, default_value=vegas_versions[0], key='vegas')],
    [sg.Text('Select YTP Style:'), sg.Combo(styles, default_value=styles[0], key='style')],
    [sg.Text('OFX Plugins:'), sg.Combo(ofx_plugins, default_value=ofx_plugins[0], key='ofx')],
    [sg.Text('VST Plugins:'), sg.Combo(vst_plugins, default_value=vst_plugins[0], key='vst')],
    [sg.HorizontalSeparator()],
    [sg.Button('Generate', size=(10, 1)), sg.Button('Exit', size=(10, 1))]
]

window = sg.Window('IL Vocodex Video Generator - Windows XP Edition', layout, icon=None, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Generate':
        sg.popup(
            'Generation Complete!',
            f"Editor Style: {values['editor']}\n"
            f"Vegas Pro Version: {values['vegas']}\n"
            f"YTP Style: {values['style']}\n"
            f"OFX Plugin: {values['ofx']}\n"
            f"VST Plugin: {values['vst']}\n",
            title='Success',
            keep_on_top=True
        )

window.close()