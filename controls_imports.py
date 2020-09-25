import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import control as ctrl
from ipywidgets import interact
import sympy as sym
from sympy.abc import *
sym.init_printing()
omega= sym.symbols('omega', real = True)
t = sym.symbols('t', positive = True)
s = sym.symbols('s', positive = True)
x = sym.Function('x')
y = sym.Function('y')
f = sym.Function('f')
import numpy.polynomial.polynomial as p
from numpy.polynomial import Polynomial as display_poly
from numpy.polynomial import Polynomial as poly_display
j = complex(0,1)
i = complex(0,1)
from numpy import e, pi


def ctrl_ilt(expr):
    ilt = 0
    expanded = sym.apart(expr).as_ordered_terms()

    print('Expanded this is ', expanded)
    for term in expanded:
        print('Terms are ', term)
        print(sym.inverse_laplace_transform(term, s, t))
        ilt += sym.inverse_laplace_transform(term, s, t)
    return ilt

def sdof_resp(x0=1, v0=0.1, m=1, c=0.25, k=10, tmax=10):
    t = np.linspace(0, tmax, 200)
    omega = np.sqrt(k / m)
    zeta = c / 2 / np.sqrt(m * k)
    if zeta < 1:
        omega_d = omega * np.sqrt(1 - zeta**2)
        X0 = np.sqrt(x0**2 * omega**2 + v0**2 + 2 * x0 * v0 * zeta *
                     omega) / omega_d
        Phi0 = np.arctan2(x0 * omega_d, (v0 + zeta * omega * x0))
        x = X0 * np.exp(-zeta * omega * t) * np.sin(omega_d * t + Phi0)

        expdecay = X0 * np.exp(-zeta * omega * t)
        plt.plot(t, expdecay,'--', label = 'Decay Envelope')
        plt.plot(t, -expdecay, '--')
        plt.text(tmax/3, X0 * np.exp(-zeta * omega * tmax/3) + X0*0.03, 'Decay Envelope, $X_0e^{-\zeta\omega_nt}$')
        period = 2.0 * np.pi/omega_d
        plt.annotate(text='', xy=(1*period,-0.9*X0), xytext=(2*period,-0.9*X0), arrowprops=dict(arrowstyle='<->'))
        plt.text(1.5*period, -X0*1.0, 'Period', ha = 'center')
    else:

        C1 = (x0 * omega * (zeta + np.sqrt(zeta**2 - 1)) + v0
              ) / 2 / omega / np.sqrt(zeta**2 - 1)
        C2 = (-x0 * omega * (zeta - np.sqrt(zeta**2 - 1)) - v0
              ) / 2 / omega / np.sqrt(zeta**2 - 1)
        x = C1 * np.exp(
            (-zeta + np.sqrt(zeta**2 - 1)) * omega * t) + C2 * np.exp(
                (-zeta - np.sqrt(zeta**2 - 1)) * omega * t)
        x_label = C1 * np.exp(
            (-zeta + np.sqrt(zeta**2 - 1)) * omega * tmax/3) + C2 * np.exp(
                (-zeta - np.sqrt(zeta**2 - 1)) * omega * tmax/3)
        plt.axis([0, tmax, -np.abs(C1+C2)*1.1, np.abs(C1+C2)*1.1])
        plt.text(tmax/3, x_label + x[0]*0.03, 'Overdamped response')


    plt.plot(t, np.real(x), label = 'Response')
    plt.xlabel('$t$ (sec)')
    plt.ylabel('$x(t)$ (m)')
    plt.grid(True)
    plt.title('x versus time. $\\zeta = ${:.2f}'.format(zeta))
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.show()
