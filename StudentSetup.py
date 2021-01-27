import sys
from cx_Freeze import *
includefiles = ['college.ico']
excludes = []
packages = []
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table = [
    ('DesktopShortcut',                                     # Shortcut
     'DesktopFolder',                                       # Directory_
     'StudentManagementSystem',                             # Name
     'TARGETDIR',                                           # Component_
     '[TARGETDIR]\StudentManagementSystem.exe',             # Target
     None,                                                  # Arguments
     None,                                                  # Description
     None,                                                  # Hotkey
     None,                                                  # Icon
     None,                                                  # IconIndex
     None,                                                  # ShowCmd
     'TARGETDIR',                                           # WKDir
     )
]

msi_data = {'Shortcut': shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version='0.1',
    description='Student Management System Developed By Himanshu Sharma',
    author='Himanshu Sharma',
    name='Student Management System',
    options={'build_exe': {'include_files': includefiles}, 'bdist_msi': bdist_msi_options, },
    executables=[
        Executable(
            script="StudentManagementSystem.py",
            base=base,
            icon='college.ico',
        )
    ]
)
