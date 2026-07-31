# import numpy
# import matplotlib.pyplot as plt
# x=numpy.random.uniform(0.0,5.0,250)
# plt.hist(x,5)
# plt.show()
#  Normal distribution 
# import numpy
# import matplotlib.pyplot as plt
# x=numpy.random.normal(5.0,1.0,100000)
# plt.hist(x,100)
# plt.show()
#  we use the array from the numpy.random.normal() method with 100000 values, to draw a histogram with 100 
#  bars we specify taht the mean value is 5.0 and the standard deviation is 1.0 . Meaning that the values should 
#  concentrated around 5.0 and rarely further away than 1.0 from the mean . And as you see from the histogram most 
#  value are between 4.0 and 6.0 with a top at approximately 5.0
#   Regression 
# import matplotlib.pyplot as plt 
# x=[5,7,8,9]
# y=[99,85,67,77]
# plt.scatter(x,y)
# plt.show()
import matplotlib.pyplot as plt 
from scipy import stats 
# create an array that represent the value of the x-axis and y-axis 
x=[5,7,8,7]
y=[99,88,77,66]
slope,intercept,r,p,std_err=stats.linregress(x,y)
#  Execute a method that return some important key values of linear regression 
def myfunc(x):
    return slope*x+intercept
    #  Create a function that uses the slope and intercept values to return a new values . THis  new value 
    #  represent where on y-axis the corresponding x value will be placed
    mymodel=list(map(myfunc,x))
    #  Run each value of the x array through the function. This will result in a new with new values for the y-axis
    plt.scatter(x,y)
    #  Draw the original scatter plot
    plt.plot(x,mymodel)
    #  Draw the line of linear regression 
    plt.show()
    #  display the diagram
    

