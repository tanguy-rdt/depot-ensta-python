import numpy as np

A= np.array([8, 2, 1, 1, 5, 1, 9, 1, 3, 2, 3, 5, 42, 28, 5, 1, 9, 1, -50, 12
             , 6, 5, 3, 12, -38]).reshape(5, 5) # matrice 5*5

B= np.array([42, 12, 28, 90, 32])

rangA=np.linalg.matrix_rank(A) #rang de A

eig=np.linalg.eig(A)
valPropre=eig[0]
vectPropre=eig[1]

P=vectPropre.copy() #les vecteurs propres sont déjà dans le bon sens P=(v0, v1, v2, v3, v4)
D=np.diag(valPropre)

Pinv=np.linalg.inv(P)

Aequal=np.allclose(A, (P.dot(D).dot(Pinv))) # .dot pour la multiplication de matrice
# A = P * D * Pinv
# Avec P la matrice de passage

sol=np.linalg.solve(A, B)

Bequal=np.allclose(A.dot(sol), B)



