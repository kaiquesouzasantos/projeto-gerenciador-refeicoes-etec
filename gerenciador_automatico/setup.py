import cx_Freeze
import sys

base = "Win32GUI" if sys.platform == "win32" else None
executables = [cx_Freeze.Executable('main.py', base = base)]

cx_Freeze.setup(
    name="Sistema de Controle da Etec",
    options={'build_exe':
                 {
                    'packages': ['tkinter','tk', 'time', 'customtkinter', 'datetime', 'hashlib', 'os', 'pyqrcode', 'threading', 'imghdr', 'smtplib', 'email', 'pyzbar'],
                    'include_files': [
                        'assets'
                    ]
                 }
    },
    executables=executables
)