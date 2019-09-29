from django.db import transaction
from .models import *
from django.db.models import F

def trasactionfunc(totrasaction):
    try:
        with transaction.atomic():
            Audio.objects.filter(id__in=totrasaction['audio']).update(counter=F('counter') + 1)
            Video.objects.filter(id__in=totrasaction['video']).update(counter=F('counter') + 1)
            Text.objects.filter(id__in=totrasaction['text']).update(counter=F('counter') + 1)
    except:
        transaction.rollback()
    else:
        return True
    return False