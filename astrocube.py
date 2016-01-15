import numpy as np

from vispy import app, scene

from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

from multivol import MultiVolume
from multivol import get_translucent_cmap

# filename = download_file('https://astropy.stsci.edu/data/l1448/l1448_13co.fits')
filename = get_pkg_data_filename('l1448/l1448_13co.fits')

# Read in data
data = fits.getdata(filename)

# Create subsets

subset1 = np.zeros_like(data)
keep = data[:,:33,:33] > 1
subset1[:,:33,:33][keep] = data[:,:33,:33][keep]

subset2 = np.zeros_like(data)
keep = data[:,:33,-33:] > 1
subset2[:,:33,-33:][keep] = data[:,:33,-33:][keep]

subset3 = np.zeros_like(data)
keep = data[:,-33:,-33:] > 0.5
subset3[:,-33:,-33:][keep] = data[:,-33:,-33:][keep]

subset4 = np.zeros_like(data)
keep = data[:,-33:,:33] > 0.5
subset4[:,-33:,:33][keep] = data[:,-33:,:33][keep]

# Create Vispy visualization

canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
view = canvas.central_widget.add_view()
emulate_texture = False

grays = get_translucent_cmap(1, 1, 1)
reds = get_translucent_cmap(1, 0, 0)
greens = get_translucent_cmap(0, 1, 0)
blues = get_translucent_cmap(0, 0, 1)
oranges = get_translucent_cmap(1, 0.5, 0)

# Create the volume visuals, only one is visible
print(data.max())
volumes = [
           (data, (0, 6), grays),
           (subset1, (0, 4), reds),
           (subset2, (0, 4), greens),
           (subset3, (0, 4), blues),
           (subset4, (0, 4), oranges)
       ]
       
volume1 = MultiVolume(volumes, parent=view.scene, threshold=0.225,
                               emulate_texture=emulate_texture)
volume1.transform = scene.STTransform(translate=(64, 64, 0))


view.camera = scene.cameras.TurntableCamera(parent=view.scene, fov=60.,
                                            name='Turntable')


canvas.update()
#
# # create colormaps that work well for translucent and additive volume rendering
#
#
# # for testing performance
# # @canvas.connect
# # def on_draw(ev):
# # canvas.update()
#
if __name__ == '__main__':
    app.run()
