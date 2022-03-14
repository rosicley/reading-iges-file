from geomdl import exchange
from geomdl import multi
from geomdl.visualization import VisMPL as vis
from geomdl import construct
from geomdl import operations
from geomdl import exchange_vtk



# Import converted data
data = exchange.import_json("testeMulti.json")

# Add the imported data to a surface container
surf_cont = multi.SurfaceContainer(data)
surf_cont.sample_size = 30

for surface in data:
    print(surface.cpsize)

print(type(data))

# pvolume = construct.construct_volume(
#     'w', data[0], data[1], data[2], data[3], data[4], degree=3)
# print(pvolume.knotvector_w)

pvolume = construct.construct_volume(
    'w', data[0], data[1], degree=1)
    
print(pvolume.knotvector_u)
print(pvolume.knotvector_v)
print(pvolume.knotvector_w)

# # Visualize volume
pvolume.vis = vis.VisVolume(vis.VisConfig(ctrlpts=True, evalpts=True))
pvolume.render()

operations.insert_knot(pvolume, [None, None, 0.5], [0, 0, 1])
pvolume.degree_w=2
print(pvolume.knotvector_w)
pvolume.render()

# # # Visualize volume
# operations.insert_knot(pvolume, [None, None, 0.25], [0, 0, 2])
# operations.insert_knot(pvolume, [None, None, 0.75], [0, 0, 2])
# print(pvolume.knotvector_w)
# pvolume.render()


# # # Construct the isosurface
# surfiso = construct.extract_isosurface(pvolume)
# msurf = multi.SurfaceContainer(surfiso)

# # Render the isourface
# msurf.vis = vis.VisSurface(vis.VisConfig(ctrlpts=False, legend=False))
# msurf.delta = 0.05
# msurf.render(evalcolor=["skyblue", "cadetblue", "crimson", "crimson", "crimson", "crimson"])

# exchange_vtk.export_polydata(msurf,'exportado_vtk1.vtk', tessellate=True)

# Visualize
# surf_cont.vis = vis.VisSurface(ctrlpts=False)
# surf_cont.render()
