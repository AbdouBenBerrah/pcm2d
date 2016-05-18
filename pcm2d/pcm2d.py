#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Module pcm2d"""


import numpy as np
import scipy as sc
import pcm2d.optical_func as opt

class PcmStorage:
    """A 2D PCM Storage has some properties:
    - a lenght 'length'
    - a width 'width'
    - an absorption coefficient for both solid and liquid phase 'kas' and 'kal'
    - a diffusion coefficient for both solid and liquid phase 'kds' and 'kdl'
    - an anisotropy factor of the Heyney-Greenstein sacattering function for both solad and liquid phase 'gs' and 'gl'
    - a refraction index for both solid and liquid phase 'ns' and 'nl'
    - a ratio liquid over solid 'ls_r' """

    def __init__(self, width, length, kas, kal, kds, kdl, gs, gl, ns, nl, ls_r):
        """ inititialisation function for pcm """
        self.width = width
        self.length = length
        self.kas = kas
        self.kad = kal
        self.kds = kds
        self.kdl = kdl
        self.gs = gs
        self.gl = gl
        self.ns = ns
        self.nl = nl
        self.ls_r = ls_r

        self.vect = np.array([1., 0.], float)
        
        self.points = np.empty([0, width / 2.],float)
        
        self.khat = self.setKhat(kas, kds, kal, kdl)

        



    def setKhat(self, kas, kds, kal, kdl):
        """ set the null collision coef """
        
        return np.maximum(kas + kal,kal + kdl)





    








    
