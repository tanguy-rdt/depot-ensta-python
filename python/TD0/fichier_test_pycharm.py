import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def derive_x(n):
    V = np.ones(n)
    V[-1] = 0
    Vn = np.tile(V, n)
    Vn = Vn[:-1]
    return np.diag(Vn, 1) - np.diag(Vn, -1)


def derive_y(n):
    Vn = np.ones(n * n - n)
    return np.diag(Vn, n) - np.diag(Vn, -n)


def laplacien(n):
    return -4 * np.eye(n * n) + np.abs(derive_x(n)) + np.abs(derive_y(n))


def fonction_F(n, t, a, b, mu):
    X_range = np.linspace(0, 1, n + 2)[1:-1]
    Y_range = np.linspace(0, 1, n + 2)[1:-1]
    # on a de la chance, par défaut meshgrid range
    # les abscisses et les ordonnées pile dans l'ordre
    # dont on a besoin
    x, y = np.meshgrid(X_range, Y_range)
    F = np.pi * np.exp(np.pi * t) * (
        (1 + 2 * np.pi * mu) * np.sin(np.pi * x) * np.sin(np.pi * y) +
        a * np.cos(np.pi * x) * np.sin(np.pi * y) +
        b * np.sin(np.pi * x) * np.cos(np.pi * y)
    )
    return F.flatten()


def U_exact(n, t, return_xy=False):
    X_range = np.linspace(0, 1, n + 2)[1:-1]
    Y_range = np.linspace(0, 1, n + 2)[1:-1]
    x, y = np.meshgrid(X_range, Y_range)
    U = np.exp(np.pi * t) * np.sin(np.pi * x) * np.sin(np.pi * y)
    U = U.flatten()
    if return_xy:
        return x, y, U
    else:
        return U


def A_explicite(n, delta_t, mu, a, b):
    h = 1 / (n + 1)  # sinon jouer avec linspace et retstep
    A = mu * laplacien(n) / (h ** 2)
    A -= a * derive_x(n) / (2 * h)
    A -= b * derive_y(n) / (2 * h)
    A *= delta_t
    A += np.eye(n * n)
    return A


def etude_explicite(n, delta_t, Tmax, mu, a, b, keep_all=False):
    T = np.arange(0, Tmax, delta_t)
    A = A_explicite(n, delta_t, mu, a, b)
    print("Conditionnement de A:", np.linalg.cond(A))

    U = U_exact(n, 0)
    U_list = [U.reshape((n, n))]
    t0 = time.time()

    for t in T[1:]:
        F = fonction_F(n, t, a, b, mu)
        U = A @ U + delta_t * F
        if keep_all:
            U_list.append(U.reshape((n, n)))
    t_solve = time.time() - t0
    print("Temps de résolution:", t_solve)

    if keep_all:
        return T, np.array(U_list)
    else:
        return T[-1], U.flatten()


def err_rel(U_approx, n, T):
    err = []
    for idx in range(len(T)):
        U_sol = U_exact(n, T[idx]).reshape((n, n))
        err.append(np.abs(U_approx[idx] - U_sol) / U_sol)
    return np.array(err)


def update_plot(frame_number, axes, plot, XX, YY, U_list):
    plot[0].remove()
    plot[0] = axes.plot_surface(XX, YY, U_list[frame_number], cmap="magma")


def animate_res(res, n):
    XX, YY, _ = U_exact(n, 0, return_xy=True)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_zlim(0, np.max(res))
    plot = [ax.plot_surface(XX, YY, err[0])]
    # grosse bouse pleine de bugs qui ne marche pas si on n'assigne
    # pas l'animation à une variable @#@@!!$$!!
    _ = animation.FuncAnimation(fig, update_plot, len(res),
                                fargs=(ax, plot, XX, YY, res),
                                interval=10)
    plt.show()


a = 2
b = 1.5
mu = 1
n = 15
h = 1 / (n + 1)
Tmax = 1
delta_t = 0.1 * h * h / mu
# le conditionnement de A explose quand s'approche de la limite
# delta_t = 0.25 * h * h
T, U_approx = etude_explicite(n, delta_t, Tmax, mu, a, b, True)
err = err_rel(U_approx, n, T)

animate_res(U_approx[::10, :, :], n)
# animate_res(err[::10, :, :], n)
print("FIN")