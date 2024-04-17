from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from gtts import gTTS
import os
from datetime import datetime
from .models import Speech
from django.http import FileResponse
from django.conf import settings

# Create your views here.


@login_required
def converter_view(request):
    return render(request, 'converter.html')


@login_required
def generate_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        try:
            # Generate speech
            tts = gTTS(text)
            # Define path to save audio
            audio_filename = f'{datetime.now().strftime("%Y%m%d%H%M%S")}.mp3'
            audio_path = os.path.join('media', audio_filename)

            tts.save(audio_path)

            # Save speech to database
            speech = Speech.objects.create(text=text, audio_file=audio_path)

            return JsonResponse({'status': 'success', 'audio_path': audio_path})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'})


@login_required
def serve_audio_file(request, path):
    return FileResponse(open(path, 'rb'), content_type='audio/mpeg')


@login_required
def display_speeches(request):
    speeches = Speech.objects.all()
    return render(request, 'speeches.html', {'speeches': speeches})