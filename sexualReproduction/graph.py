import matplotlib.pyplot as plt
import numpy as np

def plot_graph(rabbit_count, fox_count):
    
    frames = np.arange(len(rabbit_count))



    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['axes.facecolor'] = 'black'
    fig = plt.figure()
    fig.patch.set_facecolor('black')

    # Step 4: Plot the data
    plt.plot(frames, rabbit_count, label='Rabbit')
    plt.plot(frames, fox_count, label='Fox')

    # Customize the plot
    plt.xlabel('Frame no', color='white')   # Set x-axis label color to white
    plt.ylabel('Animal count', color='white')   # Set y-axis label color to white
    plt.title('Number of animals in every frame', color='white')   # Set title color to white
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
