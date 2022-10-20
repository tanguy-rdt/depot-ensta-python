

import matplotlib.pyplot as plt
import matplotlib.patches as patches
plt.figure()
ax = plt.gca()
p1 = patches.FancyArrowPatch((0.1, 0.1), (0.9, 0.9),
                             arrowstyle='<->', mutation_scale=20)
ax.add_patch(p1)
plt.show()


