import numpy as np

def vetor_matriz_householder ( vetor ):
    sinal = np.sign( vetor[0][0] )
    norma = np.linalg.norm( vetor, 2 )
    e = np.zeros( vetor.shape )
    e[0][0] = 1

    if ( sinal == 0 ):
        sinal = 1

    v = vetor + ( sinal * norma * e )

    return np.eye( vetor.shape[0] ) - ( ( 2 / ( v.transpose() @ v ) ) * v @ v.transpose() )


if ( __name__ == "__main__" ):
    vetor_entrada = [ float( x ) for x in input( "Insira os valores do vetor separados por espaço: " ).split( " " ) ]

    vetor = np.zeros( [ len( vetor_entrada ), 1 ] )

    for i in range( len( vetor_entrada ) ):
        vetor[i][0] = vetor_entrada[i]

    print( "-------------------------------------------------------------------------------\n{}".format( vetor_matriz_householder( vetor ) ) )