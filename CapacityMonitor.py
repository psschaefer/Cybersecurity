import psutil
import time
import numpy as np
import Plotter as Plotter

# monitor memory and cpu
def monitor_capacity():
    current_time_step = 0
    time_steps = np.array([])
    memory = np.array([])
    cpu = np.array([])


    while True:

        cpu_usage = psutil.cpu_percent(interval=0.1)
        memory_usage = psutil.virtual_memory().percent
        current_time_step += 0.1

        cpu = np.append(cpu, int(cpu_usage))
        memory = np.append(memory, int(memory_usage))
        time_steps = np.append(time_steps, current_time_step)
        print("Cpu_usage_",cpu_usage)
        print("Memory_usage",memory_usage)
        print("current_timesteps",current_time_step)
        time.sleep(0.1)

        if current_time_step > 15:
            break

    Plotter.plot(time_steps, memory, cpu)




monitor_capacity()

