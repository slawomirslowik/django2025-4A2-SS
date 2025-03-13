from django.contrib import admin
from .models import Question, Choice, Author

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Author)
