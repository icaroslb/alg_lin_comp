import numpy as np

def norma_p_vetor ( v, p ):
	tam = v.shape[0]
	norma = 0
	
	for i in range ( tam ):
		norma += (v[i, 0])**p
	
	return norma**( 1 / p )

def norma_p ( M, p, m ):
	lin_col = M.shape
	
	norma = 0
	
	for i in range ( m ):
		x = np.random.rand( lin_col[0], 1 )
		x = ( x / np.linalg.norm( x ) )
		
		norma_aux = norma_p_vetor( M @ x, p ) / norma_p_vetor( x, p )
		
		norma = max( norma, norma_aux )
	
	return norma
			

valor_p = int( input( "Insira o p: " ) )
valor_m = int( input( "Insira o m: " ) )
num_lin_col = [ int(valor) for valor in input( "A quantidade de linhas(l) e colunas(c) separados por espaço \"l c\": " ).split( " " ) ]

M = np.zeros( ( num_lin_col[0], num_lin_col[1] ) )

for i in range ( num_lin_col[0] ):
	valores = [ float(valor) for valor in input( "Valores da linha " + str(i) + " separados por espaço: " ).split( " " ) ]
	M[ i, : ] = valores[0:num_lin_col[1]]

print( "\n-------------------------------------------------------------------------------\n" )

print( str( norma_p( M, valor_p, valor_m ) ) )
