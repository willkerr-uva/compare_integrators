from gqconstants import HighPrecisionGaussInt
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x)

#trapezoid
def trap(f, a, b, N):
    x = np.linspace(a, b, N)
    h = (b-a)/(N-1)
    y=f(x)
    return h*(.5*y[0]+np.sum(y[1:-1])+.5*y[-1])

#simpson
def simp(f, a, b, N):
    x = np.linspace(a, b, N)
    h = (b-a)/(N-1)
    y=f(x)
    return (h/3)*(y[0]+4*np.sum(y[1:-1:2])+2*np.sum(y[2:-2:2])+y[-1])

#gauss
def gauss(f, a, b, N):
    gq = HighPrecisionGaussInt(N)
    return gq.integ(f, a, b)

a, b = 0.0, 1.0
val = 1-f(-1)
Ns = [2, 10, 20, 40, 80, 160, 320, 640, 1280]
trap_err, simp_err, gauss_err = [], [], []

for N in Ns:
    t = trap(f, a, b, N)
    s = simp(f, a, b, N)
    g = gauss(f, a, b, N)
    trap_err.append(abs((t-val)/val))
    simp_err.append(abs((t-val)/val))
    gauss_err.append(abs((t-val)/val))

#table
print("N\tE_trap\tE_simp\tE_gauss")
for i, N in enumerate(Ns):
    print(f"{N}\t{trap_err[i]:.3e}\t{simp_err[i]:.3e}\t{gauss_err[i]:.3e}")

#log plot
plt.figure(figsize=(8,6))
plt.loglog(Ns, trap_err, 'o-', label="Trapezoid")
plt.loglog(Ns, simp_err, 's-', label="Simpson")
plt.loglog(Ns, gauss_err, '^-', label="Gaussian")
plt.xlabel("Number of points N")
plt.ylabel("Relative error")
plt.title("Relative Error vs N (Log-Log)")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.savefig("Errors.png")
plt.show()
