from django.db import models


# News manager
# class BarishalNews(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(division_of_news="barishal")

# Add News Model
# class News(models.Model):
#
#     news_type = (
#         ('general_news', 'General News'),
#         ('lead_news', 'Lead News')
#     )
#
#     lead_type = (
#         ('lead_main', 'Main Lead News'),
#         ('lead_minor_1', "Small Top Lead News"),
#         ('lead_minor_2', 'Small Bottom Lead News')
#     )
#
#     news_division = (
#         ('barishal', 'Barishal'),
#         ('chattogram', 'Chattogram'),
#         ('dhaka', 'Dhaka'),
#         ('khulna', 'Khulna'),
#         ('rajshahi', 'Rajshahi'),
#         ('rangpur', 'Rangpur'),
#         ('mymensingh', 'Mymensingh'),
#         ('sylhet', 'Sylhet')
#     )
#
#     news_status = (
#         ('publish', 'Publish'),
#         ('draft', 'Draft'),
#     )
#
#     class PublishedNews(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(news_status='publish')
#
#     class LeadMainObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(lead_types="lead_main")
#
#     class LeadMinor1Objects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(lead_types='lead_minor_1')
#
#     class LeadMinor2Objects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(lead_types='lead_minor_2')
#
#     class NewsGeneralObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(news_types='general_news')
#
#     news_types = models.CharField(default='', max_length=255, choices=news_type, blank=True, null=True)
#     lead_types = models.CharField(default='', max_length=255, choices=lead_type, blank=True, null=True)
#
#     news_status = models.CharField(default='', max_length=255, choices=news_status, blank=True, null=True)
#
#     news_id = models.CharField(default='', max_length=255, blank=True, null=True)
#     news_title = models.TextField(default='', blank=False, null=False, max_length=255)
#     news_img   = models.ImageField(upload_to='news_images')
#     news_img_short_description = models.CharField(default='', blank=True, null=True, max_length=255)
#     news_details = models.TextField(default='', blank=False, null=False)
#     news_category = models.ForeignKey(NewsCategory, on_delete=models.PROTECT)
#     news_subcategory = models.ForeignKey(NewsSubCategory, on_delete=models.PROTECT, blank=True, null=True)
#
#     division_of_news = models.CharField(default='', max_length=255, choices=news_division, blank=True, null=True)
#
#
#     objects = models.Manager() # built-in manager
#     leadmainobjects = LeadMainObjects() # custom manager
#     leadminor1objects = LeadMinor1Objects() # custom manager
#     leadminor2objects = LeadMinor2Objects() # custom manager
#     newsgeneralobjects = NewsGeneralObjects() # custom manager
#     publishedObjects = PublishedNews() # custom manager
#
#     # division news manager
#     barishalnewsobjects = BarishalNews()
#     chattogramnewsobjects = ChattogramNews()
#     dhakanewsobjects = DhakaNews()
#     khulnanewsobjects = KhulnaNews()
#     rajshahinewsobjects = RajshahiNews()
#     rangpurnewsobjects = RangpurNews()
#     mymensinghnewsobjects = MymensinghNews()
#     sylhetnewsobjects= SylhetNews()
#
#     def __str__(self):
#         return self.news_title + '|' + str(self.pk)
#
#




# site logo
class SiteLogo(models.Model):
    logo = models.ImageField(upload_to="logos")
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.logo)

# contact information
class SiteContactInfo(models.Model):
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.email + str(self.pk)

# contact info in Bangla
class SiteContactInfoBangla(models.Model):
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.email + '|' + str(self.pk)


# about us
class AboutUs(models.Model):
    about_us = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + "|" + str(self.added_at)


# messages
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    sub = models.CharField(max_length=255, blank=True, null=True)
    msg = models.TextField()

    def __str__(self):
        return self.name + "|" + self.email


# social media links
class SocailMediaLinks(models.Model):
    fb = models.CharField(max_length=255, blank=True, null=True)
    tw = models.CharField(max_length=255, blank=True, null=True)
    insgrm = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


# img for book an appointment
class BookAppointment(models.Model):
    img = models.ImageField(upload_to='appointment')

    def __str__(self):
        return str(self.pk)



# appointment list
class BookingAppointmentRequest(models.Model):
    name = models.CharField(default='', max_length=255, blank=True, null=True)
    email = models.CharField(default='', max_length=255, blank=True, null=True)
    phone = models.CharField(default='', max_length=255, blank=True, null=True)
    date_choice_1 = models.CharField(default='', max_length=255, blank=True, null=True)
    date_choice_2 = models.CharField(default='', max_length=255, blank=True, null=True)
    date_choice_3 = models.CharField(default='', max_length=255, blank=True, null=True)
    subject = models.CharField(default='', max_length=255, blank=True, null=True)
    msg = models.CharField(default='', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name + "||" + self.email


# floor
class FloorList(models.Model):
    floor_no = (
        ('0', "Ground Floor"),
        ('1', "1st Floor"),
        ('2', "2nd Floor"),
        ('3', "3rd Floor"),
        ('4', "4th Floor"),
        ('5', "5th Floor"),
        ('6', "6th Floor"),
        ('7', "7th Floor"),
        ('8', "8th Floor"),
        ('9', "9th Floor"),
        ('10', "10th Floor"),
        ('11', "11th Floor"),
        ('12', "12th Floor"),
        ('13', "13th Floor"),
        ('14', "14th Floor"),
    )

    floor = models.CharField(default='', max_length=255, choices=floor_no)
    floor_name = models.CharField(default='', max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.floor_name) + "||" + str(self.floor)

# floor details
class FloorDetails(models.Model):

    floor_no = models.ForeignKey(FloorList, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to='floor_details')
    title = models.CharField(default='', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title














