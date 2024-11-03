import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d

                                ##############
                                ## TP 2 ######
                                ## PARTIE B ## 
                                ##############

N=10
nt=100
tf=0.01
t=np.linspace(0,tf,nt)

dx=dy=1/N #Pas d'espace en x et en y
dt=tf/(nt) #pas en temps
lx=dt/(dx**2) #lambda_x
ly=dt/(dy**2) #lambda_y

def u0(x,y): #Donne u(x,y,0) la condition initiale
    if (0.4 <= x <= 0.6) and (0.4 <= y <= 0.6):
        return 1
    else:
        return 0

def A0(): #Donne U0=u(x,y,0)
    A=np.zeros((N+1,N+1))
    x=y=np.linspace(0,1,N+1)
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j]=u0(x[i],y[j])
    return A

'''
def Mat(N): #Matrice de Discretisation (A REFAIRE !!!!)
    M=np.zeros((N+1,N+1))
    
    for j in range(len(M)):
        M[j][j]=1+2*(lx+ly)
        if j < len(M)-1:
            M[j][j+1]=-lx 
        if j >= 1:
            M[j][j-1]=-lx
    return M
'''


def Mat(N):
    p=N+1
    m=N+1
    M=np.zeros((m*p,m*p))
    for i in range(len(M)):
        for j in range(len(M[i])):
            
            k=(j-1)*m+i
            
            if i==j:
                M[i][j]=1-2*(lx+ly)
            if i<m-1:
                M[i][i+1]=-lx
            if i >=1:
                M[i][i-1]=-lx
                
            '''
            if i<N+1:
                M[k][k+1]=-lx
            if i>=1:
                M[k][k-1]=-lx
                
            ## Fonctionne pas à partir d'ici !!!!
            if j<p and j>0:
                M[k][k+p]=-ly
            if j>=1:
                M[k][k-p]=-ly
            '''
            
            if j>1:
                M[k][k-m]=-ly
            
            
    return M


      
'''
def Mat(N):
    M=np.zeros((N+1,N+1))
    for i in range(1,len(M)-1):
        for j in range(1,len(M[i])-1):
            k=(j-1)*N+i
            if i<N-1:
                M[k][k+1]=-lx
            if i>=1:
                M[k][k-1]=-lx
            if j<N-1:
                M[k][k+N]=-ly
            if j>=1:
                M[k][k-N]=-ly
            M[i][i]=1-2*(lx+ly)
    return M
'''

def Un(A0,M0,t): #Donne Un=u(x,y,t)
    B=[A0]               
    for i in range(len(t)):                 
        A0=np.dot(np.linalg.inv(M0),A0)
        B.append(A0)
    return B

###############################################################################

A=A0()
print(A,'\n') #Affiche matrice condition initiale.

M=Mat(N)
print(M) #Affiche matrice de Discretidation.

B=Un(A,M,t)

###############################################################################
############################## GRAPHE #########################################

x=y=np.linspace(0,1,N+1)
X,Y = np.meshgrid(x,y)
Z=B[nt]

#Activation des axes tridimensionnelles.
fig = plt.figure()
ax=plt.axes(projection='3d')

#Syntaxe for plotting.
ax.plot_surface(X,Y,Z, cmap='viridis')
ax.set_title('u(x,y,t)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
