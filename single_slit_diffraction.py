import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from diffraction import single_slit_diffraction_intensity

X = np.arange(-0.005,0.005,0.00001)

wavelength = 500*(10**-9)
slit_width = 100*(10**-6)
screen_distance = 50*(10**-2)

Y = single_slit_diffraction_intensity(slit_width, wavelength, screen_distance, X)

plot, = plt.plot(X,Y)
plt.xlabel("Distance from center")
plt.ylabel("Intensity")
axis=(plt.axes([0.75, 0.75, 0.14, 0.05]))
axis2 = (plt.axes([0.75,0.65, 0.14, 0.05]))
axis3 = (plt.axes([0.75,0.55, 0.14, 0.05]))

wavelength_slider = Slider(axis,'Wavelength(nm)',100, 1000,valinit=wavelength*10**9)
slit_width_slider = Slider(axis2, "Slit Width(micrometers)", 10, 1000, valinit=slit_width*10**6)
screen_distance_slider = Slider(axis3, "Screen Distance(cm)", 10, 100, valinit= screen_distance*10**2)


def update(val) :
  wavelength = wavelength_slider.val*(10**-9)
  slit_width = slit_width_slider.val*(10**-6)
  screen_distance = screen_distance_slider.val*(10**-2)
  Y = single_slit_diffraction_intensity(slit_width, wavelength, screen_distance, X)
  plot.set_ydata(Y)

wavelength_slider.on_changed(update)
slit_width_slider.on_changed(update)
screen_distance_slider.on_changed(update)

plt.show()