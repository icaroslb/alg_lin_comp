import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

figura = plt.figure()
graf = figura.gca( projection='3d' )

x = np.linspace( -1.0, 1.0, 100 )
y = np.linspace( -1.0, 1.0, 100 )
z = np.linspace( -1.0, 1.0, 100 )

graf.plot( x, y, x**2 + y**2 )

plt.savefig( "arquivo_quest_10.png" )

