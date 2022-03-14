from matplotlib import cm
from fileinput import filename
import iges
from geomdl.visualization import VisMPL
from geomdl import operations
from geomdl import exchange
import numpy as np


file = iges.read('teste4.igs')

surfaces = file.bspline_surfaces()

surface0 = surfaces[0]

surf = surface0.to_geomdl()

cps = surf.ctrlpts2d
for cp in cps:
    for c in cp:
        print(c)

print("\n\nAPÓS REFINAMENTO:\n\n")

operations.refine_knotvector(surf, [1, 0])

cps = surf.ctrlpts2d
for cp in cps:
    for c in cp:
        print(c)

print("\n\nCOORDENADAS REAIS DOS PONTOS:\n\n")

cps = surf.ctrlpts
for cp in cps:
    print(cp)
