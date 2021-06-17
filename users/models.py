from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image =models.ImageField(default='defult.jpg',upload_to='profile_ooics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''When you are overriding model's save method in Django, you should also pass *args and **kwargs to overridden method. this code may work fine:
You've overridden the save method, but you haven't preserved its signature. Yo need to accept the same arguments as the original method, and pass them in when calling super'''


