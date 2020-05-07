from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField()
    image = models.ImageField(upload_to ='blog/static/uploads/') 

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    # approved_comment = models.BooleanField(default=False)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def __str__(self):
        return self.text