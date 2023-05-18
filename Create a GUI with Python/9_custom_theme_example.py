import PySimpleGUIQt as sg

# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#ffcc00',
                                        'TEXT': 'black',
                                        'INPUT': 'white',
                                        'TEXT_INPUT': 'black',
                                        'SCROLL': 'gray',
                                        'BUTTON': ('white', '#ff3333'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
# Switch to use your newly created theme
sg.theme('MyNewTheme')
# Call a popup to show what the theme looks like
sg.popup_get_text('Hello world')