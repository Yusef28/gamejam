import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pygame"], 
"excludes": ["tkinter"], 
"include_files":["images/","music/", "sfx/"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(  name = "TestSpiele",
		version = "0.0.1",
		description = "Meine Teste Spiele!",
		options = {"build_exe": build_exe_options},
		executables = [Executable("__main__.py", base=base)])