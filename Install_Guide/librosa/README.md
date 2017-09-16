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

should need at least one Backend
I was using window7. so needed to install ffmpeg.
## Go https://www.ffmpeg.org/download.html
## click get packages(window), download zip file.
## add  System_variable, go PATH, add @@your path where it is@@/ffmpeg/bin
 check if it's installed, go to cmd, 
 > ffmpeg -version
 
 tutorial 1 example.
 ![ tutorial 1](https://raw.githubusercontent.com/sungmin-yang/Min_course/edit/master/Install_Guide/librosa//tutorial1.JPG)
