#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Module pcm2d"""


import numpy as np
import scipy as sc
import pcm2d.optical_func as opt

class PcmStorage:
    """ A 2D PCM Storage has some properties:
    - a lenght 'length'
    - a width 'width'
    - an absorption coefficient for both solid and liquid phase 'kas' and 'kal'
    - a diffusion coefficient for both solid and liquid phase 'kds' and 'kdl'
    - an anisotropy factor of the Heyney-Greenstein sacattering function for both solad and liquid phase 'gs' and 'gl'
    - a refraction index for both solid and liquid phase 'ns' and 'nl'
    - a ratio liquid over solid 'ls_r' 
    - two phase solid ('phase' = 0) and liquid ('phase' = 1) """

    def __init__(self, width, length, kas, kal, kds, kdl, gs, gl, ns, nl, ls_r, phase):
        """ inititialisation function for pcm """
        self.width = width
        self.length = length
        self.kas = kas
        self.kal = kal
        self.kds = kds
        self.kdl = kdl
        self.gs = gs
        self.gl = gl
        self.ns = ns
        self.nl = nl
        self.ls_r = ls_r
        self.phase = phase

        
        
        self.vect = np.array([1., 0.], float)
        self.point_orig = np.array([0, width / 2.],float)
        self.point_end = np.zeros(2)

        self.front = self.ls_r * self.length
        self.points = np.array([0, width / 2.],float)
        
        self.khat = self.setKhat()
        
        



    def setKhat(self):
        """ set the null collision coef """
        return np.maximum(self.kas + self.kal, self.kal + self.kdl)




    def getPathLength(self):
        """ get a random path length """
        return - np.log(np.random.rand()) / self.khat


    def setRayEnd(self):
        self.point_end = self.point_orig + self.vect * self.pathLength
        print(self.pathLength)
        print (self.point_end)
    

    def intersectWithBoundary(self):
        """ compute intersection between a ray and the geometry """ 
        out_x = out_y = True
        length_x = length_y = self.length**2 + self.width**2
        if self.point_end[0] < 0:
            length_x = - self.point_orig[0] / self.vect[0]
            self.point_end[0] = 0
        elif self.point_end[0] > self.length :
            length_x = (self.length - self.point_orig[0]) / self.vect[0]
            self.point_end[0] = self.length
        else:
            out_x = False

        if self.point_end[1] < 0:
            length_y = - self.point_orig[1] / self.vect[1] 
            self.point_end[1] = 0
        elif self.point_end[1] > self.width :
            length_y = (self.width - self.point_orig[1]) / self.vect[1]
            self.point_end[1] = self.width
        else:
            out_y = False

        if not out_x and not out_y :
            return False
        elif length_x < length_y:
            self.pathLength = (self.point_end[0] - self.point_orig[0]) / self.vect[0]
        else:
            self.pathLength = (self.point_end[1] - self.point_orig[1]) / self.vect[1]

        self.setRayEnd()
        return True

    def getPhaseChange(self):
        length_x = self.length**2 + self.width**2
        changePhase = False
        
        if self.phase == 0 and self.point_end[0] > self.front:
            self.phase = 1
            length_x = (self.front - self.point_orig[0]) / self.vect[0]
            changePhase = True
        if self.phase == 1 and self.point_end[0] < self.front:
            self.phase = 0
            length_x = (self.front - self.point_orig[0]) / self.vect[0]
            changePhase = True
            
        if changePhase:
            self.pathLength = (self.front - self.point_orig[0]) / self.vect[0]
            self.setRayEnd()

    def getInteraction(self):
        pass
        

    def doPropagation(self):
        out_of_pcm = False
        
        while not out_of_pcm:
            self.pathLength = self.getPathLength()
            self.setRayEnd()
            out_of_pcm = self.intersectWithBoundary()
            if out_of_pcm:
                break
            self.getPhaseChange()
            print("phase  :", self.phase)
            self.point_orig = self.point_end

        print("sortie")
        
        
        return 0.
    






class Ray:
    """ 2D ray propagating inside the PCM """

    def __init__(self):
        pass
