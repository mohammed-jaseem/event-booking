from django.db import models

class Slider(models.Model):
    image = models.ImageField(upload_to="booking_slider")
    title = models.CharField(max_length=225)

    class Meta:
        db_table = "slider"
        verbose_name = "slider"
        verbose_name_plural = "slideries"
        ordering = ["-id"]

    def __str__(self):
        return self.title
    
class Event(models.Model):
    image = models.ImageField(upload_to="booking_event")
    name = models.CharField(max_length=225)

    

    class Meta:
        db_table = "event"
        verbose_name = "event"
        verbose_name_plural = "events"
        ordering = ["-id"]

    def __str__(self):
        return self.name
    
class Tip(models.Model):
    image = models.ImageField(upload_to="booking_event")
    title = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    short_description = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


    class Meta:
        db_table = "tip"
        verbose_name = "tip"
        verbose_name_plural = "tips"
        ordering = ["-id"]

    def __str__(self):
        return self.title
