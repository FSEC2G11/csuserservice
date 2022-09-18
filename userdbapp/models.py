from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

#Enumerations
class UserType(models.IntegerChoices):
    ADMIN = 0
    GENERAL = 1

# class DataModelType(models.IntegerChoices):
#     PCA = 0
#     SIMCA = 1
#     PLSDA = 2
#     KNN = 3
#     SVM = 4
#
# class DataModel(models.Model):
#     name = models.CharField(max_length=20, primary_key=True)
#     type = models.IntegerField(choices=DataModelType.choices, default=1)
#     file = models.BinaryField(null=False)
#
#     def __str__(self):
#         return str(self.name)

class CDAUsers(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    usertype = models.IntegerField(choices=UserType.choices, default=1)
    email = models.EmailField()
    password = models.CharField(max_length=128, null=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = _("CDA User")
        verbose_name_plural = _("CDA Users")
