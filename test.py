"""
This file contains an example of how to use FrisPy to visualize a simulated trajectory.
"""
import __init__

# Some example initial conditions are in simple_initial_conditions.txt, located a the top level of this repository.
disc = __init__.create_disc(filename = "simple_initial_conditions.txt")
times, trajectory = __init__.get_trajectory(disc)

#Try plotting
try:
    import matplotlib.pyplot as plt
    x,y,z = trajectory.T
    plt.plot(x, z)
    plt.title("Simulated Trajectory of a Frisbee")
    plt.text(2, 0.4, "x=0 y=1.2 vx=17.92 vy=1.26, theta=4")
    plt.xlabel("distance [meters]")
    plt.ylabel("height [meters]")
    plt.show()
except Exception:
    print("Matplotplot not installed. Cannot visualize example.")
