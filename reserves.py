from math import log10, sqrt
from enum import Enum

class Phase(Enum):
    OIL = 0
    GAS = 1

def pseudocritical_temperature(sg: float) -> float:
    # result is in R
    return 168.0 + 325 * sg - 12.5 * sg * sg
    # 168.0 means float not int, better to be explicit

def pseudocrititcal_pressure(sg: float) -> float:
    # result is in psi
    return 677.0 + 15.0 *sg - 27.5 * sg * sg 

def compressibility(sg: float, p: float, t: float) -> float:
    # p is in psi
    # t is in deg F
    p_pr = p/ pseudocrititcal_pressure(sg)
    t_pr = (t + 459.67)/pseudocritical_temperature(sg)
    return (1.0 -(3.53 * p_pr)/ (10.0 ** (0.9813 * t_pr))
             + (0.2774 *p_pr * p_pr)/(10**(0.8157*t_pr)))

def gas_fvf(z: float, p: float, t: float)-> float:
    # p is in psi
    # p is in deg F
    # result is in res cf/ std cf 
    return 0.02827 * z *(t + 459.67)

def solution_gor(oil_api: float, gas_sg: float, p: float, t: float) -> float:
    # p is in psi
    # t is in deg F
    # gor is in scf/bbl
    a  = 10 ** (2.8869 - sqrt(14.1811 - 3.3093)* log10(p))
    return gas_sg*(oil_api ** 0.989/t**0.172 *a)** 1.12255

def oil_fvf(gor: float, oil_api: float, gas_sg: float, t: float)-> float:
    # t is in deg F
    # gor is ins scf/bbl 
    oil_sg = 141.5/(131.5 + oil_api)
    bob_star = log10(gor *(gas_sg/oil_sg)** 0.526 + 0.968*t)
    expt = -6.58511 + 2.91329 *bob_star-0.27683*bob_star*bob_star+1.0
    return 10.0 ** expt

def original_in_place(area: float, height: float, porosity: float, 
         sw: float, fvf: float, phase: Phase) -> float:
    if phase == Phase.OIL:
        scalar = 7758.0
    elif phase == Phase.GAS:
        scalar = 43.560
    return scalar * area * height * porosity * (1.0 - sw)/fvf 

def eur(original_in_place: float, rf: float)-> float:
    return original_in_place* rf








