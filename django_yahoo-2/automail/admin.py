from django.contrib import admin
from automail.models import emailAddr
from automail.run import MailVerify
# Register your models here.

def AutoVerify(self,request,queryset):
    print(queryset)
    for i in queryset:
        emailaddr = i.emailaddr
        emailpsd = i.emailpsd
        print(emailaddr,emailpsd)
        MailVerify(emailaddr,emailpsd)

# class reFresh():
#     pass

class EmailAddrAdmin(admin.ModelAdmin):
    list_display = ['emailaddr']
    # actions = [AutoVerify,reFresh]
    actions = [AutoVerify]
    search_fields = ['emailaddr']
    # ordering =

admin.site.register(emailAddr, EmailAddrAdmin)
