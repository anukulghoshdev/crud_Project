from django.db import models

class Musician(models.Model):
    # id = models.AutoField(primary_key=True) #hidden key
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    # class Meta:
    #     db_table = 'musician'

    def __str__(self):
        return self.first_name +" "+self.last_name



class Album(models.Model):

    # id = models.AutoField(primary_key=True) #hidden key
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_datefield = models.DateField(null=True)

    # class Meta:       ## change databases table name
    #     db_table = 'album'


    rating = (
        ('', '--SELECT OPTIONS--'),
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Not Bad'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name + ", Rating: " + str(self.num_stars)
