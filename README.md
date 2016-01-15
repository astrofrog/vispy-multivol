About
=====

This implements a ``MultiVolumeVisual`` and a ``MultiVolume`` class for
[VisPy](http://www.vispy.org) which allows multiple volumes to be shown
simultaneously. This is still experimental and under development.

Simply use the ``MultiVolume`` class as you would use the ``Volume`` class in
[VisPy](http://www.vispy.org), but instead of passing the volume data,
``clim``, and ``cmap`` as separate arguments, the first argument should be a
list of tuples, where each tuple contains ``(data, clim, cmap)``.

In future it should be possible to also add extra tuples to the ``volumes``
attribute of the ``MultiVolume`` on-the-fly.

You can try the two examples in the repository by running:

```
python medical.py
```

and

```
python astrocube.py
```

![screenshot](screenshot.png)
