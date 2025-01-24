import matplotlib.pyplot as plt

def plot(time_steps, memory, cpu):

    plt.figure()
    plt.plot(time_steps, memory, color='red')
    plt.title("RAM Usage over Time")
    plt.xlabel("Time in Seconds")
    plt.ylabel("RAM Usage in %")
    plt.savefig('mem.png')

    plt.figure()
    plt.plot(time_steps, cpu, color='blue')
    plt.title("CPU Usage over Time")
    plt.xlabel("Time in Seconds")
    plt.ylabel("CPU Usage in %")
    plt.savefig('cpu.png')
