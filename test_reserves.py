# test are taken from exercises in "EOS in PVT analysis" by Tarek Ahmed

from pytest import approx 
# helps for checking equality not exactly but close enough 
from reserves import *

def test_tpc():
    assert pseudocritical_temperature(0.699)==approx(389.1, abs = 0.1)

def test_ppc():
    assert pseudocrititcal_pressure(0.699)==approx(669.2, abs = 0.1)

def test_z():
    assert compressibility(0.699, 3000, 640.0 - 459.67) == approx(0.824, abs = 0.1)

def test_gas_fvf():
    assert 1.0/ gas_fvf(0.78, 2000.0, 600.0 - 459.67) == approx(151.15, abs = 0.1)

def test_solution_gor():
    assert solution_gor(47.1, 0.851, 2377.0 + 14.7, 250.0) == approx(737.0, abs = 1.0)
    assert solution_gor(48.6, 0.911, 2051.0 + 14.7, 260.0) == approx(686.0, abs = 1.0)

def test_oil_fvf():
    assert oil_fvf(751.0, 47.1, 0.851, 250.0) == approx(1.473, abs = 0.001)
    assert oil_fvf(693.0, 48.6, 0.911, 260.0) == approx(1.461, abs = 0.001)