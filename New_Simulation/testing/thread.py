import matplotlib.pyplot as plt
import numpy as np

# Step 3: Prepare your data
# Example arrays
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = np.arange(len(x))



plt.rcParams['toolbar'] = 'None'
plt.rcParams['axes.facecolor'] = 'black'
fig = plt.figure()
fig.patch.set_facecolor('black')

# Step 4: Plot the data
plt.plot(x, y1, label='y1 = x^2', marker='o')
plt.plot(x, y2, label='y2 = x', marker='x')

# Customize the plot
plt.xlabel('X-axis', color='white')   # Set x-axis label color to white
plt.ylabel('Y-axis', color='white')   # Set y-axis label color to white
plt.title('Plot of Two Arrays', color='white')   # Set title color to white
plt.legend()

# Change the color of tick labels and spines to white
plt.tick_params(colors='white', which='both')    # Set tick color to white
plt.gca().spines['top'].set_color('white')       # Top border
plt.gca().spines['bottom'].set_color('white')    # Bottom border
plt.gca().spines['left'].set_color('white')      # Left border
plt.gca().spines['right'].set_color('white') 

legend = plt.legend()
for text in legend.get_texts():
    text.set_color('white') 


# Step 6: Display the plot
plt.show()
