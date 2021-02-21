import numpy as np
import quest_7

def Q_T_rot_givens( A, m, n ):
    Q = np.eye( m )
    T = A

    for i in range( min( m, n ) - 1 ):
        for j in range( i + 1, min( m, n ) ):
            Q_i = quest_7.vetor_matriz_rot_givens( np.array( [ T[ :, i ] ] ).transpose(), i, j )

            T = Q_i @ T
            Q = Q @ Q_i.transpose()
    
    return Q, T


if ( __name__ == "__main__" ):
    m, n = [ int( x ) for x in input( "Insira as ordens m e n separadas por espaço: " ).split( " " ) ]

    A = np.zeros( [ m, n ] )

    for i in range( m ):
        linha = [ float( x ) for x in input( "Insira a linha {} separadas por espaço: ".format( i ) ).split( " " ) ]
        A[ i, : ] = linha[ 0 : n ]
    
    
    Q, T = Q_T_rot_givens( A, m, n )

    print( "-------------------------------------------------------------------------------\nMatriz Q:\n{}\n\nMatriz T:\n{}\n".format( Q, T ) )