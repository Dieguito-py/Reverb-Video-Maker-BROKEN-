from moviepy.editor import *
from opplast import Upload
import time
import search
import input
# import datetime
import letras
import tags
import input
# from Google import Create_Service
# from googleapiclient.http import MediaFileUpload

clip = ImageClip('C:\\Users\\User\\Documents\\code\\vmsv\\imagemvideo\\'+input.msc+'new.png')
audio_clip = AudioFileClip('C:\\Users\\User\\Documents\\code\\vmsv\\remix\\'+search.ba[1]+"remix.wav")
clip = clip.set_duration(audio_clip.duration)
clip = clip.set_audio(audio_clip)
clip.write_videofile('C:\\Users\\User\\Documents\\code\\vmsv\\videos\\'+input.msc+'.mp4',fps=10)

upload = Upload(
    r"C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\wzddb15b.Selenium",
)

was_uploaded, video_id = upload.upload(
    'C:\\Users\\User\\Documents\\code\\vmsv\\videos\\'+input.msc+'.mp4',
    title=letras.yttitle,
    description="Original song: " +search.link+ '\n\nLyrics: \n'+letras.lirica,
    thumbnail='C:\\Users\\User\\Documents\\code\\vmsv\\imagemvideo\\'+input.msc+'new.png',
    tags=[input.art, input.msc, input.musica, tags.format],
    only_upload=False
)

if was_uploaded:
    print(f"{video_id} foi upado com sucesso")

time.sleep(28)

upload.close()


#UPLOAD FROM GOOGLE API


# CLIENT_SECRET_FILE = 'client_secret.json'
# API_NAME = 'youtube'
# API_VERSION = 'v3'
# SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# upload_date_time = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'

# request_body = {
#     'snippet': {
#         'categoryI': 10,
#         'title': letras.yttitle,
#         'description': "Original song: " +search.link+ '\n\n Lyrics: \n'+letras.lirica+'\n\nObrigado Por Estar Aqui♡',
#         'tags': [input.art, input.msc, input.musica, tags.format]
#     },
#     'status': {
#         'privacyStatus': 'private',
#         'publishAt': upload_date_time,
#         'selfDeclaredMadeForKids': False, 
#     },
#     'notifySubscribers': True
# }

# mediaFile = MediaFileUpload('C:\\Users\\User\\Documents\\code\\vmsv\\videos\\'+input.msc+'.mp4')

# response_upload = service.videos().insert(
#     part='snippet,status',
#     body=request_body,
#     media_body=mediaFile
# ).execute()


# service.thumbnails().set(
#     videoId=response_upload.get('id'),
#     media_body=MediaFileUpload('C:\\Users\\User\\Documents\\code\\vmsv\\imagemvideo\\'+input.msc+'new.png')
# ).execute()
