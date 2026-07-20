# first install py -3.14 -m pip install matplotlib in window powershell
# import matplotlib.pyplot as plt 
# import numpy as np 
# xpoints=np.array([0,6])
# ypoints=np.array([0,250])
# plt.plot(xpoints,ypoints)
# plt.show()
# import matplotlib.pyplot as plt 
# import numpy as np 
# xpoints=np.array([1,8])
# ypoints=np.array([3,10])
# plt.plot(xpoints,ypoints)
# plt.show()
# import matplotlib.pyplot as plt 
# import numpy as np
# xpoints=np.array([1,8])
# ypoints=np.array([3,10])
# plt.plot(xpoints,ypoints,'o')
# plt.show()
# import sys
# import matplotlib
# # matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.random.normal(170,10,250)
# plt.hist(x)
# plt.show()
# import matplotlib.pyplot as plt
# import  numpy as np 
# xpoints=np.array([1,2,6,8])
# ypoints=np.array([3,8,1,10])
# plt.plot(xpoints,ypoints)
# plt. show()
# import matplotlib.pyplot as plt
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints)
# plt.show() 
# import matplotlib.pyplot as plt # here i made a marker
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,marker="o")
# plt.show() 
# import matplotlib.pyplot as plt 
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,marker="*") # .point,,pixel,x,+,ssqure,Ddiamond,ppantagon,HHexagon,vTriangle Down,
# plt.show()
# import matplotlib.pyplot as plt  # fmt marker link color
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,'o:r') # color g for green, b blue,c cyan,m megenta,
# plt.show()
# import matplotlib.pyplot as plt # marker size 
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,'ob')
# plt.show() 
# import matplotlib.pyplot as plt # marker size 
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,marker="o",ms=20)
# plt.show()
# import matplotlib.pyplot as plt # marker size  for dotted line
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,linestyle='dotted')
# plt.show() 
# import matplotlib.pyplot as plt # marker size  for dashed line
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,linestyle='dashed')
# plt.show() 
# import matplotlib.pyplot as plt # for line width
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints,linewidth='20.5')
# plt.show() 
# import matplotlib.pyplot as plt #for multiple line 
# import  numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# xpoints=np.array([6,2,7,11,5,4])
# plt.plot(ypoints)
# plt.plot(xpoints)

# plt.show() 
# import matplotlib.pyplot as plt #for many lines by adding point for x and y
# import  numpy as np
# x1=np.array([3,8,1,10,5,7])
# y1=np.array([6,2,7,11,5,4])
# x2=np.array([0,1,2,3,4,5])
# y2=np.array([6,7,4,3,9,2])
# plt.plot(x1,y1,x2,y2)
# plt.show() 
# import matplotlib.pyplot as plt # label
# import  numpy as np
# x=np.array([3,8,1,10,5,7])
# y=np.array([6,2,7,11,5,4])
# plt.plot(x,y)
# plt.xlabel("Average pulse")
# plt.ylabel("Calorie Burnage")


# plt.show() 
# import matplotlib.pyplot as plt # title 
# import  numpy as np
# x=np.array([3,8,1,10,5,7])
# y=np.array([6,2,7,11,5,4])
# plt.plot(x,y)
# plt.title("Sports watch Data")
# plt.xlabel("Average pulse")
# plt.ylabel("Calorie Burnage")
# plt.show() 
# import matplotlib.pyplot as plt # font size 
# import  numpy as np
# x=np.array([3,8,1,10,5,7])
# y=np.array([6,2,7,11,5,4])
# font1={'family':'serif','color':'blue','size':20}
# font2={'family':'serif','color':'darkred','size':15}
# plt.title("sport watch Data",fontdict=font1)
# plt.xlabel("Average pulse",fontdict=font2)
# plt.ylabel("Calorie Burnage",fontdict=font2)
# plt.plot(x,y)
# plt.show() 
# import matplotlib.pyplot as plt # title position
# import  numpy as np
# x=np.array([3,8,1,10,5,7])
# y=np.array([6,2,7,11,5,4])
# plt.plot(x,y)
# plt.title("Sports watch Data" ,loc='left')
# plt.xlabel("Average pulse")
# plt.ylabel("Calorie Burnage")
# plt.show() 
# import matplotlib.pyplot as plt # Adding grid
# import  numpy as np
# x=np.array([3,8,1,10,5,7])
# y=np.array([6,2,7,11,5,4])

# plt.title("Sports watch Data")
# plt.xlabel("Average pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x,y)
# plt.grid()
# plt.show()
# import matplotlib.pyplot as plt # specify which grid line to display
# import  numpy as np
# x=np.array([3,8,1,10,5,7])
# y=np.array([6,2,7,11,5,4])

