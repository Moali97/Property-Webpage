from django.db import models


class Propertydetails(models.Model):
    city = models.CharField(max_length = 30)
    description = models.TextField(blank=True)
    address = models.CharField(max_length = 200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Propertydetails"

    def __str__(self):
        return self.city


#price range boxes or
#list date = models.DateTimeField(default=datetime.now, blank=True)