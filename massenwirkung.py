import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from matplotlib.widgets import Slider

def mw(t,x,k_p=1,k_n=2):
    return [k_n*x[2]-k_p*x[0]*x[1],k_n*x[2]-k_p*x[0]*x[1],k_p*x[0]*x[1]-k_n*x[2]]

ys=integrate.solve_ivp(mw,[0,1],[10,5,0],t_eval=np.linspace(0,1,100))
#ys=integrate.solve_ivp(mw,[0,1],[10,5,0],t_eval=np.linspace(0,1,100))

fig,ax=plt.subplots()
line_A,=ax.plot(ys.t,ys.y[0,:])
line_B,=ax.plot(ys.t,ys.y[1,:])
line_C,=ax.plot(ys.t,ys.y[2,:])
ax.set_ylim([0,12])
fig.subplots_adjust(bottom=0.25)
axk1=fig.add_axes([0.25,0.1,0.65,0.03])
axk2=fig.add_axes([0.25,0.15,0.65,0.03])
k1_slider=Slider(ax=axk1,label="k1",valmin=0,valmax=2,valinit=1)
k2_slider=Slider(ax=axk2,label="k2",valmin=0,valmax=2,valinit=1)

def update(val):
    ys=integrate.solve_ivp(lambda t,x:mw(t,x,k_p=k1_slider.val,k_n=k2_slider.val),[0,1],[10,5,0],t_eval=np.linspace(0,1,100))
    line_A.set_ydata(ys.y[0,:])
    line_B.set_ydata(ys.y[1,:])
    line_C.set_ydata(ys.y[2,:])
    fig.canvas.draw_idle()

k1_slider.on_changed(update)
k2_slider.on_changed(update)
plt.show()

# Questions:
# 
