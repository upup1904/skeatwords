from django.db import models


# Create your models here.


class SkeatEntry(models.Model):
    """An instance of this model represents all words with same  spelling

    So there is only one instance for "bass" or "clap".  Since Joyce will
    deliberately conflate words.

    There are words that are 
    """
    word = models.CharField(max_length=50)
    image_link = models.URLField(name='word_image_url', null=True)
    page_number = models.SmallIntegerField(null=True)
    not_in_main_skeat = models.BooleanField(null=True)
    


class SkeatPage(models.Model):
    """Page in A-Z part of Skeat 3rd Ed.

    It is a int 3 <= page <= 726
    Does not  represent addendum or special list words (homynms etc)"""
    first_keyword = models.ForeignKey(SkeatEntry, on_delete=models.CASCADE, related_name="first_keyword")
    second_keyword = models.ForeignKey(SkeatEntry, on_delete=models.CASCADE, related_name="second_keyword")
    page_number = models.SmallIntegerField(name="page_number", verbose_name="Page Number")
    default_res_image_link = models.URLField(name="image_link")






    
