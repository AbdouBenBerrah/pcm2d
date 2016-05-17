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
        return (1 + g**2 - ((1 - g**2)/(1 + g * (2 * s - 1)))) / ( 2 * g)



def snell_descartes(n1, n2, normal, theta1):    
    """This function compute the Snells-Descartes law for a refraction and
    returns a refraction direction with respect to the refractive index of both material, 
    the incident direction and the normal at the interface"""
    theta2 = np.array([[0],[0]])
    n1_n2 = n1 / n2
    cosTheta1 = normal[0] * (- theta1[0]) + normal[1] * (- theta1[1])
    cosTheta2 = sc.sqrt(1 - (n1_n2**2) * (1 - cosTheta1**2))
    if cosTheta2 < 0:
        theta2 = theta1 + (2 * cosTheta1) * normal
    else:
        theta2 = n1_n2 * theta1 + (n1_n2 * cosTheta1 + cosTheta2) * normal
    return theta2


    

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

        self.khat = self.setKhat(kas, kds, kal, kdl)




    def setKhat(self, kas, kds, kal, kdl):
        """ set the null collision coef """
        
        return np.maximum(kas + kal,kal + kdl)
        

    









    
