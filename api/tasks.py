from celery import shared_task
from api.trasactionfunc import trasactionfunc

@shared_task(time_limit=20000)
def trasactiontaskfunc(totrasaction):
    return trasactionfunc(totrasaction)