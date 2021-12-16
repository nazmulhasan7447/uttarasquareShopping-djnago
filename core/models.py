from django.db import models


class BannerList(models.Model):

    img = models.ImageField(upload_to='banner')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)



class EventGuest1(models.Model):
    img = models.ImageField(upload_to='Guest_images')
    name = models.CharField(default='', max_length=255)
    designation = models.CharField(default='', max_length=255)

    def __str__(self):
        return self.name


class EventGuest2(models.Model):
    img = models.ImageField(upload_to='Guest_images')
    name = models.CharField(default='', max_length=255)
    designation = models.CharField(default='', max_length=255)

    def __str__(self):
        return self.name


class EventGuest3(models.Model):
    img = models.ImageField(upload_to='Guest_images')
    name = models.CharField(default='', max_length=255)
    designation = models.CharField(default='', max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(default='', max_length=255)
    place = models.CharField(default='', max_length=255)
    date = models.CharField(default='', max_length=255)
    time_start = models.CharField(default='', max_length=255)
    time_end = models.CharField(default='', max_length=255)
    writer = models.CharField(default='', max_length=255, blank=True, null=True)

    event_defualt_img = models.ImageField(upload_to="Event_default_img", blank=True, null=True)

    guest1_img = models.ImageField(upload_to='Guest_images', blank=True, null=True)
    guest2_img = models.ImageField(upload_to='Guest_images', blank=True, null=True)
    guest3_img = models.ImageField(upload_to='Guest_images', blank=True, null=True)

    guest1_name = models.CharField(max_length=255, default='', blank=True, null=True)
    guest2_name = models.CharField(max_length=255, default='', blank=True, null=True)
    guest3_name = models.CharField(max_length=255, default='', blank=True, null=True)

    guest_1_designation = models.CharField(max_length=255, default='', blank=True, null=True)
    guest_2_designation = models.CharField(max_length=255, default='', blank=True, null=True)
    guest_3_designation = models.CharField(max_length=255, default='', blank=True, null=True)

    guest1 = models.ForeignKey(EventGuest1, on_delete=models.PROTECT, blank=True, null=True)
    guest2 = models.ForeignKey(EventGuest2, on_delete=models.PROTECT, blank=True, null=True)
    guest3 = models.ForeignKey(EventGuest3, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title + "||" + str(self.date)



# store
class Store(models.Model):

    product_for = (
        ('woman', "Woman"),
        ('man', "Man's"),
        ('kids', "Kid's"),
        ('toys', "Toy's"),
        ('others', 'Others'),
    )

    store_img = models.ImageField(upload_to='store_img', blank=True, null=True)
    brand_name = models.CharField(default='', max_length=255)
    floor_no = models.CharField(default='', max_length=255)
    product_person_type = models.CharField(default='', max_length=255, choices=product_for)
    store_website_link = models.CharField(default='', max_length=300)

    def __str__(self):
        return self.brand_name



# restaurants
class Restaurants(models.Model):

    restaurants_img = models.ImageField(upload_to='restaurants_img', blank=True, null=True)
    name = models.CharField(default='', max_length=255)
    floor_no = models.CharField(default='', max_length=255)
    resrants_website_link = models.CharField(default='', max_length=300)

    def __str__(self):
        return self.name


# newsletter
class NewsLetter(models.Model):

    name = models.CharField(default='', max_length=255, blank=True, null=True)
    email = models.CharField(default='', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name + "||" + self.email















