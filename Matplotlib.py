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
import sys
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()
