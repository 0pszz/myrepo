from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)  # عنوان الصورة
    description = models.TextField(blank=True)  # وصف الصورة (اختياري)
    keywords = models.CharField(max_length=500)  # الكلمات المفتاحية
    image = models.ImageField(upload_to='images/')  # مسار تخزين الصورة
    
    def __str__(self):
        return self.title