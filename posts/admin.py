from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from posts.models import Post, Comment


class PostAdmin(UserAdmin):

    fieldsets = (
        (
            None, {
                "fields": (
                    'account',
                    'content',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide", ),
                "fields": ("account", 'content')
            },
        ),
    )
    list_display = ('account', 'content', 'pub_date')
    list_filter = ()
    search_fields=('account',)
    ordering = ('pub_date',)
    filter_horizontal = ()

admin.site.register(Post, PostAdmin)


class CommentAdmin(UserAdmin):

    fieldsets = (
        (
            None, {
                "fields": (
                    'account',
                    'comment',
                    'post',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide", ),
                "fields": ("account", 'comment', 'post')
            },
        ),
    )
    list_display = ('account', 'comment','post' ,'pub_date')
    list_filter = ()
    search_fields=('account',)
    ordering = ('pub_date',)
    filter_horizontal = ()
admin.site.register(Comment, CommentAdmin)