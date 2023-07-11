import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import matplotlib.colors as mcolors

# Define efficiency ranges for each nose cone type
efficiency_ranges = {
    'LV-Haack': [(0.8, 1, 1), (1, 1.2, 3)],
    'Von Karman': [(0.8, 1, 1), (1, 1.2, 2), (1.2, 1.4, 1), (1.4, 1.75, 3), (1.75, 1.9, 2), (1.9, 2.2, 1)],
    'Parabola': [(0.8, 0.9, 1), (0.9, 1.1, 3)],
    '3/4 Parabola': [(0.8, 0.9, 3), (1.3, 1.45, 2), (1.45, 1.95, 1), (1.95, 2.2, 2)],
    '1/2 Parabola': [(1.4, 1.55, 3), (1.55, 2.2, 2)],
    'x^(3/4)': [(0.8, 0.9, 2), (1.45, 1.6, 3), (1.6, 2.2, 2)],
    'x^(1/2)': [(0.8, 0.95, 1), (0.95, 1.05, 2), (1.05, 1.15, 1), (1.15, 1.35, 2), (1.35, 1.45, 1), (1.45, 1.8, 2), (1.8, 1.95, 3)],
    'Cone': [(0.8, 2.2, 4)],
    'Ogive': [(0.8, 2.2, 4)]
}

# Read the SVG images
#images = {
#    'Ogive': mpimg.imread('NoseconeImages/ogive.svg'),
#    'Cone': mpimg.imread('NoseconeImages/cone.svg'),
#    'LV-Haack': mpimg.imread('NoseconeImages/lv_haack.svg'),
#    'Von Karman': mpimg.imread('NoseconeImages/von_karman.svg'),
#    'Parabola': mpimg.imread('NoseconeImages/parabola.svg'),
#    '3/4 Parabola': mpimg.imread('NoseconeImages/three_quarters_parabola.svg'),
#    '1/2 Parabola': mpimg.imread('NoseconeImages/half_parabola.svg'),
#    'x^(3/4)': mpimg.imread('NoseconeImages/x_three_quarters.svg'),
#    'x^(1/2)': mpimg.imread('NoseconeImages/x_half.svg')
#}


# Define colors for efficiencies
colors = {
    1: 'green',
    2: 'yellow',
    3: 'orange',
    4: 'red'
}

plt.figure(figsize=(12, 8))

# Plot efficiency ranges for each nose cone type
for i, (cone_type, ranges) in enumerate(efficiency_ranges.items()):
    for start, end, efficiency in ranges:
        plt.hlines(i, start, end, colors=colors[efficiency], lw=15)

plt.yticks(range(len(efficiency_ranges)), list(efficiency_ranges.keys()))
plt.xlabel('Mach number')
plt.ylabel('Nose cone type')

# Create a custom legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors.values()]
labels = [f'{efficiency}' for efficiency in colors.keys()]
plt.legend(handles, labels)

# Add the images to the graph
#for i, (cone_type, image) in enumerate(images.items()):
#    ax = plt.gca()
#    imagebox = OffsetImage(image, zoom=0.2)
#    ab = AnnotationBbox(imagebox, (0.8, i))
#    ax.add_artist(ab)

plt.grid(True)
plt.title('Efficiencies of Different Nose Cone Types')
plt.tight_layout()
plt.show()