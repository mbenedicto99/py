import matplotlib.pyplot as plt
import numpy as np

def draw_art():
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Círculo externo
    circle = plt.Circle((0, 0), 1, edgecolor='black', facecolor='none', lw=2)
    ax.add_patch(circle)

    # Círculo interno menor
    inner_circle = plt.Circle((0, 0), 0.3, edgecolor='black', facecolor='none', lw=2)
    ax.add_patch(inner_circle)

    # Linhas internas
    angles = np.linspace(0, 2 * np.pi, 12, endpoint=False)  # 6 segmentos
    for angle in angles:
        x1, y1 = 0.3 * np.cos(angle), 0.3 * np.sin(angle)
        x2, y2 = np.cos(angle), np.sin(angle)
        ax.plot([x1, x2], [y1, y2], 'k', lw=2)

    plt.show()

draw_art()
