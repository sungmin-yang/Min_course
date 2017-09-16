import librosa
y, sr = librosa.load('Kalimba.mp3')

mfcc_test1 = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=5)
mfcc_test2 = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

#print(dir(librosa))
import matplotlib.pyplot as plt
import librosa.display
plt.figure(figsize=(10,4))
librosa.display.specshow(mfcc_test1, x_axis='time')
plt.title('MFCC value')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
librosa.display.specshow(mfcc_test2, x_axis='time')
plt.title('MFCC value')
plt.tight_layout()
plt.show()
