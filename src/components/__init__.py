# This brings every function in every Python file in the components folder into
# the components namespace

import sys
import os

# Add the directory containing components/ to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import importlib

# Get the directory path of the current file (__init__.py)
current_dir = os.path.dirname(__file__)

# Automatically import all Python files (except __init__.py)
__all__ = []
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        # Remove the .py extension to get the module name
        module_name = filename[:-3]
        module = importlib.import_module(f"components.{module_name}")
        
        # Dynamically add all public members of the module to the namespace
        for attr in dir(module):
            if not attr.startswith("_"):  # Skip private members
                globals()[attr] = getattr(module, attr)
                __all__.append(attr)
