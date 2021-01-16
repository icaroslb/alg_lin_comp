import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( 0.5, 5.5, 100 )

plt.plot( x,  x**5 - ( 15 * x**4 ) + ( 85 * x**3 ) - ( 225 * x**2 ) + ( 274 * x ) - 120 )
plt.plot( x,  0 * x )

plt.savefig( "arquivo_quest_9.png" )

