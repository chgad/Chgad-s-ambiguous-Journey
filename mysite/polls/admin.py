from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

    def has_delete_permission(self, request, obj=None):
        return True


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
            ]

    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
