import numpy as np
import sounddevice as sd
import tkinter as tk

start_freq = 50         # Hz, start frequency
end_freq = 100          # Hz, ending frequency
duration = 60           # Sweep duration
sample_rate = 44100     # Hz, sample rate

def generate_sweep(start_freq, end_freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    frequency = np.linspace(start_freq, end_freq, len(t))
    signal = 0.5 * np.sin(2 * np.pi * frequency * t)

    return signal

def play_audio(signal, sample_rate):
    sd.play(signal, sample_rate)
    sd.wait()
    
def main():

    def start_sweep():
        global start_freq, end_freq, duration, sample_rate
        
        start_freq = int(txf_startFreq.get("1.0", "end-1c"))
        end_freq = int(txf_endFreq.get("1.0", "end-1c"))
        duration = int(txf_duration.get("1.0", "end-1c"))
        
        sweep_signal = generate_sweep(start_freq, end_freq, duration, sample_rate)

        play_audio(sweep_signal, sample_rate)
    
    root = tk.Tk()
    root.title("Frequency Sweep")
    #root.geometry("200x200")

    lbl_startFreq = tk.Label(root, text="Start Freq. (Hz)", width=20)
    lbl_startFreq.grid(row=0, column=0)

    lbl_endFreq = tk.Label(root, text="End Freq. (Hz)", width=20)
    lbl_endFreq.grid(row=1, column=0)

    lbl_duration = tk.Label(root, text="Duration (s)", width=20)
    lbl_duration.grid(row=2, column=0)

    txf_startFreq = tk.Text(root, height=1, width=20)
    txf_startFreq.grid(row=0, column=1)

    txf_endFreq = tk.Text(root, height=1, width=20)
    txf_endFreq.grid(row=1, column=1)

    txf_duration = tk.Text(root, height=1, width=20)
    txf_duration.grid(row=2, column=1)

    btn_run = tk.Button(root, text="Run Freq. Sweep", command=start_sweep, width=40, fg="white", bg="red")
    btn_run.grid(row=3, column=0, columnspan=2)

    root.mainloop()

main()
