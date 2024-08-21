from PIL import Image
import numpy as np
import pandas as pd


im = Image.open('DB/Maidanetske_magnet.tif')
im.show()
imArray = np.array(im)
imShape = imArray.shape
print(imArray.size)
convert = np.reshape(imArray, (imShape[0]*imShape[1], imShape[2]))
ind = np.array([(x,y) for x in range(imShape[0]) for y in range(imShape[1])])
print(convert.size)
print(ind.size)
print(ind)

n = np.column_stack((ind, convert))
print(n)

df = pd.DataFrame(n, columns=["X", "Y", "R", "G", "B"])
print(df)
##reshape with x an y coord
# for index, x in np.ndenumerate(imArray):
#     t = [index[0],index[1],imArray[index[0]][index[1]][0],imArray[index[0]][index[1]][1],imArray[index[0]][index[1]][2]]
#     convert = np.append(convert, [t])
# r = np.reshape(convert,(imShape[0]*imShape[1],5))
# print(r)