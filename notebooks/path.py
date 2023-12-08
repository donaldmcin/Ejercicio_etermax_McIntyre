import os
from pathlib import Path

# path del proyecto
MAIN_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent

# path data
DATA_PATH = os.path.join(MAIN_PATH,'corpus')