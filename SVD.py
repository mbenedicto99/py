"""
Finalidade  : Decomposição em Valores Singulares (SVD) usando Python com NumPy. Esse exemplo mostra como decompor uma matriz 𝐴 em 𝑈Σ𝑉^𝑇
  e como você pode reconstruí-la com precisão ou com aproximação de baixo rank (compressão)
# Autor     : Marcos de Benedicto (IA)
# Data      : 22/03/2025
"""

import numpy as np

# Matriz A (exemplo simples)
A = np.array([
    [3, 2],
    [2, 3]
])

# SVD: decomposição A = U @ S @ VT
U, S, VT = np.linalg.svd(A)

# Exibir resultados
print("Matriz original A:")
print(A)

print("\nMatriz U:")
print(U)

print("\nValores singulares (vetor S):")
print(S)

print("\nMatriz V transposta (VT):")
print(VT)

# Converter vetor S para matriz diagonal
Sigma = np.diag(S)

# Reconstruir A (A ≈ U @ Sigma @ VT)
A_reconstruida = U @ Sigma @ VT
print("\nMatriz reconstruída (U * Σ * VT):")
print(A_reconstruida)
