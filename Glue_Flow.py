import numpy as np
import matplotlib.pyplot as plt
# Function to calculate the stream function for flow over a cylinder
def stream_function(x, y, U, R):
    rsq = x ** 2 + y ** 2
    psi = U * y * ( 1.0 - R ** 2 / rsq )
    return np.where( rsq >= R * R, psi, 0.0 )

# Function to calculate the velocity components (u, v) from the stream function
def velocity_components(x, y, U, R):
    rsq = x ** 2 + y ** 2
    Rsq = R ** 2
    u = U * ( 1 - Rsq / rsq + 2 * Rsq * y ** 2 / ( rsq * rsq ) )
    v = -2 * U * Rsq * x * y / ( rsq * rsq )
    u = np.where( rsq >= Rsq, u, 0.0 )
    v = np.where( rsq >= Rsq, v, 0.0 )
    return u, v

# Function to plot streamlines
def plot_streamlines(ax, X, Y, stream_function, U, R):
    psi = stream_function(X, Y, U, R)
    levels = np.linspace(np.min(psi), np.max(psi), 50)
    ax.contour(X, Y, psi, levels=levels, colors='b' )

# Function to plot velocity vectors
def plot_velocity_vectors(ax, X, Y, velocity_components, U, R ):
    spacing = 5
    x_points = X[::spacing, ::spacing]
    y_points = Y[::spacing, ::spacing]

    psi_x, psi_y = velocity_components(x_points, y_points, U, R)
    ax.quiver(x_points, y_points, psi_x, psi_y, color='r', scale=0.3 )


# Create a figure and axis
fig, ax = plt.subplots()

# Cylinder properties
D = 1.27  # Diameter of the cylinder
R = D / 2  # Radius of the cylinder
U = 0.01  # Fluid velocity

# Set plot limits
ax.set_xlim(-D, D)
ax.set_ylim(-D, D)

# Set aspect ratio to be equal
ax.set_aspect('equal')

# Create a grid for the streamlines
x = np.linspace( -D, D, 200 )
y = np.linspace( -D, D, 200 )
X, Y = np.meshgrid(x, y)

#plot_streamlines( ax, X, Y, stream_function, U, R )

plot_velocity_vectors( ax, X, Y, velocity_components, U, R )
    
ax.set_xlim(-D, D)
ax.set_ylim(-D, D)
ax.set_aspect('equal')
ax.set_title(f'Fluid Flow Over a Cylinder')

plt.show()