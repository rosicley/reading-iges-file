from matplotlib import cm
from fileinput import filename
import iges
from geomdl.visualization import VisMPL
from geomdl import operations
from geomdl import exchange
from geomdl import helpers
import numpy as np


file = iges.read('teste4.igs')

ent = file.entities()
print(ent)
# # for e in ent:
# #     print(e)

# new_column = np.array([3, 6])
# print(new_column.shape)
# new_column = np.array(new_column)
# print(new_column.shape)


surfaces = file.bspline_surfaces()

surface0 = surfaces[0]

# print(surface0.control_points())

surf = surface0.to_geomdl()

# operations.refine_knotvector(surf, [1, 0])

# surf.co

# # Set evaluation delta
# surf.delta = 0.025
exchange.export_json(surf, 'file1.json')
# # operations.refine_knotvector(surf, [1, 0])
# exchange.export_json(surf,'file2.json')


# # Evaluate surface points
surf.evaluate()

# # Import and use Matplotlib's colormaps

# Plot the control points grid and the evaluated surface
surf.vis = VisMPL.VisSurface()
surf.render(colormap=cm.cool)


# # cps = surface0.control_points()

# curves = file.bsplines()

# # for curve in curves:
# #     print(len(curves.))

print(surf.knotvector_u)
operations.refine_knotvector(surf, [1, 0])
print(surf.knotvector_u)

surf.render(colormap=cm.cool)


