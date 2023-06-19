import os
from pydub import AudioSegment
import random
from mutagen.mp3 import MP3


def parse_and_split_dir(directory, out_dir):
  files = [x for x in os.listdir(directory) if ".mp3" in x]
  print(files)
  cntr = 0
  for wav in files:
    wav = wav.replace(" ", "\ ")
    temp_dir = os.path.join(out_dir, str(cntr))
    # Path(temp_dir).mkdir(parents=True, exist_ok=True)
    temp_dir = os.path.join(temp_dir, "output%05d.mp3")
    command = "ffmpeg -i {} -f segment -segment_time 60 -c copy {}".format(os.path.join(directory, wav), temp_dir)
    # command = shlex.split(command)
    # subprocess.run(command)
    cntr += 1
cwd = os.getcwd()
# print(parse_and_split_dir(cwd+"\file.mp3", cwd))
# print(parse_and_split_dir(cwd, cwd))


file=input('file name :')
cwd=os.getcwd()
os.system("set path=C:\ffmpeg\bin")
filename=cwd+"/music/"+file
# os.system('ffmpeg -i "'+str(filename)+'" -f segment -segment_time 3600 -c copy '+cwd+"/results/"+'file%010d.mp3')
# os.system('ffmpeg -i "'+str(filename)+'" -f segment -segment_time 3600 -c copy output_audio_file_%010d.mp3')
# os.system('ffmpeg -i "'+str(filename)+'" -f segment -segment_times 120,300 -c copy output_audio_file_%9d.mp3')
#list of 3 min
def convert(src,dest):
    sound = AudioSegment.from_mp3(src)
    sound.export(dest, format="wav")
    return "Done!"

audio = MP3(filename)
audio_length=audio.info.length
print("Total audio length in: ",int(audio.info.length),"Seconds")
print("Total audio length in: ",int(audio.info.length/60),"Minutes")
print("Total audio length in: ",int(audio.info.length/3600),"Hours")
divider=input("Divide it in Seconds [3600s => 1h, 180s =>2 min] :")
tracks=audio_length/int(divider)
print("Maximum tracks on this audio :",int(tracks),"Track in Minutes")
start=0
end=150
cwd=os.getcwd()
newpath=str(cwd)+"/small_results/WAV-Results-"+str(random.randint(300,9889998))
if not os.path.exists(newpath):
    os.makedirs(newpath)
else:
    print("Path exists.")
dst=cwd+"/small_results/"
for i in range(int(tracks)):  
    os.system('ffmpeg -i "'+str(filename)+'"  -ss  "'+str(start)+'"  -to "'+str(end)+'" -c copy '+dst+'file"'+str(i)+'".mp3')
    src=str(cwd)+"/small_results/file"+str(i)+".mp3"
    dest=str(newpath)+"/"+str(i)+".wav"
    print(convert(src,dest))
    rando=random.randint(150,int(divider))
    start=end
    print('start ',start)
    
    # end=end+random.randint(150,int(divider))
    end=end+rando
    print('End ',end)


    
