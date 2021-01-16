import numpy as np

v = np.arange( 1000 )**2

print( "\n-------------------------------------------------------------------------------\n" )

print( "Resposta: {}".format( np.linalg.norm( v, 1 ) ) )
