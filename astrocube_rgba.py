import numpy as np

from vispy import app, scene

from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

from multivol import RGBAVolume
from multivol import get_translucent_cmap

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

grays = np.array([1,1,1,0.5])
reds = np.array([1,0,0,0.5])
greens = np.array([0,1,0,0.5])
blues = np.array([0,0,1,0.5])
oranges = np.array([1,0.5,0,0.5])

# Combine data
combined_data = np.zeros(data.shape + (4,))
combined_data += data[:,:,:,np.newaxis] / 6. * grays
combined_data += subset1[:,:,:,np.newaxis] / 4. * reds
combined_data += subset2[:,:,:,np.newaxis] / 4. * greens
combined_data += subset3[:,:,:,np.newaxis] / 4. * blues
combined_data += subset4[:,:,:,np.newaxis] / 4. * oranges

combined_data /= 5.

combined_data = np.clip(combined_data, 0, 1)

volume1 = RGBAVolume(combined_data, parent=view.scene)
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
