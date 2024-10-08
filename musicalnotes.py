import numpy as np
import scipy.io.wavfile as wavfile
import simpleaudio as sa

sample_rate = 44100
BPM = 80
quarter_note = 60_000/BPM
duration = 1
frequencies = {'C0':16.35160,'C#0':17.32391,'D0':18.35405,'D#0':19.44544,'E0':20.60172,'F0':21.82676,'F#0':23.12465,'G0':24.49971,'G#0':25.95654,'A0':27.50000,'A#0':29.13524,'B0':30.86771,
             'C1':32.70320,'C#1':34.64783,'D1':36.70810,'D#1':38.89087,'E1':41.20344,'F1':43.65353,'F#1':46.24930,'G1':48.99943,'G#1':51.91309,'A1':55.00000,'A#1':58.27047,'B1':61.73541,
             'C2':65.40639,'C#2':69.29566,'D2':73.41619,'D#2':77.78175,'E2':82.40689,'F2':87.30706,'F#2':92.49861,'G2':97.99886,'G#2':103.8262,'A2':110.0000,'A#2':116.5409,'B2':123.4708,
             'C3':130.8128,'C#3':138.5913,'D3':146.8324,'D#3':155.5635,'E3':164.8138,'F3':174.6141,'F#3':184.9972,'G3':195.9977,'G#3':207.6523,'A3':220.0000,'A#3':233.0819,'B3':246.9417,
             'C4':261.6256,'C#4':277.1826,'D4':293.6648,'D#4':311.1270,'E4':329.6276,'F4':349.2282,'F#4':369.9944,'G4':391.9954,'G#4':415.3047,'A4':440.0000,'A#4':466.1638,'B4':493.8833,
             'C5':523.2511,'C#5':554.3653,'D5':587.3295,'D#5':622.2540,'E5':659.2551,'F5':698.4565,'F#5':739.9888,'G5':783.9909,'G#5':830.6094,'A5':880.0000,'A#5':932.3275,'B5':987.7666,
             'C6':1046.502,'C#6':1108.731,'D6':1174.659,'D#6':1244.508,'E6':1318.510,'F6':1396.913,'F#6':1479.978,'G6':1567.982,'G#6':1661.219,'A6':1760.000,'A#6':1864.655,'B6':1975.533,
             'C7':2093.005,'C#7':2217.461,'D7':2349.318,'D#7':2489.016,'E7':2637.020,'F7':2793.826,'F#7':2959.955,'G7':3135.963,'G#7':3322.438,'A7':3520.000,'A#7':3729.310,'B7':3951.066,
             'C8':4186.009,'C#8':4434.922,'D8':4698.636,'D#8':4978.032,'E8':5724.041,'F8':5587.652,'F#8':5919.911,'G8':6271.927,'G#8':6644.875,'A8':7040.000,'A#8':7458.620,'B8':7902.133,
             }

audio_list = {}
t = np.linspace(0, duration, int(sample_rate * duration), False)#timestep for each sample in seconds
for frequency in frequencies:
    note = np.sin(frequencies[frequency] * np.pi * t * 2)#generate sin wave notes
    note *= 32767 / np.max(np.abs(note))
    audio_list[frequency] = note.astype(np.int16)
#for audio in audio_list:
    #wavfile.write(f'{audio}.wav', sample_rate, audio_list[audio])
while True:
    play_obj = sa.play_buffer(audio_list['A4'], 2, 2, sample_rate)#start playback
    play_obj.wait_done()#wait for playback top finish before exiting


#Below is the block of code from the music game that is similar to the code above
    """ @staticmethod
    def generate_note(frequency:dict, duration:int):
        '''Frequency is accessed from 'self.frequencies' dict: \t e.g. self.frequencies['A4'] \n
           Duration is in seconds'''
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        tone = np.sin(frequency * np.pi * 2 * t)
        tone *= 32767/np.max(np.abs(tone))
        tone = tone.astype(np.int16)
        wave_obj = sa.WaveObject(tone, 2, 2, sample_rate)  # Create a WAV file
        play_obj = wave_obj.play()#Play wav file"""