import numpy as np
import os

import quest_8
import quest_9

if ( __name__ == "__main__" ):
    matriz_3x5 = np.random.rand( 3, 5 )
    matriz_5x5 = np.random.rand( 5, 5 )
    matriz_5x3 = np.random.rand( 5, 3 )
    
    Q_h, T_h = quest_8.Q_T_householder( matriz_3x5, 3, 5 )
    Q_g, T_g = quest_9.Q_T_rot_givens( matriz_3x5, 3, 5 )

    print( "Matriz 3x5 gerada:\n{}\n".format( matriz_3x5 ) )
    input( "Enter para mostrar Householder..." )
    print( "Matriz Q Householder:\n{}\n\nMatriz T Householder:\n{}\n\nQ * T:\n{}\n".format( Q_h, T_h, Q_h @ T_h ) )
    input( "Enter para mostrar Givens..." )
    print( "Matriz Q Givens:\n{}\n\nMatriz T Givens:\n{}\n\nQ * T:\n{}\n".format( Q_g, T_g, Q_g @ T_g ) )
    input( "Enter para continuar..." )
    
    os.system('cls' if os.name == 'nt' else 'clear')

    Q_h, T_h = quest_8.Q_T_householder( matriz_5x5, 5, 5 )
    Q_g, T_g = quest_9.Q_T_rot_givens( matriz_5x5, 5, 5 )

    print( "Matriz 5x5 gerada:\n{}\n".format( matriz_5x5 ) )
    input( "Enter para mostrar Householder..." )
    print( "Matriz Q Householder:\n{}\n\nMatriz T Householder:\n{}\n\nQ * T:\n{}\n".format( Q_h, T_h, Q_h @ T_h ) )
    input( "Enter para mostrar Givens..." )
    print( "Matriz Q Givens:\n{}\n\nMatriz T Givens:\n{}\n\nQ * T:\n{}\n".format( Q_g, T_g, Q_g @ T_g ) )
    input( "Enter para continuar..." )

    os.system('cls' if os.name == 'nt' else 'clear')

    Q_h, T_h = quest_8.Q_T_householder( matriz_5x3, 5, 3 )
    Q_g, T_g = quest_9.Q_T_rot_givens( matriz_5x3, 5, 3 )

    print( "Matriz 5x3 gerada:\n{}\n".format( matriz_5x3 ) )
    input( "Enter para mostrar Householder..." )
    print( "Matriz Q Householder:\n{}\n\nMatriz T Householder:\n{}\n\nQ * T:\n{}\n".format( Q_h, T_h, Q_h @ T_h ) )
    input( "Enter para mostrar Givens..." )
    print( "Matriz Q Givens:\n{}\n\nMatriz T Givens:\n{}\n\nQ * T:\n{}\n".format( Q_g, T_g, Q_g @ T_g ) )