import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D

def readPDBfile(filename):

    '''read a PDB file, extract the ATOM lines, and return
       atom number, atom name, residue number, and coords for each'''
    # build them up in lists because they are cheap to append
    #don't know how big the array would otherwise need to be; this just makes the size needed. 
    anum = []
    aname = []
    resno = []
    coords = []
    # open the file and process each line
    # your work goes here
    for line in filename.readlines():
        if line [:6] == 'ATOM  ':
            num=int(line[6:11])
            anum.append(num)
            name=line[12:16]
            aname.append(name)
            resn=int(line[22:26])
            resno.append(resn)
            coord=[float(line[30:38]),float(line[38:45]),float(line[46:54])]
            coords.append(coord)
    # convert the results to numpy arrays
    anum = np.array(anum)
    coords = np.array(coords)
    resno = np.array(resno)

    # return the 4 results
    return (anum, aname, resno, coords)
    #return the tuple with four things inside of it. 
pdb_file=file('7HVP.pdb','r')
aname, anum, resn, coords = readPDBfile(pdb_file)

def drawCA(anum, coords):
    i=0
    '''plot the Calpha backbone of an atom'''
    fig = pylab.figure()
    x=[]
    y=[]
    z=[]
    # your work goes here
    for line in anum:
		if line[:4] == ' CA ':
            for x,y,z in coords[i]:
                xcoord=coords[i,0]
                x.append(xcoord)
                print x
                ycoord=coords[i,1]
                y.append(ycoord)
                print y
                zcoord=coords[i,2]
                z.append(zcoord)
                print z
                ax=Axes3D(fig)
                ax.plot(x,y,z) # x, y, and z are 1D arrays giving the coordinates of the points
                pylab.show()
        return fig, x, y, z
    i=i+1
drawCA(aname,coords)
       
   # here is a helper I wrote to make your job easier in Hbonds
def atomType(aname):
   # pairs[1]
   # pairs[2]
   # def distance(p0,p1):
    #    return np.sqrt(np.sum(p0 -p1)**2)
   # for i,p in enumerate(atomType(aname)):
        if (p==("N" or "O") and q==("N" or "O")) and (2.6 <= distance (coords [i,:], coords[j,:]) <=3.2) and ((resno[i] - resno[j] >=2)) and ((resn[i] - resn[j]) >= 2 or ((resn[i] - resn[j]) <=2):
            
        
    '''Get the 2nd character of all the atom names'''
    # this is trickier than it should, ideally, be. Unfortunately, numpy arrays of
    # strings don't slice like (I think) they should. So I'm converting the array of
    # strings to an array of characters view(), reshaping that flattened result into a
    # 2D array of characters N x 4. Extracting the character at index 1 from each of them.
   # return aname.view(dtype='S1').reshape((-1,4))[:,1]