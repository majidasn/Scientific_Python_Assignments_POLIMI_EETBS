import pandas as pd

#([type, h, k, L, area,Rvalue])

R1=["convection",20.0, None,0.25,None,0]
Rf=["condseries",None, 0.026,0.25,0.03,0]
Rp1=["condseries",None, 0.22,0.25,0.02,0]
Rp2=["condseries",None, 0.22,0.25,0.02,0]
R_pc1=["conductionpar",None, 0.22,0.015,0.16,0]
R_pc2=["conductionpar",None, 0.22,0.015,0.16,0]
Rb=["conductionpar",None, 0.72,0.22,0.16,0]
R2=["convection",10.0, None,0.25,None,0]


area_series=0.25

#calculate R total
res_name = ["Rf","Rp1","Rp2","Rpc_1","Rpc_2","Rb","R1","R2"]
columns = ["type","h","k","L","area","R"]
resistances_ListOfLists  = [R1,Rf,Rp1,Rp2,R_pc1,R_pc2,Rb,R2]

resistances_dataFrame = pd.DataFrame(resistances_ListOfLists,index=res_name, columns=columns)

resistances_dataFrame["R"][ resistances_dataFrame ["type"]=="condseries" ] =  resistances_dataFrame["L"][resistances_dataFrame["type"]=="condseries" ] / (resistances_dataFrame["k"][resistances_dataFrame["type"]=="condseries" ] * resistances_dataFrame["area"][resistances_dataFrame["type"]=="condseries" ])
resistances_dataFrame["R"][ resistances_dataFrame ["type"]=="conductionpar" ] =  resistances_dataFrame["L"][resistances_dataFrame["type"]=="conductionpar" ] / (resistances_dataFrame["k"][resistances_dataFrame["type"]=="conductionpar" ] * resistances_dataFrame["area"][resistances_dataFrame["type"]=="conductionpar" ])
resistances_dataFrame["R"][ resistances_dataFrame ["type"]=="convection" ] = 1 / (resistances_dataFrame["h"][resistances_dataFrame["type"]=="convection" ] * resistances_dataFrame["area"][resistances_dataFrame["type"]=="convection" ])
condseries = resistances_dataFrame["R"][ resistances_dataFrame ["type"]=="condseries" ].sum()
conductionpar = 1/ ((1/resistances_dataFrame["R"][ resistances_dataFrame ["type"]=="condpara" ]).sum())
Rconv = resistances_dataFrame["R"][ resistances_dataFrame ["type"]=="conv" ].sum()
Rtot = Rconv + conductionpar + condseries

