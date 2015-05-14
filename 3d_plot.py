#Physics 91SI - Lab 7, Part 1

#A walk-through exercise in producing quality plots
#We will import some pre-generated data and we have some pre-written code below
#We will see how the data plots as is, with relatively little options activated, 
#and explore how to make the plot more readable and overall better


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cPickle as pickle
from matplotlib import cm


def main():

    #Some pre-generated data saved as a Pickle
    #diffs is 3D array

    f = open('diffs.pickl','r')
    diffs = pickle.load(f)
    #should have f.close(), but...



    #x, y, and z are the variables related to the dimensions of diffs

    file_x = open("x_array.pickl",'r')
    file_y = open("y_array.pickl",'r')
    file_z = open("z_array.pickl",'r')
    
    x_array = pickle.load(file_x)
    y_array = pickle.load(file_y)
    z_array = pickle.load(file_z)
    


    #Our plot is only going to look at a subset of the total 3D array
    #These are the ranges we will include, and these lists are referenced later in the code

    x_array_indices = range(100,161)
    y_array_indices = range(9,35)
    z_array_indices = range(50)
    
    
    
    #Here we create our figure object, and add an axes object to the figure, note the projection='3d'

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    

    #These are lists that will separate the points in the array where the value is positive, vs negative
    pos_x=[]
    pos_y=[]
    pos_z=[]
    neg_x=[]
    neg_y=[]
    neg_z=[]
    
    
    c_sparse=1
    #c_sparse sets how many values are skipped when plotting along the x and z ranges (y has been left alone so far)
    for i_y in range(len(y_array_indices)):
        for i_z in [c_sparse*i for i in range(len(z_array_indices)/c_sparse)]:
            for i_x in [c_sparse*i for i in range(len(x_array_indices)/c_sparse)]:
            #The above 2 for loops use something called list comprehensions, we'll get to that next week, so don't worry too much about them
    
                #We want to get the average value of the array elements in the range that we'll represent with just a single point
                mean_mu = np.mean( diffs[i_z:i_z + c_sparse , i_y , i_x:i_x + c_sparse] )
    
                if mean_mu > 0:
                    pos_x.append(np.log10(np.mean(x_array[x_array_indices[i_x:i_x+c_sparse]])))
                    pos_y.append(y_array[y_array_indices[i_y]])
                    pos_z.append(np.mean(z_array[z_array_indices[i_z:i_z+c_sparse]]))
                #do nothing if mean == 0.  not too important a point
                if mean_mu < 0:
                    neg_x.append(np.log10(np.mean(x_array[x_array_indices[i_x:i_x+c_sparse]])))
                    neg_y.append(y_array[y_array_indices[i_y]])
                    neg_z.append(np.mean(z_array[z_array_indices[i_z:i_z+c_sparse]]))
    
    	
    
    #Add two scatter plots to our set of axes, one of the positive values, and one of the negative values
    ax.scatter(pos_x,pos_y,pos_z,s=50,c='g',marker='^')
    ax.scatter(neg_x,neg_y,neg_z,s=50,c='r',marker='v')

    
    ax.set_xlim3d(np.log10(x_array[x_array_indices[0]]),np.log10(x_array[x_array_indices[-1]]))
    ax.set_ylim3d(y_array[y_array_indices[0]],y_array[y_array_indices[-1]])
    ax.set_zlim3d(z_array[z_array_indices[0]],z_array[z_array_indices[-1]]) 
    
    ax.set_xlabel('Log_x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Difference plot')
    
    fig.savefig('figure1.png')
    
    plt.show()

if __name__ == "__main__":
	main()

