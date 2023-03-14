import cx_Freeze

executables = [cx_Freeze.Executable('main.py', base = "Win32GUI")]

cx_Freeze.setup(
    name="Sistema de Controle da Etec",
    options={'build_exe':
                 {
                    'packages': ['tkinter', 'customtkinter', 'datetime', 'hashlib', 'os', 'pyqrcode', 'threading'],
                    'include_files': [
                        'assets'
                    ]
                 }
    },
    executables=executables
)