import rasterio
import rasterio.features
import rasterio.warp
import rasterio.mask
from rasterio.plot import show
import fiona

## import polygons calculated by NN
# with fiona.open("DB/Maidanetske_polygons_experts.geojson", "r") as shapefile:
#     ##field_2 defines confidence of NN
#     shapes = [feature["geometry"] for feature in shapefile if feature["properties"]["field_2"] > 0.1]

## import polygons from experts
with fiona.open("DB/Maidanetske_polygons_experts.geojson", "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]



## mas the buildings
with rasterio.open('DB/Maidanetske_magnet.tif') as dataset:
    out_image, out_transform = rasterio.mask.mask(dataset, shapes, crop=True)
    out_meta = dataset.meta

show(out_image)