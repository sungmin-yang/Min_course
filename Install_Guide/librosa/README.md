it should work
# >> pip install librosa

if it doesn't work,
# >> easy_install librosa
 if there is error with 'numba',  
# >> pip install numba
# >> easy_install numba
# >> easy_install librosa # final

then it should work.

example,
import librosa
y, sr = librosa.load('Kalimba.mp3')


# All backends failed!
--> 116     raise NoBackendError()
