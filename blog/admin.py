from django.contrib import admin

# Register your models here.

from .models import Post #Acá incluimos el modelo Post definido en el capítulo anterior

admin.site.register(Post) #Acá hacemos visible en la página del adminestrador registrando el modelo así

