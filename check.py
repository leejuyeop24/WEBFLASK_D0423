import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib as ma
import torch
import torchvision
from importlib.metadata import version

print(f"pandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")
print(f"scikit-learn version: {sk.__version__}")
print(f"matplotlib version: {ma.__version__}")
print(f"torch version: {torch.__version__}")
print(f"torchvision version: {torchvision.__version__}")
print(f"flask version: {version('flask')}")
