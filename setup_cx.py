# what you want to application to be called
application_title = "Lat2Cyr"
# the name of the python file you use to run the program
main_python_file = "main.py"

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["os", "sys", "codecs", "lat2cyr"]
packages = ['lat2cyr']

setup(
        name = application_title,
        version = "0.1",
        description = "Sample cx_Freeze PyQt4 script",
        options = {"build_exe" : {"includes" : includes, "packages" : packages },
                   "bdist_mac" : {"iconfile" : "lat2cyr.icns",
                                  "bundle_name" : "Lat2Cyr"}},
        executables = [Executable(main_python_file, base = base)])
