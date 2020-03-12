from django.contrib import admin

from .models import Question

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    #field = ['pub_date', 'question_text']

    # for many fields
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
