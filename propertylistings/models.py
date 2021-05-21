from django.db import models


class Propertydetails(models.Model):
    city = models.CharField(max_length = 30)
    description = models.TextField(blank=True)
    address = models.CharField(max_length = 200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(default=1)
    property_type = models.CharField(max_length = 25, default='')
    picture = models.ImageField(null=True, blank=True, upload_to="images2/")

    class Meta:
        verbose_name_plural = "Propertydetails"

    def __str__(self):
        return self.city


#price range boxes or
#list date = models.DateTimeField(default=datetime.now, blank=True)


