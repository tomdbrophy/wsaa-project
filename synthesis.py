import numpy as np
from scipy.io.wavfile import write
from scipy import signal
import matplotlib.pyplot as plt
from pydub import AudioSegment

sr = 44100
freq = 440
length = 1

t = np.linspace(0, length, length*sr, dtype=float)
y = np.sin(np.pi * 2.0 * freq * t)

#write('sine.wav', sr, y)

sound = AudioSegment.from_wav('sine.wav')

sound.export('sine.mp3', format='mp3')