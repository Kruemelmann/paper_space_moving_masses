import numpy as np
from astropy.constants import G, M_earth

# Physikalische Konstanten
G_value = G.value  # m^3 / (kg s^2)
M = M_earth.value  # kg

# Zylinder-Parameter
m_body = 900.0      # kg
m_payload = 100.0   # kg
cylinder_length = 2.0  # m

# Simulation
dt = 1.0       # Sekunden pro Schritt
steps = 10000  # Simulationsdauer

def simulate_orbit_and_record_distances(payload_offset_from_center):
    pos = np.array([7.0e6, 0.0])  # Startposition (7000 km vom Erdmittelpunkt)
    vel = np.array([0.0, 7500.0])  # Typische Umlaufgeschwindigkeit (m/s)

    distances = []  # Abstand zur Erde bei jedem Zeitschritt

    for _ in range(steps):
        to_center = -pos
        r = np.linalg.norm(to_center)
        direction = to_center / r

        payload_pos = pos + direction * payload_offset_from_center

        total_mass = m_body + m_payload
        center_of_mass = (m_body * pos + m_payload * payload_pos) / total_mass

        to_center_com = -center_of_mass
        r_com = np.linalg.norm(to_center_com)
        grav_dir = to_center_com / r_com
        force = G_value * M * total_mass / r_com**2 * grav_dir

        acc = force / total_mass
        vel += acc * dt
        pos += vel * dt

        # Distanzen zur Erde:
        distance_pos = np.linalg.norm(pos)
        distance_payload = np.linalg.norm(payload_pos)
        distance_com = np.linalg.norm(center_of_mass)

        distances.append((distance_pos, distance_payload, distance_com))

    return np.array(distances)

# Simulation durchführen
distances_centered = simulate_orbit_and_record_distances(0.0)
distances_downward = simulate_orbit_and_record_distances(-cylinder_length / 2)
distances_upward = simulate_orbit_and_record_distances(+cylinder_length / 2)

# Nur Payload-Distanzen extrahieren und in km umrechnen
payload_centered_km = distances_centered[:, 1] / 1e3
payload_downward_km = distances_downward[:, 1] / 1e3
payload_upward_km = distances_upward[:, 1] / 1e3

# CSV-Zeilen generieren
csv_centered = ",".join(f"{v:.3f}" for v in payload_centered_km)
csv_downward = ",".join(f"{v:.3f}" for v in payload_downward_km)
csv_upward = ",".join(f"{v:.3f}" for v in payload_upward_km)

# Ausgabe
print("Payload mittig:")
print(csv_centered)
print("\nPayload planetennah:")
print(csv_downward)
print("\nPayload planetenfern:")
print(csv_upward)
