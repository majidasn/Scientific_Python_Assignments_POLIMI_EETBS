# -*- coding: utf-8 -*-
import numpy as np

Resistancesnames =np.array (["R1","Rf","Rp1","Rp2","R_pc1","R_pc2","Rb","R2"] ) 
Rtype = np.array (["convection","condseries","condseries","condseries","conductionpar","conductionpar","conductionpar","convection"])
R_h = np.array([20.0, None, None, None, None, None,None,10.0,])
R_k = np.array([None,0.026, 0.22, 0.22, 0.22, 0.22, 0.72,None])
R_area = np.array ([ 0.25,0.25, 0.25, 0.25, 0.015, 0.015, 0.22, 0.25])
R_length = np.array([None,0.03, 0.02, 0.02, 0.16, 0.16, 0.16,None])

Rvalues = np.array (np.zeros(8))
Rvalues [Rtype == "condseries"] = R_length[Rtype=="condseries"]/(R_k[Rtype=="condseries"]*R_area[Rtype=="condseries"])
Rvalues [Rtype == "conductionpar"] = R_length[Rtype=="conductionpar"]/(R_k[Rtype=="conductionpar"]*R_area[Rtype=="conductionpar"])
Rvalues [Rtype == "convection"] = 1/(R_h[Rtype=="convection"]*R_area[Rtype=="convection"])

Rparainv = np.array (np.zeros(8))
Rparainv [Rtype == "conductionpar"] = 1/Rvalues [Rtype == "conductionpar"]
Rconductionpar = 1/Rparainv [Rtype == "conductionpar"].sum()

Rcondser = Rvalues [Rtype == "condseries"].sum()
Rconv = Rvalues [Rtype == "convection"].sum()
Rtot = Rcondser + Rconductionpar + Rconv
print "Total resistance is: " + str(Rtot) + "°C/W"

