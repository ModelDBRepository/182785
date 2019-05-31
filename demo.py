"""
Demo of automatically generating a 3D-printable WRL file from a SWC file.
"""

import urllib2
from neuron import h
from prepare_3dprintable import ctng
from mayavi import mlab

morphology_url = 'http://neuromorpho.org/dableFiles/amaral/CNG%20version/c91662.CNG.swc'
morphology_filename = 'c91662.CNG.swc'
wrl_filename = 'c91662.wrl'

"""
download c91662 morphology from NeuroMorpho.Org

Ascoli, G. A., Donohue, D. E., & Halavi, M. (2007). NeuroMorpho. Org: a central
   resource for neuronal morphologies. The Journal of Neuroscience, 27(35),
   9247-9251.
Ishizuka, N., Cowan, W. M., & Amaral, D. G. (1995). A quantitative analysis of
    the dendritic organization of pyramidal cells in the rat hippocampus. Journal
    of Comparative Neurology, 362(1), 17-45.
"""
with open(morphology_filename, 'w') as f:
    f.write(urllib2.urlopen(morphology_url, timeout=10).read())

"""
Load it into NEURON
"""
h.load_file('stdlib.hoc')
h.load_file('import3d.hoc')
cell = h.Import3d_SWC_read()
cell.input(morphology_filename)
i3d = h.Import3d_GUI(cell, 0)
i3d.instantiate(None)

"""
Generate the WRL
"""
ctng(show=False, magnification=200)
mlab.savefig(wrl_filename)