# plt.title("Sports watch Data")
# plt.xlabel("Average pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x,y)
# plt.grid(axis='x')
# plt.show() 
# import matplotlib.pyplot as plt # two graph side by side
# import  numpy as np
# x=np.array([0,1,2,3])
# y=np.array([10,20,30,40])
# plt.subplot(1,2,1)
# plt.plot(x,y)
# x=np.array([1,2,4,6])
# y=np.array([3,8,1,10])
# plt.subplot(1,2,2)
# plt.plot(x,y)
# plt.show()
# import matplotlib.pyplot as plt # two graph on top of each other
# import  numpy as np
# x=np.array([0,1,2,3])
# y=np.array([10,20,30,40])
# plt.subplot(2,1,1)
# plt.plot(x,y)
# x=np.array([1,2,4,6])
# y=np.array([3,8,1,10])
# plt.subplot(2,1,2)
# plt.plot(x,y)
# plt.show()
# import matplotlib.pyplot as plt # Draw 6 plot and add tile
# import  numpy as np
# x=np.array([0,1,2,3])
# y=np.array([10,20,30,40])
# plt.subplot(2,3,1)
# plt.plot(x,y)
# plt.title("sales")
# x=np.array([1,2,4,6])
# y=np.array([3,8,1,10])
# plt.subplot(2,3,2)
# plt.plot(x,y)
# plt.title("sales")
# x=np.array([1,2,4,6])
# y=np.array([3,8,1,10])
# plt.subplot(2,3,3)
# plt.plot(x,y)
# plt.title("sales")
# x=np.array([1,2,4,6])
# y=np.array([3,8,1,10])
# plt.subplot(2,3,4)
# plt.plot(x,y)
# plt.title("sales")
# x=np.array([1,2,4,6])
# y=np.array([3,8,1,10])
# plt.subplot(2,3,5)
# plt.plot(x,y)
# plt.title("sales")
# x=np.array([1,2,4,6])
# y=np.array([3,8,1,10])
# plt.subplot(2,3,6)
# plt.plot(x,y)
# plt.plot(x,y)
# plt.title("sales")
# plt.suptitle("My shope")
# plt.show()
# import matplotlib.pyplot as plt #for scatter graph
# import  numpy as np
# x=np.array([3,8,1,10,5,7])
# y=np.array([6,2,7,11,5,4])
# plt.scatter(x,y,)
# plt.show() 
# import matplotlib.pyplot as plt #bar chat
# import  numpy as np
# x=np.array(["A","B","C","D","E","F"])
# y=np.array([6,2,7,11,5,4])
# plt.bar(x,y,)
# plt.show()
# import matplotlib.pyplot as plt # Draw 6 horizontal bar chat
# import  numpy as np
# x=np.array(["A","B","C","D","E","F"])
# y=np.array([6,2,7,11,5,4])
# plt.barh(x,y,)
# plt.show()
# import matplotlib.pyplot as plt #bar chat color
# import  numpy as np
# x=np.array(["A","B","C","D","E","F"])
# y=np.array([6,2,7,11,5,4])
# plt.bar(x,y, color="red")
# plt.show()
# import matplotlib.pyplot as plt #bar chat width
# import  numpy as np
# x=np.array(["A","B","C","D","E","F"])
# y=np.array([6,2,7,11,5,4])
# plt.bar(x,y, width=0.1)
# plt.show()
# import matplotlib.pyplot as plt #bar chat height 
# import  numpy as np
# x=np.array(["A","B","C"])
# y=np.array([6,2,7])
# plt.barh(x,y,height=0.1)
# plt.show()
# import matplotlib.pyplot as plt #historical
# import  numpy as np
# x=np.random.normal(170,10,250)
# plt.hist(x)
# plt.show()
# import matplotlib.pyplot as plt #pie chat
# import  numpy as np
# y=np.array([6,2,7,11,5,4])
# plt.pie(y)
# plt.show()
# import matplotlib.pyplot as plt #label for pie chat 
# import  numpy as np
# y=np.array([6,2,7,11])
# mylabels=["Apple","Bannana","Cherries","Dates"]
# plt.pie(y, labels=mylabels)
# plt.show()
# import matplotlib.pyplot as plt #start the first wedge at 90 degree 
# import  numpy as np
# y=np.array([6,2,7,11])
# mylabels=["Apple","Bannana","Cherries","Dates"]
# plt.pie(y, labels=mylabels,startangle=90)
# plt.show()
# import matplotlib.pyplot as plt # explode and shadow
# import  numpy as np
# y=np.array([6,2,7,11])
# mylabels=["Apple","Bannana","Cherries","Dates"]
# myexplode=[0.2,0,0,0]
# plt.pie(y, labels=mylabels,explode=myexplode,shadow=True)
# plt.show()
# import matplotlib.pyplot as plt # colors for pie chart
# import  numpy as np
# y=np.array([6,2,7,11])
# mylabels=["Apple","Bannana","Cherries","Dates"]
# mycolor=["black","green","red","white"]

# plt.pie(y, labels=mylabels,colors=mycolor)
# plt.show()

import matplotlib.pyplot as plt # explode and shadow
import  numpy as np
y=np.array([6,2,7,11])
mylabels=["Apple","Bannana","Cherries","Dates"]
plt.pie(y, labels=mylabels)
plt.legend(title="Four fruit")
plt.show()




 







