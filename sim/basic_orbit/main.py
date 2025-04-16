import numpy as np
import matplotlib.pyplot as plt

# Konstanten
G = 6.67430e-11  # Gravitationskonstante in m^3 kg^-1 s^-2
M = 5.972e24     # Masse der Erde in kg
R_earth = 6371e3 # Erdradius in m
r0 = 7000e3      # Anfangsentfernung des Satelliten in m (z.B. 7000 km)
v0 = 7.5e3       # Anfangsgeschwindigkeit des Satelliten in m/s (z.B. 7,5 km/s)

# Anfangsbedingungen
x0 = r0           # x-Position des Satelliten
y0 = 0            # y-Position des Satelliten
vx0 = 0           # x-Geschwindigkeit des Satelliten
vy0 = v0          # y-Geschwindigkeit des Satelliten

# Zeitparameter
t_max = 2 * np.pi * np.sqrt(r0**3 / (G * M))  # Umlaufzeit (Keplersches Gesetz)
dt = 10         # Zeitschritt in Sekunden
times = np.arange(0, t_max, dt)

# Initialisierung der Positionen und Geschwindigkeiten
positions = []
velocities = []
x, y, vx, vy = x0, y0, vx0, vy0

# Funktion für die Berechnung der Gravitationskraft
def gravitational_force(x, y):
    r = np.sqrt(x**2 + y**2)  # Abstand zum Erdmittelpunkt
    F = -G * M * np.array([x, y]) / r**3  # Gravitationskraft in x- und y-Richtung
    return F

# Runge-Kutta-Integration (4. Ordnung)
for t in times:
    # Berechne Gravitationskraft
    F = gravitational_force(x, y)

    # Runge-Kutta-Methoden für Position und Geschwindigkeit
    k1_vx, k1_vy = F * dt / 2
    k1_x, k1_y = vx * dt, vy * dt

    k2_vx, k2_vy = (F + gravitational_force(x + k1_x / 2, y + k1_y / 2)) * dt / 2
    k2_x, k2_y = (vx + k1_vx / 2) * dt, (vy + k1_vy / 2) * dt

    k3_vx, k3_vy = (F + gravitational_force(x + k2_x / 2, y + k2_y / 2)) * dt / 2
    k3_x, k3_y = (vx + k2_vx / 2) * dt, (vy + k2_vy / 2) * dt

    k4_vx, k4_vy = (F + gravitational_force(x + k3_x, y + k3_y)) * dt
    k4_x, k4_y = (vx + k3_vx) * dt, (vy + k3_vy) * dt

    # Aktualisiere Positionen und Geschwindigkeiten
    x += (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
    y += (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
    vx += (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
    vy += (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6

    positions.append([x, y])
    velocities.append([vx, vy])

# Umwandeln der Positionen in ein numpy Array
positions = np.array(positions)

# Plot der Satellitenbahn
plt.figure(figsize=(8, 8))
plt.plot(positions[:, 0], positions[:, 1], label="Satellitenbahn")
plt.plot(0, 0, 'ro', label="Erde")
plt.title('Satellitenbahn um die Erde')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
