# Reference de la librairie utilisee : https://pypi.org/project/youtube-transcript-api/
# Installee depuis le terminal de visual code via : pip install youtube_transcript_api
# Dump un fichier json issu du transcript de la video dont l'ID est videoid

from youtube_transcript_api import YouTubeTranscriptApi
import json

# dump YouTube Transcript dans un fichier
def dump_dans_fichier(nomfichier = '', transcript = {}):
    nomjson = nomfichier+".json"
    with open(nomjson, 'w') as mefile:
        json.dump(transcript, mefile, indent=4)
        print('file dumped')


videoid = 'EdztlqcN_VQ'

yt_transcript = YouTubeTranscriptApi.get_transcript(videoid, languages=['fr'])

dump_dans_fichier(nomfichier=videoid, transcript=yt_transcript)