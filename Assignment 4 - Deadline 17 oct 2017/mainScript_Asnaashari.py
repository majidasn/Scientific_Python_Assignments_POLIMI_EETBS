import os
os.chdir("D:\polimi note books/energy and enviromnetal technologies for building systems/assignments")
import wallcalculations_Asnaashari as WCA

wallpar1=["out_Surface_winter","gypsum","woodBevel","GlassFiber","brick","woodFiber","inside_Surface"]
wallpar2=["out_Surface_winter","gypsum","woodBevel","woodStud90","brick","woodFiber","inside_Surface"]
f1=0.3
f2=0.7

resultsforthiswall=WCA.wallCalc_withParallel(wallpar1,wallpar2,0.3,0.7)
    
doorlayer = ["out_Surface_winter" , 'Wood_50mm' , 'Inside_Surface']
rooflayer = ["out_Surface_winter" , 'AsphaltShingleRoofing' ,
'Wood_Fiberboard' ,'Glass_Fiber' , 'Inside_Surface' ]

door = WCA.wallcalc_series ( doorlayer )
roof = WCA.wallcalc_series ( rooflayer )


Door_area = 1*2.2
Wall_area = 105.8
Roof_area = 20*10


Tin = 20
Tout = -4.8
delta_T = Tin - Tout




Qwall = Wall_area * delta_T * resultsforthiswall['U_TOT']
Qdoor = Door_area * delta_T * door ['U_TOT']
Qroof = Roof_area * delta_T * roof ['U_TOT']

Qtot = Qwall + Qdoor + Qroof







