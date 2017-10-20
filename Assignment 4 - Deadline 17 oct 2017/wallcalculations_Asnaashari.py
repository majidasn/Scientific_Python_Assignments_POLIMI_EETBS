# -*- coding: utf-8 -*-
def wallCalc_withParallel(wallpar1,wallpar2,f1,f2):
    material_library={"out_Surface_winter":0.03,"woodBevel":0.14,"woodFiber":0.23,"GlassFiber":2.52,"woodStud90":0.63,"gypsum":0.079,"inside_Surface":0.12,"brick":0.12}
    
    wallpar1=["out_Surface_winter","gypsum","woodBevel","GlassFiber","brick","woodFiber","inside_Surface"]
    wallpar2=["out_Surface_winter","gypsum","woodBevel","woodStud90","brick","woodFiber","inside_Surface"]
    f1=0.3
    f2=0.7
    
    wallcomplete=wallpar1+wallpar2

    R_par1_tot=0
    

    for anylayer in wallpar1:
        Rparallel=material_library[anylayer]
        R_par1_tot=R_par1_tot+Rparallel
    U_between_studs=1/ R_par1_tot
    print U_between_studs
    
    R_par2_tot=0

    for anylayer in wallpar2:
        Rparallel=material_library[anylayer]
        R_par2_tot=R_par2_tot+Rparallel
    U_at_studs=1/ R_par2_tot
    print U_at_studs

    RValues_layers=[]
    for anylayer in wallcomplete:
        RValue_layers = material_library[anylayer]
        RValues_layers.append(RValue_layers)
    print"Rtotal for wall layers is" + str(RValue_layers)
        
        
        
    U_TOT = f1*U_between_studs + f2*U_at_studs
    R_TOT = 1 / U_TOT
    print "R_Tot is " + str(R_TOT) + "m2°C/W"
    print "U_Tot is " + str(U_TOT) + "W/m2°C"             
    results = {"Rtot":R_TOT,"Utot":U_TOT}
    return results  
        

        
wallpar1=["out_Surface_winter","gypsum","woodBevel","GlassFiber","brick","woodFiber","inside_Surface"]
wallpar2=["out_Surface_winter","gypsum","woodBevel","woodStud90","brick","woodFiber","inside_Surface"]
f1=0.3
f2=0.7   
    
resultsforthiswall=wallCalc_withParallel(wallpar1,wallpar2,0.3,0.7)
    

#------------------------------------------------------------------------------------------------------------------.

def wallcalc_series(serieslayerlist) :
    
    Material_library = { "out_Surface_winter" : 0.03 , 'Inside_Surface' : 0.12 , 'Wood_50mm' : 0.22 ,
    'Wood_Bevel' : 0.14 , 'Wood_Fiberboard' : 0.23 , 'Glass_Fiber' : 2.52 , 'Wood_Stud' : 0.63 , 'Gypsum' : 0.079 ,
    'Cement_Mortar' : 0.018 , 'Common_Brick' : 0.12 , 'Wood_Fiberboard' : 0.23 , 'asphaltroof' : 0.077}
    R_series = 0
    
    for anylayer in serieslayerlist :
        if (anylayer == 'Wood_50mm') :                                  
            R_anylayer = Material_library ['Wood_50mm']     
        else :
            R_anylayer = Material_library [ anylayer ] 
        R_series = R_series + R_anylayer
        print R_series
    
        
    U_series = 1 / R_series 
    print "value of all res: " + str (R_series) 

    print "U" + str (U_series) 
    
    results = {R_series,U_series}
    return results
    

  
layerlist_door = [ 'out_Surface_winter','Inside_Surface','Wood_50mm']
layerlist_roof = [ 'out_Surface_winter' , 'asphaltroof' ,'Wood_Fiberboard' ,'Glass_Fiber' , 'Inside_Surface' ]


door = wallcalc_series ( layerlist_door )
roof = wallcalc_series ( layerlist_roof )


