import matplotlib.pyplot as plt
import numpy as np

phase_arr = []
f_arr = []
amplitude_arr = []

phase_arr.append(0)
f_arr.append(2.0)
amplitude_arr.append(1.0 )

phase_arr.append(np.pi/3)
f_arr.append(1.0)
amplitude_arr.append( 2.0)

phase_arr.append(np.pi/6)
f_arr.append(3.0)
amplitude_arr.append(1.5)

x_arr = []
y_arr = []

for j in range(0,3):
    phase = phase_arr[j]
    f = f_arr[j]
    amplitude = amplitude_arr[j]
    x = []
    y = []
    for i in np.arange(0,int(5/0.001)):
        time = i*0.001
        x.append(time)
        value = amplitude*np.sin((2*np.pi*f*time)-phase)
        y.append(value)
    plt.plot(x, y)
    plt.xlabel('Time(t)')
    plt.ylabel('amplitude(V)')
    plt.show()
    x_arr.append(x)
    y_arr.append(y)

wave_n = []
for i in range(0, len(y)):
    wave = y_arr[0][i] + y_arr[1][i] + y_arr[2][i]
    wave_n.append(wave + 0.1*np.random.normal())
    
plt.plot(x_arr[0], wave_n)
plt.xlabel('frequency(hz)')
plt.ylabel('amplitude(V)')
plt.show()


