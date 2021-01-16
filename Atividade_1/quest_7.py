import numpy as np

print( "Insira o vetor separando os valor por espaço: ", end = '' )
val_vetor = [ float(valor) for valor in input().split( " " ) ]

print( "Insira o valor de k: ", end = '' )
k = int( input() )

tam_vetor = len( val_vetor )

matriz_A = np.zeros( ( tam_vetor, k ) )

for i in range( k ):
	for j in range( tam_vetor ):
		matriz_A[j, i] = val_vetor[j]

print( "\n-------------------------------------------------------------------------------\n" )

print( "\nA matriz:" )
print( matriz_A )
