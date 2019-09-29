from django.db import models

# Create your models here.

class All(models.Model):
    class Meta:
        abstract = True
        
    title = models.CharField(verbose_name='Заголовок', max_length=255, default='none')
    
    def __str__(self):
        return self.title
    

class Content(All):
    class Meta:
        abstract = True
    
    counter = models.IntegerField(verbose_name='Счётчик', default=0)
    
class Video(Content):
    fileurl = models.CharField(verbose_name='Url файла', max_length=255)
    subtitresurl = models.CharField(verbose_name='Url субтитров', max_length=255)
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
    
class Audio(Content):
    bitrate = models.IntegerField(verbose_name='Битрейт', default=0)
    
    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'
    
class Text(Content):
    text = models.TextField(blank=True, verbose_name='Содержимое',)
    
    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текст'

class Page(All):
    text = models.ManyToManyField(Text, through='PageText', verbose_name='Текст', blank=True, related_name="page")
    video = models.ManyToManyField(Video, through='PageVideo', verbose_name='Видео', blank=True, related_name="page")
    audio = models.ManyToManyField(Audio, through='PageAudio', verbose_name='Аудио', blank=True, related_name="page")
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страница'

class PageText(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.IntegerField()

class PageVideo(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.IntegerField()

class PageAudio(models.Model):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.IntegerField()

