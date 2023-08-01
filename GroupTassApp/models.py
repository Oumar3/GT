from django.db import models

# Create your models here.

class Annonce(models.Model):
    title=models.CharField(max_length=255)
    intro=models.TextField()
    slug=models.CharField(max_length=100)
    body=models.TextField()
    date_pub=models.DateTimeField(auto_now=True)
    img=models.ImageField(upload_to='media', blank=True,null=True)

    class Meta:
        ordering=['date_pub']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    objet=models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.name + ' ' + self.email + self.objet + ' ' + self.message

class Team(models.Model):
    image=models.ImageField(upload_to='media', blank=True,null=True)
    nom=models.CharField(max_length=150)
    post=models.CharField(max_length=100)
    twitter=models.URLField(blank=True,null=True,default="#")
    facebook=models.URLField(blank=True,null=True,default="#")
    instagram=models.URLField(blank=True,null=True,default="#")
    linkedin=models.URLField(blank=True,null=True,default="#")

    def __str__(self):
        return self.nom + ' ' + self.post

class MotDuMembre(models.Model):
    nom=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', blank=True,null=True)
    post=models.CharField(max_length=100)
    mot=models.CharField(max_length=100)

    def __str__(self):
        return self.nom + ' ' + self.post