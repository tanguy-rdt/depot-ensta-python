import numpy as np

A = np.array([1, 0, 87, 23, 0, 6, 9])
print("A:", A)
print("A[1]:", A[1])
print("A[0]:", A[0])
print("A[-1]:", A[-1])
print("A.size:", A.size)
print("A.shape:", A.shape)
print("A[5]:", A[5])
print("A[:5]:", A[:5]) # print les 5 premiers index
print("A[3:]:", A[3:]) # print en ignorant les 3 premiers index
print("A[::-1]:", A[::-1]) # retourne la le tab
print("A[::2]:", A[::2]) # print de l'index 0 à n avec un pas de 2
print("A[1:6:2]:", A[0:6:2]) # [start:end:step], le dernier élément n'est pas pris en compte

print("\n\n")

B = np.array([[1, 0], [87, 23], [0 ,6]])
print("B:", B)
print("B[0]:", B[0])
print("B[0, 1]:", B[0, 1])
print("B[-1, 0]:", B[-1, 0])
print("B[:, 1]:", B[:, 1])
print("B.size:", B.size)
print("B.shape:", B.shape)

print("\n\n")

C = np.zeros(4) #tableau 1D 4 en zero
print("C:", C)
C = np.zeros((4, 4)) #tableau 2D 4x4 en zero
print("C:", C)
print("Dim de C:", np.ndim(C))
C = np.arange(3, 10) #tableau 1D de 3 à 10
print("C:", C)
C= np.linspace(4, 10, 4) #tableau 1D de 4 avec val équiréparti entre 4 et 10
print("C:", C)
print("Produit des coef:", np.prod(C))
print("Val min des coef:", np.min(C))
print("Moyenne des coef", np.mean(C))
C= np.eye(4) # Créer une matrice Id 4x4
C= np.diag(np.array([1, 2, 3, 4])) # Créer une matrice diagonal 4x4 avec comme valeur 1, 2, 3, 4
C = np.random.rand(4)       # uniform in [0, 1], tab 1D de 4 éléments
print("C:", C)
print("Type de valeur de C:", C.dtype)
#np.random.seed(1234)        # Setting the random seed
print(C)


print("\n\n")

L = np.array([0, 8, 9, 3])
A = np.array([5, 4, 1, 2])
ratio_LA = L / A
A_carre = A**2
prod_AL = A * L
print("ratio_LA: ", ratio_LA)
print("A_carre: ", A_carre)
print("prod_AL:", prod_AL)

print("\n\n")

A = np.arange(16).reshape((4, 4)) #créer un tableau 1D de 16 éléments (0 --> 15), et transformation sur un tab 2D (4, 4)
X = np.array([5, 4, 1, 2])
print(A)
print(X)
B = A @ X #multiplication au sens matriciel
print(B)

print("\n\n")

A = np.arange(16).reshape((4, 4))
X = np.array([5, 4, 1, 2])
print(A.T) #Transposer du tableau A
print(X.T) #Transposer du tableau X








