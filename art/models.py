from django.db import models
from userauth.models import User
from django.core.exceptions import ValidationError
from .validators import validate_file_extension

class ArtSave(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	file = models.FileField(upload_to = "templates/static/images",validators=[validate_file_extension])
	description = models.TextField(null=True)



class CommentSection(models.Model):
	art = models.ForeignKey(ArtSave,related_name='comments',on_delete = models.CASCADE)
	created_on = models.DateTimeField(auto_now_add = True)
	SCORE_CHOICES = zip( range(1,6), range(1,6) )
	stars = models.IntegerField(choices=SCORE_CHOICES, null = True)
	Comment = models.TextField(blank = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	class Meta:
		ordering = ['-created_on']
