import math
def getCylinderVolume (height, radius) :
    Volume = math.pi * (radius**2) * height
    return Volume 

r = float(input("What's the radius"))
h = float(input("What's the height"))


Volume = getCylinderVolume (h,r)
print("Your cake will be", round (Volume,4), "cubic centimeters")

def getCakeSlices (Volume, slicevolume) :
    Slices = Volume / slicevolume
    return int(Slices)
    
slice_volume = int(input("What slice volume would you like?"))

Slices = getCakeSlices (Volume, slice_volume)
print (Slices) 


