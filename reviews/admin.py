from django.contrib import admin

class ReviewAdimin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment')
