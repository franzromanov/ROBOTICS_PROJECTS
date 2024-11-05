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
theta_1=((90)*math.pi)/180
theta_2=((45)*math.pi)/180
theta_3=((45)*math.pi)/180


DH_Param=[

[theta_1,0,0,0],
[theta_2,math.radians(90),0,5],
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
A_trans_all=[
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
]

A_container=[]

"""
[joint_1],
[joint_2],
[joint_3],
"""

for i in range(3):
    A_trans_i=[

    [math.cos(DH_Param[i][0]),-(math.sin(DH_Param[i][0]))*math.cos(DH_Param[i][1]),math.sin(DH_Param[i][0])*math.sin(DH_Param[i][1]),(DH_Param[i][2])*math.cos(DH_Param[i][0])],
    [math.sin(DH_Param[i][0]),(math.cos(DH_Param[i][0]))*math.cos(DH_Param[i][1]),-(math.cos(DH_Param[i][0])*math.sin(DH_Param[i][1])),(DH_Param[i][2])*math.sin(DH_Param[i][0])],
    [0,math.sin(DH_Param[i][1]),math.cos(DH_Param[i][1]),DH_Param[i][3]],
    [0,0,0,1],

    ]

    A_trans_all=np.matmul(np.array(A_trans_all),np.array(A_trans_i))
    A_container.append(A_trans_all)

print(A_container)

# Extract x, y, and z coordinates from each transformation matrix in A_container
x0, y0, z0 = A_container[0][0, 3], A_container[0][1, 3], A_container[0][2, 3]
x1, y1, z1 = A_container[1][0, 3], A_container[1][1, 3], A_container[1][2, 3]
x2, y2, z2 = A_container[2][0, 3], A_container[2][1, 3], A_container[2][2, 3]

# Print the extracted coordinates
print("Coordinates of joints:")
print(f"Joint 1: (x0, y0, z0) = ({x0}, {y0}, {z0})")
print(f"Joint 2: (x1, y1, z1) = ({x1}, {y1}, {z1})")
print(f"Joint 3: (x2, y2, z2) = ({x2}, {y2}, {z2})")

# Optional: Plotting the 3D positions
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot([0, x0, x1, x2], [0, y0, y1, y2], [0, z0, z1, z2], marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Robot Arm Joint Positions in 3D')
plt.show()

