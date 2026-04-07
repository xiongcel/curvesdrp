#source /Users/cx/Downloads/ctest/.venv/bin/activate
#python3 /Users/cx/Downloads/ctest/ctest.py

import numpy as np
import random
import curver

S = curver.load(1,1)
print(S)
# surface = curver.load('S_1_2') #same thing, just with str/different formatting 
# print(surface)
# print(curves)
# curves = S.curves

# c = S.lamination([1, 0, 1, 0, 0, 0])

curves = list(S.curves.values())
print(f"Choices of curves are: {curves}.")  #isotopy classes?
curve = random.choice(curves)
print(f"Starting curve is: {curve}")

for step in range(20):
    c = random.choice(curves)   #random curve to be turned into mapping class for dehn twist 
    # print(c)
    twist = c.encode_twist()
    if random.random() < 0.5:
        twist = twist.inverse()
    curve = twist(curve)    #curve = twist * old curve
    # print(curve)
print(f"Your random curve is: {curve}!")

# c = S.lamination([1, 0, 1, 0, 0, 0])
# a = S.arcs['s_1']
# h = S('a_0.b_0')
# curver.show(c, h(c), a, h(a))
# print(h.is_periodic())
# print(h)

"""representation of Bolza surface"""
l = [0,1,2,3]
gens = {}
for k in l:
    x = 1 + np.sqrt(2)
    y = (2 + np.sqrt(2))*(np.sqrt(np.sqrt(2)-1))*np.exp((1j*k*np.pi)/4)
    z = (2 + np.sqrt(2))*(np.sqrt(np.sqrt(2)-1))*np.exp(-(1j*k*np.pi)/4)
    gens[k] = np.array([[x, y], [z, x]])
    # print(g)
# print(gens)

"""check hom relation aBcDAbcD = 1"""
A = gens[0]@np.linalg.inv(gens[1])@gens[2]@np.linalg.inv(gens[3])@np.linalg.inv(gens[0])@gens[1]@np.linalg.inv(gens[2])@gens[3]
I = np.identity(2)
if np.allclose(A, I) or np.allclose(A, -I):
    print("yay")
# print(np.linalg.eigvals(gens[0]))

# def hyp_length(M):
#     tr = np.trace(M)
#     return 1/2 * np.log(eigenvalue stuff goes here)
# print(f"Hyperbolic length is: {hyp_length(gens[0])}")