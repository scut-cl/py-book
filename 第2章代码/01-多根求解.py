import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
#先确定字体，以免无法识别汉字
my_font = font_manager.FontProperties(fname=  "C:/Windows/Fonts/msyh.ttc")
X=np.linspace(0,60,600)
plt.figure(figsize=(15,5))
Y = X-0.5-4*X*np.sin(X)
plt.xlabel(u'X数值',fontproperties=my_font)
plt.ylabel(u'Y数值',fontproperties=my_font)
plt.title(u"函数图像",fontproperties=my_font,fontsize=16)
plt.plot(X,Y,label=u"多根求解函数")
plt.xlim(0,60)
plt.legend(prop=my_font)
plt.grid()
plt.show()
