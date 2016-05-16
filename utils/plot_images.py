import numpy as np
import math

# assumes images are square, otherwise pass tuple as imgsize
# good arguments for blend: None, np.maximum, np.minimum
def plot_images(images, positions, figsize=(512,512), imgsize=None, blend=None, bg=None):
    images = np.asarray(images)
    if images.ndim == 2:
        side = int(np.sqrt(len(images[0])))
        w = side if imgsize is None else imgsize[0]
        h = side if imgsize is None else imgsize[1]
        images = images.reshape(-1, h, w)
    else:
        h = images.shape[1]
        w = images.shape[2]
    
    positions = np.asarray(positions)
    positions -= positions.min(axis=0)
    positions /= positions.max(axis=0)
    positions *= (figsize[0] - w, figsize[1] - h)
    
    plot = np.zeros((figsize[1], figsize[0]))
    if bg is not None:
        plot.fill(bg)
    for image, position in zip(images, positions):
        x = int(position[0])
        y = int(position[1])
        if blend is None:
            plot[y:y+h, x:x+w] = image
        else:
            plot[y:y+h, x:x+w] = blend(plot[y:y+h, x:x+w], image)
    return plot