from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class CategoryGenreAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name'
    )
    search_fields = ('slug',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'role'
    )
    list_editable = ('role',)
    list_filter = ('role',)
    search_fields = ('username',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'category'
    )
    search_fields = ('name',)
    list_filter = ('category',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'text',
        'score',
        'pub_date'
    )
    search_fields = ('title',)
    list_filter = ('author', 'title')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'review',
        'text',
        'pub_date'
    )
    search_fields = ('review',)
    list_filter = ('author', 'review')
    empty_value_display = '-пусто-'


admin.site.register(Category, CategoryGenreAdmin)
admin.site.register(Genre, CategoryGenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
