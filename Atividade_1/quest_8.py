import numpy as np

print( "Insira o vetor separando os valor por espaço: ", end = '' )
val_vetor = [ float(valor) for valor in input().split( " " ) ]

print( "Insira o valor de k: ", end = '' )
k = int( input() )

tam_vetor = len( val_vetor )

matriz_A = np.zeros( ( tam_vetor, k + 1 ) )

for i in range( tam_vetor ):
	for j in range( k + 1 ):
		matriz_A[i, j] = val_vetor[i]**j

print( "\n-------------------------------------------------------------------------------\n" )

print( "\nA matriz:" )
print( matriz_A )
