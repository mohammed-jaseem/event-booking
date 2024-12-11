from django.db import models
from users.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "customer_customer"
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ["-id"]

    def __str__(self):
        return self.user.email

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
    
class Category(models.Model):
    name = models.CharField(max_length=225)
    phone = models.IntegerField()
    place = models.CharField(max_length=225)
    evant_name = models.CharField(max_length=225)
    date_time = models.DateTimeField()
    tickets = models.ForeignKey(Event, on_delete=models.CASCADE)


    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["-id"]

    def __str__(self):
        return self.name
    
class Project(models.Model):
    image = models.ImageField(upload_to="booking_project")
    name = models.CharField(max_length=225)
    date_time = models.DateTimeField()
    place = models.CharField(max_length=225)

    class Meta:
        db_table = "project"
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ["-id"]

    def __str__(self):
        return self.name
    
class Form(models.Model):
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=255)
    place = models.CharField(max_length=225)
    Participant = models.IntegerField()
    phone = models.IntegerField()
    image = models.ImageField()


    class Meta:
        db_table = "form"
        verbose_name = "form"
        verbose_name_plural = "forms"
        ordering = ["-id"]

    def __str__(self):
        return self.name.name


