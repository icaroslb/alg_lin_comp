import numpy as np
import math

def calcular_pi_k ( k ):
	v = np.arange( 1, k )**2
	v = 1 / v
	return math.sqrt( 6 * np.linalg.norm( v, 1 ) )

print( "\n-------------------------------------------------------------------------------\n" )

print( "π 1000: " + str( calcular_pi_k( 1000 ) ) )

k = 2

pi_1 = calcular_pi_k( 1 )
pi_2 = calcular_pi_k( 2 )

while ( abs( pi_1 - pi_2 ) > 0.00001 ):
	pi_1 = pi_2
	k += 1
	
	pi_2 = calcular_pi_k( k )

print( "Com até 5º casa decimal certa, o k = " + str(k) )
