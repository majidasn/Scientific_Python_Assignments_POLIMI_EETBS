# -*- coding: utf-8 -*-
import numpy as np
Rnames = np.array(['woodStud90','winter_out_Surface','Inside_Surface','woodBevel','woodFiberboard13mm','GlassFiber90mm','gypsumWallboard13mm'])
Rvalues = np.array([0.079,0.03,0.12, 0.14,0.23,2.45,0.63, 0.018]) 
Rtype = np.array(["par","ser","ser","ser","ser","par","ser"])


ratio = 0.75
R=Rvalues[Rtype=="ser"]+Rvalues[Rtype=="par"]
R=Rvalues.sum()

Upar=1/R[0]
User=1/R[1]
Uoverall = ratio*R[0] + ratio*R[1]

Roverall = 1/Uoverall

