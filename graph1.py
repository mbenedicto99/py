import matplotlib
%matplotlib inline
%config InlineBackend.figure_formats = ["svg"]
import cantera as ct
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 120

print(f"Using Cantera version: {ct._version_}")