from django.shortcuts import render
from .models import AudioModel
from .form import AudioForm
from moviepy.editor import *
from datetime import datetime
import os

# Create your views here.
def index(request):
    audioForm = AudioForm()
    context = { 
        'title': 'Edited.id',
        'page': 'Audio Processing',
        'audio_form': audioForm,
        'nav': [
            ['/','Home'],
            ['/imageProcess/','Image'],
            ['/audioProcess/','Audio'],
        ],
    }
    if request.method == 'POST':
        print('ini adalah method post')
        audio = AudioModel()
        if len(request.FILES) != 0:
            audio.videoFile= request.FILES['videoFile']
            audio.save()
            print(request.FILES['videoFile'])
            print(request.FILES)
            timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            newName = "".join(["static/media/", timeStamp, ".mp4"])
            oldName = "".join(["static/media/", audio.videoFile.name])
            os.rename(oldName, newName)
            mp4_file = newName
            mp3_file = "".join(["static/media/", timeStamp, ".mp3"])
            videoClip = VideoFileClip(mp4_file)
            audioClip = videoClip.audio
            audioClip.write_audiofile(mp3_file)
            audioClip.close()
            videoClip.close()
            audio.save()
    else:
        print('ini adalah method get')
    return render(request, 'audioProcess/index.html', context)
