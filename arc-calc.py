import math

class Vec3:
    x = float(0.0)
    y = float(0.0)
    z = float(0.0)
    def __init__(self):
        x=0
        y=0
        z=0

def scale(v, len):
    n = Vec3()
    s = len/(math.sqrt(v.x**2 + v.y**2 + v.z**2))
    n.x = v.x * s
    n.y = v.y * s
    n.z = v.z * s
    return n;

def project(p, k, u):
    #Projects point p onto the plane, given by normal vector u and point k
    n = Vec3()
    v = Vec3()
    J = Vec3()
    n = scale(u, 1)

    v.x = p.x - k.x
    v.y = p.y - k.y
    v.z = p.z - k.z

    d = v.x*n.x + v.y*n.y + v.z*n.z
    J.x = p.x - d*n.x
    J.y = p.y - d*n.y
    J.z = p.z - d*n.z

    return J

def vecsum(q, w):
    t = Vec3()
    t.x = q.x + w.x
    t.y = q.y + w.y
    t.z = q.z + w.z
    return t

def vecsub(q, w):
    t = Vec3()
    t.x = q.x - w.x
    t.y = q.y - w.y
    t.z = q.z - w.z
    return t

def vecmult(v, mult):
    t = Vec3()
    t.x = v.x * mult
    t.y = v.y * mult
    t.z = v.z * mult

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
r = float(input("Control Point Linear Offset"))

# find midpoint

K = Vec3()
K.x = (A.x + B.x) / 2
K.y = (A.y + B.y) / 2
K.z = (A.z + B.z) / 2

KB = Vec3()
KB = vecsub(B, K)

R = Vec3()
R.x = K.x + d * math.sin(th*math.pi/180)
R.y = K.y + d * math.cos(th*math.pi/180)
R.z = K.z

# Project these back to the plane we are working on

R = project(R, K, KB)


print("Coordinates: (", f'{R.x:.6f}', ", ", f'{R.y:.6f}', ", ", f'{R.z:.6f}', ")")

# Now, determine the equation for the line between the two points, in order to find the control points for the center point

if r != 0:
    M = Vec3()
    M = vecsub(B, A)
    M = scale(M, r)

    C1 = Vec3()
    C2 = Vec3()
    C1 = vecsum(R, M)
    C2 = vecsub(R, M)

    print("Control Point Coordinates:")
    print("(", f'{C1.x:.6f}', ", ", f'{C1.y:.6f}', ", ", f'{C1.z:.6f}', ")")
    print("(", f'{C2.x:.6f}', ", ", f'{C2.y:.6f}', ", ", f'{C2.z:.6f}', ")")
