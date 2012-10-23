#Name: Katie Hawthorne
#Name: Katie Hawthorne
#Collaborators: Alex Bacanu, Emily Bailey

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
    for line in file(filename, 'r'):
        if line[:6] == 'ATOM  ':
            anum.append(int(line[6:11]))
            aname.append(line[12:16])
            resno.append(int(line[22:26]))
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            coords.append((x,y,z))
    # convert the results to numpy arrays
    aname = np.array(aname)
    anum = np.array(anum)
    coords = np.array(coords)
    resno = np.array(resno)
    #aname = np.array(aname)
    # return the 4 results
    return (anum, aname, resno, coords)
    #return the tuple with four things inside of it. 
#pdb_file=file('7HVP.pdb','r')
#aname, anum, resno, coords = readPDBfile(pdb_file)

   
def drawCA(aname, coords):
    x=[]
    y=[]
    z=[]
    '''plot the Calpha backbone of an atom'''
    fig = pylab.figure()
    c = coords[aname == ' CA ']
    x = c[:,0]
    y = c[:,1]
    z = c[:,2]
    fig = pylab.figure()
    ax = Axes3D(fig)
    ax.plot(x,y,z)
    # your work goes here
    return fig
    
      
# here is a helper I wrote to make your job easier in Hbonds

def atomType(anum):
    '''Get the 2nd character of all the atom names'''
    # this is trickier than it should, ideally, be. Unfortunately, numpy arrays of
    # strings don't slice like (I think) they should. So I'm converting the array of
    # strings to an array of characters view(), reshaping that flattened result into a
    # 2D array of characters N x 4. Extracting the character at index 1 from each of them.
    return anum.view(dtype='S1').reshape((-1,4))[:,1]
    
def Hbonds(anum, aname, resno, coords):
    '''Find hydrogen bonds'''
    def distance(p0, p1):
        return np.sqrt(np.sum((p0 - p1)**2))
    pairs = []
    N = np.where((atomType(aname)) == 'N')[0]
    O = np.where((atomType(aname)) == 'O')[0]
    for i, p in enumerate(N):
        for j, q in enumerate(O):
            if ((resno[q] - resno[p] >= 2) or (resno[q] - resno[p] <= -2)) and (2.6 <= distance(coords[q], coords[p]) <= 3.2):
                pairs1 = [anum[O[j]], anum[N[i]]]
                pairs.append(pairs1)
            
    # your work goes here
    return pairs


# now test our functions to see that they do the right thing

for protein in ['7HVP', '1GFL']:
    # extract the data on the atoms from the pdb file
    #for loops go through everything in the list, a "definite loop"
    #goes through both entire files, one first and then the other. 
    
    num, name, rn, c = readPDBfile(protein + '.pdb')
    
    #can return multiple things from a single function and creates it into something different.
    # + operator can put strings together. 

    # draw the Calpha backbone
     
    fig = drawCA(name, c)
    
    # save it in a file
    
    fig.savefig(protein+'.png')

    # get the list of hydrogen bonding pairs
    
    hydrogen_bonding_pairs = Hbonds(num, name, rn, c)

    # and report the number
   
    print 'number of hydrogen bonding pairs in', protein, 'is', len(hydrogen_bonding_pairs)
 
