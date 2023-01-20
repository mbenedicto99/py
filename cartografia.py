from pygris import counties
import matplotlib.pyplot as plt

# Get the default TIGER/Line file for counties in Michigan
mi_tiger = counties(state = "NY", cache = True)

# Get the cartographic boundary file with cb = True
mi_cartographic = counties(state = "NY", cb = True, cache = True)

# Plot the two side-by-side to compare them
fig, ax = plt.subplots(ncols = 2)
mi_tiger.plot(ax = ax[0])
mi_cartographic.plot(ax = ax[1])

ax[0].set_title("TIGER/Line")
ax[1].set_title("Cartographic")