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
theta_1=((120)*math.pi)/180
theta_2=((45)*math.pi)/180
theta_3=((0)*math.pi)/180
theta_4=((0)*math.pi)/180
theta_5=((90)*math.pi)/180
theta_6=((180)*math.pi)/180
theta_7=((0)*math.pi)/180

DH_Param=[

[theta_1,0,0,0],
[theta_2,math.radians(-90),0,5],
[theta_3,0,10,0],
[theta_4,math.radians(0),5,0],
[theta_5,math.radians(90),5,0],
[theta_6,math.radians(-90),0,5],
[theta_7,math.radians(0),5,0],
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

for i in range(7):
	A_trans_i=[

	[math.cos(DH_Param[i][0]),-(math.sin(DH_Param[i][0]))*math.cos(DH_Param[i][1]),math.sin(DH_Param[i][0])*math.sin(DH_Param[i][1]),(DH_Param[i][2])*math.cos(DH_Param[i][0])],
	[math.sin(DH_Param[i][0]),(math.cos(DH_Param[i][0]))*math.cos(DH_Param[i][1]),-(math.cos(DH_Param[i][0])*math.sin(DH_Param[i][1])),(DH_Param[i][2])*math.sin(DH_Param[i][0])],
	[0,math.sin(DH_Param[i][1]),math.cos(DH_Param[i][1]),DH_Param[i][3]],
	[0,0,0,1],

	]

	A_trans_all=np.matmul(np.array(A_trans_all),np.array(A_trans_i))
	A_container.append(A_trans_all)
	print(A_trans_all)
print(A_container)


# Extract x, y, and z coordinates for each joint
x_coords = [A[0, 3] for A in A_container]
y_coords = [A[1, 3] for A in A_container]
z_coords = [A[2, 3] for A in A_container]

# Print the coordinates
for i, (x, y, z) in enumerate(zip(x_coords, y_coords, z_coords)):
    print(f"Joint {i+1}: (x, y, z) = ({x:.2f}, {y:.2f}, {z:.2f})")

# Optional: Plotting the 3D positions
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot([0] + x_coords, [0] + y_coords, [0] + z_coords, marker="o")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Robot Arm Joint Positions in 3D")
plt.show()
