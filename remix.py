import subprocess
import sys
import search
import pathlib
import tempfile
import shutil
from distutils.dir_util import copy_tree
import sox


def validateInput():
    try:
        fileInput = 'C:\\Users\\User\\Documents\\code\\vmsv\\dow&cov\\'+search.ba[1]+"new.wav"
        return fileInput
    except IndexError:
        print("No input file provided!")
        exit()


def applyAudioEffects(input, tmpDirectory):

    pathInput = 'C:\\Users\\User\\Documents\\code\\vmsv\\remix\\'
    inputName = search.ba[1]+'remix.wav'
    # extention = pathInput.suffix
    tmpName = " Slowed.wav"
    # tag = " [ s l o w e d   a n d   R e v e r b ]"
    inputSampleRate = sox.file_info.sample_rate(input)
    inputSampleRateCommand = str(round(inputSampleRate))
    print(inputSampleRateCommand)
    speed = 0.89
    resampleRate = round(inputSampleRate * speed)
    sampleRateCommand = "asetrate=" + str(resampleRate)
    intermediateAudio = pathlib.Path(tmpDirectory,
                                     inputName + tmpName )
    finalAudio = pathlib.Path(tmpDirectory, inputName)
    subprocess.run([
        "ffmpeg", "-i", input, "-filter:a", sampleRateCommand, "-ar",
        inputSampleRateCommand, intermediateAudio
    ])
    subprocess.run([
        "ffmpeg", "-i", intermediateAudio, "-i", "media/impulse.wav",
        "-filter_complex",
        "[0] [1] afir=dry=10:wet=10 [reverb]; [0] [reverb] amix=inputs=2:weights=10 7",
        finalAudio
    ]) 
    intermediateAudio.unlink()
    return finalAudio

def copyExports(tmpDir, input):
    destinationDir = str((pathlib.Path(input)).parents[0])
    copy_tree(tmpDir, destinationDir)
    return

validateInput
applyAudioEffects
copyExports
copy_tree

print("Starting up.")
tmpDirectory = tempfile.mkdtemp()
inputFile = validateInput()
outputAudio = applyAudioEffects(inputFile, tmpDirectory)
(outputAudio, tmpDirectory)
copyExports(tmpDirectory, inputFile)
print("Audio and video files created! Cleaning up.")
shutil.rmtree(tmpDirectory)
print("Cleanup complete.")
source = 'C:\\Users\\User\\Documents\\code\\vmsv\\dow&cov\\'+search.ba[1]+'remix.wav'
destination = 'C:\\Users\\User\\Documents\\code\\vmsv\\remix\\'+search.ba[1]+'remix.wav'
shutil.move(source,destination)



# import numpy as np
# import wave
# import struct
# import matplotlib.pyplot as plt
# from scipy.signal import convolve
# import os
# # import dowload
# import search


    
# sample_in = 'C:\\Users\\User\\Documents\\code\\vmsv\\dow&cov\\'+search.ba[1]+"new.wav"
# reverb_in = r"C:\Users\User\Documents\code\vmsv\remix\Ruby Room.wav"
# frame_rate = 44100.0

# wav_file = wave.open(sample_in, 'r')
# num_samples_sample = wav_file.getnframes()
# num_channels_sample = wav_file.getnchannels()
# sample = wav_file.readframes(num_samples_sample)
# total_samples_sample = num_samples_sample * num_channels_sample
# wav_file.close()

# wav_file = wave.open(reverb_in, 'r')
# num_samples_reverb = wav_file.getnframes()
# num_channels_reverb = wav_file.getnchannels()
# reverb = wav_file.readframes(num_samples_reverb)
# total_samples_reverb = num_samples_reverb * num_channels_reverb
# wav_file.close()

# sample = struct.unpack('{n}h'.format(n = total_samples_sample), sample)
# sample = np.array([sample[0::2], sample[1::2]], dtype = np.float64)
# sample[0] /= np.max(np.abs(sample[0]), axis = 0)
# sample[1] /= np.max(np.abs(sample[1]), axis = 0)

# reverb = struct.unpack('{n}h'.format(n = total_samples_reverb), reverb)
# reverb = np.array([reverb[0::2], reverb[1::2]], dtype = np.float64)
# reverb[0] /= np.max(np.abs(reverb[0]), axis = 0)
# reverb[1] /= np.max(np.abs(reverb[1]), axis = 0)

    
# gain_dry = 1
# gain_wet = 1
# output_gain = 0.05

# reverb_out = np.zeros([2, np.shape(sample)[1] + np.shape(reverb)[1] - 1], dtype = np.float64)
# reverb_out[0] = output_gain * (convolve(sample[0] * gain_dry, reverb[0] * gain_wet, method = 'fft'))
# reverb_out[1] = output_gain * (convolve(sample[1] * gain_dry, reverb[1] * gain_wet, method = 'fft'))


# reverb_integer = np.zeros((reverb_out.shape))

# reverb_integer[0] = (reverb_out[0]*int(np.iinfo(np.int16).max)).astype(np.int16)
# reverb_integer[1] = (reverb_out[1]*int(np.iinfo(np.int16).max)).astype(np.int16)

# reverb_to_render = np.empty((reverb_integer[0].size + reverb_integer[1].size), dtype = np.int16)
# reverb_to_render[0::2] = reverb_integer[0]
# reverb_to_render[1::2] = reverb_integer[1]

# nframes = total_samples_sample
# comptype = "NONE"
# compname = "not compressed"
# nchannels = 2
# sampwidth = 2

# wav_file_write = wave.open('C:\\Users\\User\\Documents\\code\\vmsv\\remix\\'+search.ba[1]+'remix.wav', 'w')
# wav_file_write.setparams((nchannels, sampwidth, int(frame_rate), nframes, comptype, compname))

# for s in range(nframes):
#     wav_file_write.writeframes(struct.pack('h', reverb_to_render[s]))
    
# wav_file_write.close()

# print ('deu boa!')
