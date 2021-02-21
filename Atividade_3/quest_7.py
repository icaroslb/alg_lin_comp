import numpy as np

def vetor_matriz_rot_givens ( vetor, i, j ):
    xi = vetor[i][0]
    xj = vetor[j][0]

    cost = xi / ( np.sqrt( xi**2 + xj**2 ) )
    sent = xj / ( np.sqrt( xi**2 + xj**2 ) )

    R = np.eye( vetor.shape[0] )

    R[i][i] = R[j][j] = cost
    R[i][j] =  sent
    R[j][i] = -sent

    return R

if ( __name__ == "__main__" ):
    vetor_entrada = [ float( x ) for x in input( "Insira os valores do vetor separados por espaço: " ).split( " " ) ]
    pos_entradas  = [ int( x ) for x in input( "Insira o i e j separado por espaço: " ).split( " " ) ]

    vetor = np.zeros( [ len( vetor_entrada ), 1 ] )

    for i in range( len( vetor_entrada ) ):
        vetor[i][0] = vetor_entrada[i]

    print( vetor_matriz_rot_givens( vetor, pos_entradas[0], pos_entradas[1] ) )