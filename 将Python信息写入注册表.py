import sys
from winreg import *

# tweak as necessary
version = sys.version[:3]
install_path = sys.prefix

reg_path = "SOFTWARE\\Python\\Pythoncore\\%s\\" % (version)
install_key = "InstallPath"
python_key = "PythonPath"
python_path = "%s;%s\\Lib\\;%s\\DLLs\\" % (
    install_path, install_path, install_path
)


def register_python():
    try:
        reg = OpenKey(HKEY_CURRENT_USER, reg_path)
    except EnvironmentError as e:
        try:
            reg = CreateKey(HKEY_CURRENT_USER, reg_path)
            SetValue(reg, install_key, REG_SZ, install_path)
            SetValue(reg, python_key, REG_SZ, python_path)
            CloseKey(reg)
        except:
            print("*** Unable to register!")
            return
        print(" Python", version, "is now registered!")
        return
    if QueryValue(reg, install_key) == install_path and QueryValue(reg, python_key) == python_path:
        CloseKey(reg)
        print("=== Python", version, "is already registered!")
        return
    CloseKey(reg)
    print("*** Unable to register!")
    print("*** You probably have another Python installation!")


if __name__ == "__main__":
    register_python()