import numpy as np
import matplotlib.pyplot as plt

G = 1.0  # Gravitationskonstante (vereinfacht)
M = 1000.0  # Masse des zentralen Körpers (z. B. Planet)
m_body = 9.0  # Masse der Zylinderhülle
m_payload = 1.0  # Masse des verschiebbaren Gewichts

# Länge des Zylinders (zur Berechnung des Schwerpunkts)
cylinder_length = 2.0  # Einheit: willkürlich

# Simulationsparameter
dt = 0.01  # Zeitschritt
steps = 1000  # Simulationsdauer

def simulate_orbit(payload_offset_from_center):
    # Startwerte
    pos = np.array([10.0, 0.0])  # Startposition
    vel = np.array([0.0, 3.0])   # Startgeschwindigkeit tangential

    positions = []

    for _ in range(steps):
        # Vektor zum Zentrum
        to_center = -pos
        r = np.linalg.norm(to_center)
        direction = to_center / r

        # Radiale Ausrichtung: payload liegt entlang -direction (zum Planeten)
        # Offset wird entlang dieser Richtung aufgetragen
        payload_pos = pos + direction * payload_offset_from_center

        # Schwerpunkt berechnen
        total_mass = m_body + m_payload
        center_of_mass = (m_body * pos + m_payload * payload_pos) / total_mass

        # Gravitationskraft wirkt auf den Schwerpunkt
        to_center_com = -center_of_mass
        r_com = np.linalg.norm(to_center_com)
        grav_dir = to_center_com / r_com
        force = G * M * total_mass / r_com**2 * grav_dir

        # Beschleunigung auf den Schwerpunkt
        acc = force / total_mass

        # Schwerpunkt aktualisieren → Bewegung überträgt sich auf pos
        vel += acc * dt
        pos += vel * dt

        positions.append(pos.copy())

    return np.array(positions)

# Drei Simulationen mit unterschiedlicher Payload-Position:
# 1. mittig, 2. näher zum Planeten, 3. weiter weg
traj_centered = simulate_orbit(payload_offset_from_center=0.0)
traj_downward = simulate_orbit(payload_offset_from_center=-cylinder_length/2)
traj_upward = simulate_orbit(payload_offset_from_center=+cylinder_length/2)

# Plot
plt.figure(figsize=(8, 8))
plt.plot(traj_centered[:, 0], traj_centered[:, 1], label="Payload mittig")
plt.plot(traj_downward[:, 0], traj_downward[:, 1], label="Payload planetennah")
plt.plot(traj_upward[:, 0], traj_upward[:, 1], label="Payload planetenfern")
plt.plot(0, 0, 'ko', label="Zentralkörper (fix)")
plt.legend()
plt.axis('equal')
plt.title("Orbitvergleich bei unterschiedlicher Lage des internen Gewichts")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.xlim(-5, 15)
plt.ylim(-10, 10)
plt.show()
