from os import path
from pydub import AudioSegment

# location="/music"
location=input("location :")
i=1
while(1):
  # files                                                                         
  src = location +str(i)+".mp3"
  dst = location + str(i)+".wav"

  # convert wav to mp3                                                            
  sound = AudioSegment.from_mp3(src)
  # audio = AudioSegment.from_wav(os.path.join(base_path+"audios", audio_file))
  sound.export(dst, format="wav")
  i=i+1
