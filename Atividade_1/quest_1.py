import numpy as np

print( "Quantidade de linhas(l) e colunas(c)  \"l c\": ", end = '' )
lin, col = [ int(valor) for valor in input().split( " " ) ]

matriz_A = np.zeros( ( lin, col ) )

print( "Insira os valores a(l, c):" )

for i in range (lin):
	for j in range (col):
		print( "a" + str(i) + ", " + str(j) + ": ", end = '' )
		matriz_A[i, j] = float( input() )

matriz_A_l_1 = np.hstack( ( matriz_A[0:int(lin/2), int(col/2):col], matriz_A[int(lin/2):lin, int(col/2):col] ) )
matriz_A_l_2 = np.hstack( ( matriz_A[0:int(lin/2), 0:int(col/2)],   matriz_A[int(lin/2):lin, 0:int(col/2)]   ) )
matriz_A_l   = np.vstack( ( matriz_A_l_1, matriz_A_l_2 ) )

print( "\n-------------------------------------------------------------------------------\n" )

print( "A  =" )
print( matriz_A, end = "\n\n" )
print( "A' =" )
print( matriz_A_l ),
