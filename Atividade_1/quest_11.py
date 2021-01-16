import numpy as np

def norma_1 ( M ):
	lin_col = M.shape
	
	norma = 0
	
	for j in range ( lin_col[1] ):
		norma_aux = 0
		for i in range ( lin_col[0] ):
			norma_aux += abs( M[ i, j ] )
		
		norma = max( norma, norma_aux )
	
	return norma
			


num_lin_col = [ int(valor) for valor in input( "A quantidade de linhas(l) e colunas(c) separados por espaço \"l c\": " ).split( " " ) ]

M = np.zeros( ( num_lin_col[0], num_lin_col[1] ) )

for i in range ( num_lin_col[0] ):
	valores = [ float(valor) for valor in input( "Valores da linha " + str(i) + " separados por espaço: " ).split( " " ) ]
	M[ i, : ] = valores[0:num_lin_col[1]]

print( "\n-------------------------------------------------------------------------------\n" )

print( str( norma_1( M ) ) )
