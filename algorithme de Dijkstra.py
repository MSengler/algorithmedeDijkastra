import numpy as np

GPS = np.array([[0,6,np.inf,np.inf,12,np.inf,5,np.inf,np.inf],
			[np.inf,0,4,np.inf,4,np.inf,np.inf,np.inf,np.inf],
			[np.inf,np.inf,0,4,3,2,np.inf,np.inf,np.inf],
			[np.inf,np.inf,np.inf,0,np.inf,np.inf,np.inf,np.inf,np.inf],
			[np.inf,np.inf,np.inf,2,0,7,np.inf,np.inf,np.inf],
			[np.inf,np.inf,np.inf,3,np.inf,0,np.inf,np.inf,np.inf],
			[np.inf,np.inf,np.inf,np.inf,6,np.inf,0,3,np.inf],
			[np.inf,np.inf,np.inf,np.inf,1,5,np.inf,0,np.inf],
			[np.inf,np.inf,np.inf,np.inf,np.inf,2,np.inf,2,0]])
	
GPS2 = np.array([[0,1,4,4,np.inf],
                [np.inf,0,5,1,5],
                [np.inf,np.inf,0,np.inf,1],
                [np.inf,np.inf,1,0,np.inf],
                [np.inf,np.inf,np.inf,np.inf,0]])


depart = 1
arrivee = 5


def minligne(l):
    min = l[0]
    print()
    j = 0
    for i in range(len(l)):
        if l[i]!=-1 and (min==0 or l[i]<min):
            min = l[i]
            j = i
    return np.array([min,j])



def djikstra(GPS, depart):
    n,_ = GPS.shape
    L = np.array([[i,np.inf]for i in range(0,n)])
    L[depart-1,1] = 0
    trajet = L.copy()

    j = depart-1
    for i in range(len(L)):
        if  GPS[j,i]!= np.inf and np.abs(GPS[j,i]) < np.abs(L[i,1]):
            L[i,1] = GPS[j,i]
            trajet[i,1] =GPS[j,i]
    print(L) 
    for k in range(6):
        minl = minligne(L[:,1])
        minl = minl.astype(int)

        j = minl[1]
        d = minl[0]
        #print(j, d)
        L[j,1] = -1

        for i in range(len(L)):
            if  GPS[j,i]!= np.inf and np.abs(GPS[j,i])+d < np.abs(L[i,1]):
                L[i,1] = GPS[j,i]+d
                trajet[i,1] = GPS[j,i]+d

    print(trajet)
        


