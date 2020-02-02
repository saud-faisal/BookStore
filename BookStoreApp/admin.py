from django.contrib import admin
from BookStoreApp.models import regData,Books

class regDataAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','college_roll','batch','branch','email','password','cpassword']
admin.site.register(regData)

class BooksAdmin(admin.ModelAdmin):
    list_display=['bookname','authorname','Publication','Isbn','imag','date','time']
admin.site.register(Books)
