import matplotlib.transforms as mtransforms
import rasterio
import rasterio.features
import rasterio.warp
import rasterio.mask
from rasterio.plot import show
import fiona
import numpy as np

with fiona.open("DB/Maidanetske_polygons_experts.geojson", "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]

shape = shapes[1]
coor = shape['coordinates'][0][0]
tr = mtransforms.Affine2D().scale(sx=np.float64(1), sy=np.float64(1))
coor = np.array(coor)
coor = np.hstack((coor, [[0],[0],[0],[0],[0]]))
nulling_x = coor[0][0]
nulling_y = coor[0][1]
null = coor.mean(axis=0)
coor2 = [(x[0]-null[0], x[1]-null[1], x[2]) for x in coor]
t = np.matmul(coor2, tr)
t = t[:,:2]
t = [(x[0]+nulling_x,x[1]+nulling_y) for x in t]
g = fiona.Geometry(coordinates=[[t]],type="MultiPolygon")
## mas the buildings
with rasterio.open('DB/Maidanetske_magnet.tif') as dataset:
    out_image, out_transform = rasterio.mask.mask(dataset, [g],crop=True)
    out_meta = dataset.meta

show(out_image)