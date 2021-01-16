import numpy as np

v_1 = np.arange( 1000 )
v = np.arange( 1000 )**v_1

print( "\n-------------------------------------------------------------------------------\n" )

print( "Resposta: {}".format( np.linalg.norm( v, 1 ) ) )
