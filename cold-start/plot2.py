import matplotlib.pyplot as plt

def create_bar_chart(cold_starts):
    # Bar chart data
    labels = ['WASM in Docker (JIT)', 'WASM in Docker (AOT)']
    
    # Bar chart customization
    fig, ax = plt.subplots()
    bars = ax.bar(labels, cold_starts, color='#007acc', edgecolor='black', width=0.6)

    # Add values on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center', va='bottom')

    # Adding labels and title
    ax.set_xlabel('Cold Starts')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('Cold Start Performance')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Replace the values with your actual cold-start times
    cold_starts = [0.330, 0.3]

    # Create and display the bar chart
    create_bar_chart(cold_starts)

