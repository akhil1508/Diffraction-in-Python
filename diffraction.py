
import numpy as np
# single slit diffraction
def single_slit_diffraction_intensity (slit_width, wavelength, screen_distance, X):
  return ((np.sin((np.pi*slit_width*X)/(wavelength*screen_distance)))/((np.pi*slit_width*X)/(wavelength*screen_distance)))**2

def double_slit_diffraction_intensity (slit_width, wavelength, screen_distance, distance_between_slits,  X) :
  return (((np.sin((np.pi*slit_width*X)/(wavelength*screen_distance)))/((np.pi*slit_width*X)/(wavelength*screen_distance)))**2)*((np.cos((np.pi*distance_between_slits*X)/(wavelength*screen_distance)))**2)

def grated_diffraction_intensity (slit_width, wavelength, screen_distance, distance_between_slits, number_of_slits, X):
    return (((np.sin((np.pi*slit_width*X)/(wavelength*screen_distance)))/((np.pi*slit_width*X)/(wavelength*screen_distance)))**2)*((np.sin((number_of_slits*np.pi*distance_between_slits*X)/(wavelength*screen_distance))/(number_of_slits*np.sin((np.pi*distance_between_slits*X)/(wavelength*screen_distance))))**2)
