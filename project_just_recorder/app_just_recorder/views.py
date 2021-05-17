from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import base64
import wave
from django.http import JsonResponse
from pydub import AudioSegment
from pydub.playback import play
import io

# Create your views here.


def index(request):
    return render(request, 'app_just_recorder/index.html')


@csrf_exempt
def recording(request):
    if request.method == 'POST':
        print('reuqest.POST : ', request.POST)
        base64data = request.POST['base64data']
        decode_string = base64.b64decode(base64data.split(",")[1])
        wav_file = open("temp.wav", "wb")
        wav_file.write(decode_string)

    return render(request, 'app_just_recorder/recording.html')

