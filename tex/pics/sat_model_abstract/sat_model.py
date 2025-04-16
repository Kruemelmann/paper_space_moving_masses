import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def zylinder(radius, hoehe, z_offset=0, aufloesung=50):
    """Erzeugt die Koordinaten für die Mantelfläche eines Zylinders."""
    theta = np.linspace(0, 2 * np.pi, aufloesung)
    z = np.linspace(z_offset, z_offset + hoehe, 2)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y, z

# Großer Zylinder (transparent)
groß_radius = 1
groß_hoehe = 4
x1, y1, z1 = zylinder(groß_radius, groß_hoehe)

# Kleiner Zylinder (undurchsichtig)
klein_radius = 0.8
klein_hoehe = groß_hoehe / 4
x2, y2, z2 = zylinder(klein_radius, klein_hoehe)

# Plot vorbereiten
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Großer Zylinder (halbtransparent, keine Kanten)
ax.plot_surface(x1, y1, z1, color='lightblue', alpha=0.3, edgecolor='none')

# Kleiner Zylinder (blickdicht, keine Kanten)
ax.plot_surface(x2, y2, z2, color='orange', alpha=1.0, edgecolor='none')

# Ansicht & Achsen
ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])
ax.set_zlim([0, groß_hoehe])
ax.view_init(elev=30, azim=45)

ax.set_box_aspect([1, 1, groß_hoehe / groß_radius])  # Schönes Seitenverhältnis
ax.set_title("Blick in Zylinder mit innerem Kern")

plt.tight_layout()
plt.show()
