"""
  Has three functions, one for single slit diffraction intensity, one for double slit diffraction intensity and one for diffraction grating.
  The functions are named single_slit_diffraction_intensity, double_slit_diffraction_intensity and grated_diffraction_intensity
"""
import numpy as np
# single slit diffraction
def single_slit_diffraction_intensity (slit_width, wavelength, screen_distance, X):
  """
    Takes in slit_width, wavelength, screen distance and a numpy array X(an array of distances from the center).
    Outputs an array of normalized intensities corresponding to X.
  """
  return ((np.sin((np.pi*slit_width*X)/(wavelength*screen_distance)))/((np.pi*slit_width*X)/(wavelength*screen_distance)))**2

def double_slit_diffraction_intensity (slit_width, wavelength, screen_distance, distance_between_slits,  X) :
  """
    Takes in slit_width, wavelength, screen distance, distance between the two strings and a numpy array X(an array of distances from the center).
    Outputs an array of normalized intensities corresponding to X.
  """
  return (((np.sin((np.pi*slit_width*X)/(wavelength*screen_distance)))/((np.pi*slit_width*X)/(wavelength*screen_distance)))**2)*((np.cos((np.pi*distance_between_slits*X)/(wavelength*screen_distance)))**2)

def grated_diffraction_intensity (slit_width, wavelength, screen_distance, distance_between_slits, number_of_slits, X):
  """
    Takes in slit_width, wavelength, screen distance, distance between the two strings, the total number of slits and a numpy array X(an array of distances from the center).
    Outputs an array of normalized intensities corresponding to X.
  """  
  term1 = np.sin(np.pi*X*slit_width/(wavelength*screen_distance))/(np.pi*X*slit_width/(wavelength*screen_distance))
  term2 = (np.sin(number_of_slits*np.pi*distance_between_slits*X/(wavelength*screen_distance)))/(number_of_slits*np.sin((np.pi*distance_between_slits*X)/(wavelength*screen_distance)))
  return (term1**2)*(term2**2)