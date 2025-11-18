import numpy as np
import matplotlib.pyplot as plt

# 1. Define the circle (e.g., unit circle for reference)
theta = np.linspace(0, 2 * np.pi, 100)
circle_x = np.cos(theta)
circle_y = np.sin(theta)

# 2. Define your modal vectors (complex numbers)
# For demonstration, let's create some example complex mode shape components
modal_vectors_complex = np.array([
    0.8 + 0.2j,
    0.5 - 0.5j,
    -0.7 + 0.1j,
    -0.3 - 0.6j
])

# Extract real and imaginary parts for plotting
modal_vectors_real = np.real(modal_vectors_complex)
modal_vectors_imag = np.imag(modal_vectors_complex)

# 3. Create the plot
fig, ax = plt.subplots(figsize=(7, 7))

# Plot the circle
ax.plot(circle_x, circle_y, 'k--', label='Unit Circle')

# Plot the modal vectors using quiver
# The 'quiver' function takes (origin_x, origin_y, vector_x_component, vector_y_component)
ax.quiver(
    np.zeros_like(modal_vectors_real),  # Origin x-coordinates (all at 0)
    np.zeros_like(modal_vectors_imag),  # Origin y-coordinates (all at 0)
    modal_vectors_real,                 # Vector x-components
    modal_vectors_imag,                 # Vector y-components
    angles='xy', scale_units='xy', scale=1, color='b', label='Modal Vectors'
)

# Customize the plot
ax.set_aspect('equal', adjustable='box')  # Ensure circular aspect ratio
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_title('Circle Plot of Modal Vectors (Complex Plane)')
ax.grid(True)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.legend()

# Show the plot
plt.show()