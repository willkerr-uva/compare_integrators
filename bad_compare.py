from gqconstants import HighPrecisionGaussInt
import numpy as np
import matplotlib.pyplot as plt

k = 50
a = 5.0

def f(x):
    return np.exp(-a*x) * np.sin(k * np.pi * x) #(1.0 + x) * np.sin(k * np.pi * x) + c

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
    return float(gq.integ(f, a, b))

a, b = 0.0, 1.0
val = 0.0063597539457
Ns = [3, 11, 21, 41, 81, 161, 321, 641, 1281]
trap_err, simp_err, gauss_err = [], [], []

for N in Ns:
    t = trap(f, a, b, N)
    s = simp(f, a, b, N)
    g = gauss(f, a, b, N)
    trap_err.append(abs((t-val)/val))
    simp_err.append(abs((s-val)/val))
    gauss_err.append(abs((g-val)/val))

#table
print("N\tE_trap\tE_simp\tE_gauss")
for i, N in enumerate(Ns):
    print(f"{N}\t{trap_err[i]:.3e}\t{simp_err[i]:.3e}\t{gauss_err[i]:.3e}")

#slope of errors
def slope(Ns, errs, label):
    logN = np.log10(Ns)
    logE = np.log10(errs)
    m, b = np.polyfit(logN, logE, 1)  # linear fit
    print(f"{label} slope ≈ {m:.2f}")
    return m

print()
print("Slopes:")
slope(Ns, trap_err, "Trapezoid")
slope(Ns, simp_err, "Simpson")

#decimal precision
def digits(errs):
    return [int(np.floor(-np.log10(e))) if e > 0 else 16 for e in errs]

trap_digits = digits(trap_err)
simp_digits = digits(simp_err)
print()
print("Number of digits of precision:")
print("\nN\tTrapezoid\tSimpson")
for i, N in enumerate(Ns):
    print(f"{N}\t{trap_digits[i]}\t\t{simp_digits[i]}")


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
plt.savefig("BadErrors.png")
plt.show()