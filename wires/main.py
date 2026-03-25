import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import(opening,dilation,closing,erosion)

image=np.load("data/wires2.npy")
struct=np.ones((3,1))
processed=opening(image,footprint=struct)
labeled = label(image)
print(f"{labeled.max()}")

for n in range(1,labeled.max()+1):
    wire=labeled==n
    wire = opening(wire,footprint=struct)
    labeled_wire=label(wire)
    parts = labeled_wire.max()
    print(f"Wire={n},parts={0}")

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(processed)
plt.show()