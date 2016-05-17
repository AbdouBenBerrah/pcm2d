#-*- coding: utf-8 -*-

from pcm2d.pcm2d import heyney_greenstein
from pcm2d.pcm2d import snell_descartes

from pcm2d.pcm2d import PcmStorage

import numpy as np
from numpy.testing import assert_array_equal

def test_heyney_greenstein():
    assert heyney_greenstein(0, 0.5) == 0.5

def test_heyney_greenstein_2():
    assert heyney_greenstein(0.5, 0.5) == 0.5

def test_snell_descartes():
    theta = np.array([[np.pi/2],[np.pi/2]])
    normal = np.array([[1],[0]])
    n1 = 1.
    n2 = 1.
    assert_array_equal(snell_descartes(n1, n2, normal, theta), np.array([[np.pi/2],[np.pi/2]]))



    

    
