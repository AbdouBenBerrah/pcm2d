#-*- coding: utf-8 -*-

"""Module for scattering and refraction function"""

import numpy as np
import scipy as sc




def heyney_greenstein(g, s):
    """This function compute the Heyney-Greenstein scattering function and
    returns a diffusion direction with respect to the anisotropy factor g 
    and to a random number"""
    if g == 0:
        return 2 * s - 1
    else:
        return (1 + g**2 - ((1 - g**2)/(1 + g * (2 * s - 1)))** 2 ) / ( 2 * g)



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
