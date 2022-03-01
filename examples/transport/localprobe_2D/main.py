# Add the root path of the pyqula library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")


from pyqula import geometry
from pyqula.heterostructures import LocalProbe
import numpy as np
import matplotlib.pyplot as plt
g = geometry.chain()
g = geometry.single_square_lattice()
h = g.get_hamiltonian()
h.add_onsite(2.0)
#h.add_pairing(mode="dx2y2",delta=0.1)
h.add_swave(0.5)
lp = LocalProbe(h) # create a local probe object
lp.bulk_delta = 1e-2 # this is the selfenergy of the bulk
es = np.linspace(-1.0,1.0,41)
lp.T = 1.0 
from pyqula import parallel
parallel.cores = 5
ts = parallel.pcall(lambda e: lp.didv(energy=e),es)
#ts = [lp.didv(energy=e) for e in es]

import matplotlib.pyplot as plt
plt.plot(es,ts)
plt.ylim([0.,max(ts)])
plt.show()

