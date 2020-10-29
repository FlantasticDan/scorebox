# Hack to add the GUI folder to the path to allow Qt Resources to import properly
# from uic generated ui.py files.

import sys
import os
sys.path.append(os.path.join(sys.path[0], "GUI"))