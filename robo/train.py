import numpy as np
import matplotlib.pyplot as plt
import math

#D-H Param
"""
DH_Param=[
[theta_1,alpha_1,r_1,d_1],
[theta_2,alpha_2,r_2,d_2],
[theta_3,alpha_3,r_3,d_3]

]

>>>length-in-cm<<<
"""

#revolute_param
theta_1=((45)*math.pi)/180
theta_2=((30)*math.pi)/180
theta_3=((0)*math.pi)/180


DH_Param=[

[theta_1,0,0,0],
[theta_2,90,0,5],
[theta_3,0,10,0],

]

#transformation-Matrix
"""
A_trans=[

[c_theta_i,-s_theta_i*c_alpha_i,s_theta_i*s_alpha_i,r_i*c_theta_i],
[s_theta_i,c_theta_i*c_alpha_i,-c_theta_i*s_alpha_i,r_i*s_theta_i],
[0,s_alpha_i,c_alpha_i,d_i],
[0,0,0,1],

]

>>s=sin;c=cos;<<
"""

A_trans_1=[

[math.cos(DH_Param[0][0]),-(math.sin(DH_Param[0][0]))*math.cos(DH_Param[0][1]),math.sin(DH_Param[0][0])*math.sin(DH_Param[0][1]),(DH_Param[0][2])*math.cos(DH_Param[0][0])],
[math.sin(DH_Param[0][0]),(math.cos(DH_Param[0][0]))*math.cos(DH_Param[0][1]),-(math.cos(DH_Param[0][0])*math.sin(DH_Param[0][1])),(DH_Param[0][2])*math.sin(DH_Param[0][0])],
[0,math.sin(DH_Param[0][1]),math.cos(DH_Param[0][1]),DH_Param[0][3]],
[0,0,0,1],

]


A_trans_2=[

[math.cos(DH_Param[1][0]),-(math.sin(DH_Param[1][0]))*math.cos(DH_Param[1][1]),math.sin(DH_Param[1][0])*math.sin(DH_Param[1][1]),(DH_Param[1][2])*math.cos(DH_Param[1][0])],
[math.sin(DH_Param[1][0]),(math.cos(DH_Param[1][0]))*math.cos(DH_Param[1][1]),-(math.cos(DH_Param[1][0])*math.sin(DH_Param[1][1])),(DH_Param[1][2])*math.sin(DH_Param[1][0])],
[0,math.sin(DH_Param[1][1]),math.cos(DH_Param[1][1]),DH_Param[1][3]],
[0,0,0,1],

]

A_trans_3=[

[math.cos(DH_Param[2][0]),-(math.sin(DH_Param[2][0]))*math.cos(DH_Param[2][1]),math.sin(DH_Param[2][0])*math.sin(DH_Param[2][1]),(DH_Param[2][2])*math.cos(DH_Param[2][0])],
[math.sin(DH_Param[2][0]),(math.cos(DH_Param[2][0]))*math.cos(DH_Param[2][1]),-(math.cos(DH_Param[2][0])*math.sin(DH_Param[2][1])),(DH_Param[2][2])*math.sin(DH_Param[2][0])],
[0,math.sin(DH_Param[2][1]),math.cos(DH_Param[2][1]),DH_Param[2][3]],
[0,0,0,1],

]


A_trans_all=np.matmul(np.array(A_trans_1),np.array(A_trans_2))
A_trans_all=np.matmul(A_trans_all,np.array(A_trans_3))

print(A_trans_all)