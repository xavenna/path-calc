import math

class Vec3:
    x = float(0.0)
    y = float(0.0)
    z = float(0.0)
    def __init__(self):
        x=0
        y=0
        z=0

def project(p, k, u):
    #Projects point p onto the plane, given by normal vector u and point k
    n = Vec3()
    v = Vec3()
    J = Vec3()
    s = 1/(math.sqrt(u.x**2 + u.y**2 + u.z**2))
    n.x = u.x * s
    n.y = u.y * s
    n.z = u.z * s

    v.x = p.x - k.x
    v.y = p.y - k.y
    v.z = p.z - k.z

    d = v.x*n.x + v.y*n.y + v.z*n.z
    J.x = p.x - d*n.x
    J.y = p.y - d*n.y
    J.z = p.z - d*n.z

    #print(J.x, J.y, J.z)
    return J


A = Vec3()
B = Vec3()
th = float(0.0)
d = float(0.0)
r = float(0.0)

# Make this easier to use, maybe?
A.x = float(input("A.x"))
A.y = float(input("A.y"))
A.z = float(input("A.z"))
B.x = float(input("B.x"))
B.y = float(input("B.y"))
B.z = float(input("B.z"))

th = float(input("Plane offset angle"))
d = float(input("Distance above line"))
#r = float(input("Control Point Linear Offset"))

# find midpoint

K = Vec3()
K.x = (A.x + B.x) / 2
K.y = (A.y + B.y) / 2
K.z = (A.z + B.z) / 2

KB = Vec3()
KB.x = B.x - K.x
KB.y = B.y - K.y
KB.z = B.z - K.z

#print(K.x, K.y, K.z)
#print(KB.x, KB.y, KB.z)


# angle between planes:

#thetax = math.arccos(KB.z / (sqrt(KB.x**2 + KB.y**2 + KB.z**2)))
# cast K to XY plane, calculate Rx and Ry (projected x&y)


R = Vec3()
R.x = K.x + d * math.sin(th*math.pi/180)
R.y = K.y + d * math.cos(th*math.pi/180)
R.z = K.z

#print(R.x, R.y, R.z)

# Project these back to the plane we are working on

R = project(R, K, KB)

#Rz = K.z - (KB.x / KB.z) * (R.x-K.x) - (KB.y / KB.z) * (R.y-K.y)

print("Coordinates: (", f'{R.x:.6f}', ", ", f'{R.y:.6f}', ", ", f'{R.z:.6f}', ")")
