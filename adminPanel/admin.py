from django.contrib import admin
from .models import *


# site logo
admin.site.register(SiteLogo)

# site contact logo
admin.site.register(SiteContactInfo)
admin.site.register(SiteContactInfoBangla)

admin.site.register(AboutUs)

admin.site.register(Message)

admin.site.register(SocailMediaLinks)

admin.site.register(BookAppointment)
admin.site.register(BookingAppointmentRequest)
admin.site.register(FloorList)
admin.site.register(FloorDetails)