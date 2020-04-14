from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News,Category,Tag,Commets


class NewsAdmin(SummernoteModelAdmin):
    list_display = ("titel","user","data")
    list_editable = ("user",)
    list_filter = ("user","data",)
    search_fields = ("titel","user__username",)
    summernote_fields =('text_prev','text')




admin.site.register(News,NewsAdmin)

admin.site.register(Category)
admin.site.register(Tag)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','new','data','moder')
admin.site.register(Commets,CommentAdmin)
