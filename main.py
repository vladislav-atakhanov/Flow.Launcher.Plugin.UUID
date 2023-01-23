import sys
from pathlib import Path


parent_folder_path = Path(__file__).absolute().parent
LIB = parent_folder_path / "env" / "Lib" / "site-packages"

# Flow.Launcher.Plugin.UuidGenerator
sys.path.append(str(parent_folder_path))
sys.path.append(str(LIB))
sys.path.append(str(parent_folder_path / "plugin"))


from plugin import UuidPlugin

if __name__ == "__main__":
    UuidPlugin()
