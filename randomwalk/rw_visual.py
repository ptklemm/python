import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

ax.set_title(f"Random Walk n={rw.num_points}", fontsize=24)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)

plt.savefig('saved_plots/random_walk.png', bbox_inches='tight')
plt.show()