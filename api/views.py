from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .tasks import trasactiontaskfunc
#from .trasactionfunc import trasactionfunc

# Create your views here.
protokol = 'http://'
totrasaction = {'audio': [], 'video': [], 'text': []}

def page_set(func, param):
    l = []
    for e in func():
        itemid = eval('e.'+param+'.pk')
        el  = {'id': itemid,
               'title':  eval('e.'+param+'.title'),
               'counter': eval('e.'+param+'.counter')}
        if param == 'audio':
            el.update({'bitrate': e.audio.bitrate})
        if param == 'video':
            el.update({'fileurl': e.video.fileurl, 'subtitresurl': e.video.subtitresurl})
        if param == 'text':
            el.update({'text': e.text.text})
        l.append(el)
        totrasaction[param].append(itemid)
    return l

class PageView(APIView):
    def get(self, request, item):
        page = Page.objects.filter(pk=item).first()
        
        content = {"id": item,
                   "title": page.title,
                   "audio": page_set(page.pageaudio_set.all, 'audio'),
                   "video": page_set(page.pagevideo_set.all, 'video'),
                   "text": page_set(page.pagetext_set.all, 'text'),}
        
        trasactiontaskfunc.delay(totrasaction)
        #trasactionfunc(totrasaction)
        
        return Response(content)
    
class PagesView(APIView):
    def get(self, request, offset, limit):
        host = protocol+request.get_host()
        pages = Page.objects.all()[offset:limit]
        urls = []
        for e in pages:
            urls.append(host+'/api/page/'+str(e.id))
        return Response(urls)