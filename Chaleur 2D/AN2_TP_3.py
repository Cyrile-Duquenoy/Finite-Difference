import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d

######## VALEURS FIXES #############

tf=5
nt=10
T=np.linspace(0,tf,nt)
N=5
T_rad=40
u0=20

X=Y=np.linspace(0,1,N)

######## Fonctions utiles ###########


            

######## FONCTIONS ##################

def Mat(N):
    return np.ones((N,N))*u0
    
def T_ext(M,X,Y):
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i]==0 and 0.4<=Y[j]<=0.6:
                M[i][j]=5
    return M

def pos_rad(x1,x2,y1,y2):
    return x1,x2,y1,y2

def omega(x1,y1,x2,y2,M): #Placement du radiateur
    if 0<x1<len(M) and 0<x2<len(M) and 0<y1<len(M[0]) and 0<y2<len(M[0]):
        for i in range(x1,x2):
            for j in range(y1,y2):
                M[i][j]=T_rad
        return M
    else :
        print('Radiateur en dehors de la zone autorisée')

########################## MAIN ###############################################

                    ##################
                    ## Au temps t=0 ##
                    ##################
def piece_init():
    M=Mat(N)
    Rad=pos_rad(1,2,3,4)
    M=omega(Rad[0],Rad[1],Rad[2],Rad[3],M)
    M=T_ext(M,X,Y)
    return M 

M=piece_init()
print(M)


                ## Graphe ##
                
X, Y = np.meshgrid(X,Y)
Z=M

#Activation des axes tridimensionnelles.
fig = plt.figure()
ax=plt.axes(projection='3d')

#Syntaxe for plotting.
ax.plot_surface(X,Y,Z, cmap='viridis')
ax.set_title('Condition initiale u_0(x,y)')
plt.show()

###############################################################################

                    #############################
                    ## Iterations jusqu"a tf=5 ##
                    #############################

                    



