#-*- coding: utf-8 -*-

from pcm2d.pcm2d import heyney_greenstein


def test_heyney_greenstein():
    assert heyney_greenstein(0, 0.5) == 0.5

def test_heyney_greenstein_2():
    assert heyney_greenstein(0.5, 0.5) == 0.5
