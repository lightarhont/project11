from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .tasks import trasactiontaskfunc
import pickle
#from .trasactionfunc import trasactionfunc

# Create your views here.
class PageView(APIView):
    def get(self, request, item):
        page = Page.objects.filter(pk=item).first()
        
        totrasaction = {'audio': [], 'video': [], 'text': []}
        
        la = []
        for e in page.pageaudio_set.all():
            el = {
                  'id': e.audio.pk,
                  'title': e.audio.title,
                  'counter': e.audio.counter,
                  'bitrate': e.audio.bitrate,
                  }

            totrasaction['audio'].append(e.audio.pk)
            la.append({'order': e.order, 'quantity': e.quantity, 'el': el})
        lv = []
        for e in page.pagevideo_set.all():
            el = {
                  'id': e.video.pk,
                  'title': e.video.title,
                  'counter': e.video.counter,
                  'fileurl': e.video.fileurl,
                  'subtitresurl': e.video.subtitresurl
                  }
            totrasaction['video'].append(e.video.pk)
            lv.append({'order': e.order, 'quantity': e.quantity, 'el': el})
        lt = []
        for e in page.pagetext_set.all():
            el = {
                  'id': e.text.pk,
                  'title': e.text.title,
                  'counter': e.text.counter,
                  'text': e.text.text,
                  }
            totrasaction['text'].append(e.text.pk)
            lt.append({'order': e.order, 'quantity': e.quantity, 'el': el})
        
        content = {
            "id": item,
            "title": page.title,
            "audio": la,
            "video": lv,
            "text": lt,
                   }
        
        trasactiontaskfunc.delay(totrasaction)
        #trasactionfunc(totrasaction)
        
        return Response(content)
    
class PagesView(APIView):
    def get(self, request, offset, limit):
        pages = Page.objects.all()[offset:limit]
        urls = []
        for e in pages:
            urls.append('http://127.0.0.1:8000/api/page/'+str(e.id))
        return Response(urls)