import random

def print_mat(mat):
    for i in mat:
        print(i)

def solution(M, N):
    matA = [[0 for x in range(N)] for y in range(M)]
    product = 1 # iloczyn wszystkich niezerowych elelemntow macierzy A
    num_zero = 0 # liczba elementów zerowych macierzy
    i_zero = None # wspolrzedne zerowego elementu, wykorzystywane w przypadku gdy jest tylko jeden element zerowy
    j_zero = None # wspolrzedne zerowego elementu, wykorzystywane w przypadku gdy jest tylko jeden element zerowy

    # Dodanie elementow z zakresu [0,100], obliczenie iloczynu wszystkich niezerowych elementow macierzy, liczba zerowych elementow
    for i in range(M):
        for j in range(N):
            r = random.randint(0,100)
            matA[i][j] = r
            if r != 0:
                product *=r
            else:
                if num_zero == 0:
                    i_zero = i
                    j_zero = j 

                num_zero += 1

    # Jezeli wiecej niz jeden element macierzy A rowna sie 0, wszystkie elementy matB wynosza 0
    if num_zero >= 2:
        matB = [[0 for x in range(N)] for y in range(M)]
    
    # Jezeli jeden element macierzy wynosi 0, jeden element matB rowna sie iloczynowi elementow macierzy, reszta wynosi 0
    elif num_zero == 1:
        matB = [[0 for x in range(N)] for y in range(M)]
        matB[i_zero][j_zero] = product
    
    # Jezeli brak elementow zerowych, matB[i][j] = product/matA[i][j]
    else:
        matB = [[product for x in range(N)] for y in range(M)]
        for i in range(M):
            for j in range(N):
                matB[i][j] = int(matB[i][j]/matA[i][j])
    
    # Dla liczby wierszy i kolumn rownej 1
    if (N == 1 and M == 1):
        matB = [[None for x in range(N)] for y in range(M)]
    return matA, matB


if __name__ == "__main__":
       
    M = int(input("M: "))
    N = int(input("N: "))

    matrixA, matrixB = solution(M, N)

    print("Matrix A:")
    print_mat(matrixA)

    print("Matrix B:")
    print_mat(matrixB)

        
