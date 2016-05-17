#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Module pcm2d"""


import numpy as np
import scipy as sc

def heyney_greenstein(g, s):
    """This function compute the Heyney-Greenstein scattering function and
    returns a diffusion direction with respect to the anisotropy factor g 
    and to a random number"""
    if g == 0:
        return s
    else:
        return (1 + g * g - ((1 - g * g)/(1 + g * (2 * s - 1)))) / ( 2 * g)

class PcmStorage:
    """A 2D PCM Storage has some properties:
    - a lenght 'length'
    - a width 'width'
    - an absorption coefficient for both solid and liquid phase 'kas' and 'kal'
    - a diffusion coefficient for both solid and liquid phase 'kds' and 'kdl'
    - an anisotropy factor of the Heyney-Greenstein sacattering function for both solad and liquid phase 'gs' and 'gl'
    - """

    def __init__(self):
        """ inititialisation function for pcm """
    












    
