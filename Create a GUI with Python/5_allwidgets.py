import PySimpleGUIQt as s

thelayout = [
    [s.Text('Widgets!', size=(60, 1), font=("Helvetica", 20))],
    [s.Text('To enter text...')],
    [s.InputText('This is my text')],
    [s.Checkbox('A checkbox!')],
    [s.Radio('A radiobutton', "RADIO1", default=True)],
    [s.Multiline(default_text='A multi-line text widget', size=(35, 3)),
     s.Multiline(default_text='Another multi-line', size=(35, 3))],
    [s.InputCombo(('Combobox 1', 'Combobox 2', 'Combobox 3'), size=(20, 3)),
     s.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [s.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
     s.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
     s.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
     s.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10)],
    [s.Text('_'  * 80)],
    [s.Text('Choose A Folder', size=(35, 1))],
    [s.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
     s.InputText('Default Folder'), s.FolderBrowse()],
    [s.Submit(), s.Cancel()]
     ]

window = s.Window(title="Example Widgets", size=(640,480), layout=thelayout)
button, values = window.read()
s.popup(button, values)
