# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# vispy: gallery 2

"""
Example volume rendering

** 5 - Subset highlight for 3D scatter plot 

Controls:

* 1  - toggle camera between first person (fly), regular 3D (turntable) and
       arcball
* 2  - toggle between volume rendering methods
* 3  - toggle between stent-CT / brain-MRI image
* 4  - toggle between colormaps
* 0  - reset cameras
* [] - decrease/increase isosurface threshold

With fly camera:

* WASD or arrow keys - move around
* SPACE - brake
* FC - move up-down
* IJKL or mouse - look around
"""

from itertools import cycle

import numpy as np

from vispy import app, scene, io
from vispy.scene import visuals
import vispy.visuals as impl_visuals
from vispy.color import get_colormaps, BaseColormap
from multivol import MultiVolume
from multivol import get_translucent_cmap

# Read volume
vol1 = np.load(io.load_data_file('volume/stent.npz'))['arr_0']
vol2 = np.load(io.load_data_file('brain/mri.npz'))['data']
vol2 = np.flipud(np.rollaxis(vol2, 1))

# Prepare canvas
canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
canvas.measure_fps()

# Set up a viewbox to display the image with interactive pan/zoom
view = canvas.central_widget.add_view()

# Set whether we are emulating a 3D texture
emulate_texture = False

reds = get_translucent_cmap(1, 0, 0)
blues = get_translucent_cmap(0, 0, 1)

# Create the volume visuals, only one is visible
volumes = [(vol1, None, blues), (vol1[::-1,::-1,::-1], None, reds)]
volume1 = MultiVolume(volumes, parent=view.scene, threshold=0.225,
                               emulate_texture=emulate_texture)
volume1.transform = scene.STTransform(translate=(64, 64, 0))

# Create three cameras (Fly, Turntable and Arcball)
fov = 60.
cam2 = scene.cameras.TurntableCamera(parent=view.scene, fov=fov,
                                     name='Turntable')
view.camera = cam2  # Select turntable at first

canvas.update()

# create colormaps that work well for translucent and additive volume rendering


# for testing performance
# @canvas.connect
# def on_draw(ev):
# canvas.update()

if __name__ == '__main__':
    print(__doc__)
    app.run()
