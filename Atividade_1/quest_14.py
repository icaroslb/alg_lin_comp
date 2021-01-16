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
			

num_lin_col = int( input( "O tamanho do lado da matriz quadrada: " ) )

M = np.zeros( ( num_lin_col, num_lin_col ) )

for i in range ( num_lin_col ):
	for j in range ( i, num_lin_col ):
		M[ i, j ] = M[ j, i ] = float( input( "m[ {}, {} ] = m[ {}, {} ]: ".format( i, j, j, i ) ) )

print( "\n-------------------------------------------------------------------------------\n" )

print( "\nMatriz M:\n{}".format( M ) )
print( "\nO maior auto valor de M é aproximadamente {}".format( norma_p( M, 2, 100 ) ) )
