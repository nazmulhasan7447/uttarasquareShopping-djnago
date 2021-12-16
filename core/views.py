from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Event, Store, Restaurants, NewsLetter, BannerList
from adminPanel.models import Message, SocailMediaLinks, SiteLogo, SiteContactInfo, AboutUs, BookAppointment, BookingAppointmentRequest, FloorList, FloorDetails


def fe_index(request):

    social_media_links = SocailMediaLinks.objects.filter().first()

    site_logo = SiteLogo.objects.filter().first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'social_media_link' : social_media_links,
        'contact_info': contact_info,
        'site_logo': site_logo,
    }

    return render(request, 'front-end/index.html', context)


def fe_home(request):
    # grabing event list
    event_list = Event.objects.all().order_by('-pk')[:7]

    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    social_media_links = SocailMediaLinks.objects.filter().first()

    banner = BannerList.objects.filter().order_by('-pk')[:4]

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    book_appointment_img = BookAppointment.objects.filter().order_by('-pk').first()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        if name and email:
            newsletter = NewsLetter(name=name, email=email)
            newsletter.save()
            messages.success(request, "Successfully sent!")
            return redirect('feHome')

    context = {
        'event_list': event_list,
        'social_media_link': social_media_links,
        'site_logo': site_logo,
        'bannerList': banner,
        'contact_info':contact_info,
        'book_appointment_img': book_appointment_img,
    }

    return render(request, 'front-end/home.html', context)

def fe_storeDirectory(request):

    return render(request, 'front-end/store_directory.html')

def fe_about(request):
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    about_us = AboutUs.objects.filter().order_by('-pk').first()

    context = {
        'site_logo': site_logo,
        'contact_info':contact_info,
        'about_us': about_us,
    }

    return render(request, 'front-end/about.html', context)


def fe_book_appontment(request):
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date_1 = request.POST['date_time1']
        date_2 = request.POST['date_time2']
        date_3 = request.POST['date_time3']
        subject = request.POST['subj']
        msg = request.POST['message']

        print(name, email, phone, date_3, date_2, date_1, subject, msg)

        if name and email and phone and date_1 and subject and msg:
            save_to_model = BookingAppointmentRequest(name=name, email=email, phone=phone, date_choice_1=date_1, date_choice_2=date_2, date_choice_3=date_3, subject=subject, msg=msg)
            save_to_model.save()
            messages.success(request, "Successfully sent your booking request!")
            return redirect('feBookAppointment')
        else:
            messages.warning(request, "Something Wrong. Try again!")
            return redirect('feBookAppointment')

    context = {
        'site_logo': site_logo,
        'contact_info':contact_info,
    }

    return render(request, 'front-end/book_appointment.html', context)

def fe_contact(request):

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        sub = request.POST['subj']
        msg = request.POST['msg']

        if name and email and phone and sub and msg:
            visitors_msg = Message(name=name, email=email,phone=phone,sub=sub, msg=msg)
            visitors_msg.save()
            messages.success(request, "Successfully sent!")
            return redirect('feContactUs')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('feContactUs')

    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'site_logo': site_logo,
        'contact_info': contact_info,
    }
    return render(request, 'front-end/contact.html', context)


def fe_eventList(request):

    # grabing event list
    event_list = Event.objects.all().order_by('-pk')[:7]

    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'event_list': event_list,
        'site_logo': site_logo,
        'contact_info':contact_info,
    }

    return render(request, 'front-end/event-list.html', context)

def fe_eventDetails(request):
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'site_logo': site_logo,
        'contact_info':contact_info,
    }

    return render(request, 'front-end/event-details.html', context)


def fe_restaurants(request):

    # grabing restaurants
    restaurants_list = Restaurants.objects.all().order_by('-pk')[:9]

    site_logo = SiteLogo.objects.filter().order_by('-pk').first()
    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'restaurants_list': restaurants_list,
        'site_logo': site_logo,
        'contact_info':contact_info,
    }

    return render(request, 'front-end/restaurants.html', context)

def fe_service(request):
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'site_logo': site_logo,
        'contact_info':contact_info,
    }

    return render(request, 'front-end/service.html', context)

def fe_floor(request):
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    floor_list = FloorList.objects.all()

    context = {
        'site_logo': site_logo,
        'contact_info': contact_info,
        'floor_list' : floor_list,
    }

    return render(request, 'front-end/floor.html', context)


def fe_floor_details(request, pk):
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    # grabing floor
    floor_details = FloorDetails.objects.filter(floor_no=pk).order_by('-pk')
    floor_no = FloorList.objects.filter(pk=pk).first()

    context = {
        'site_logo': site_logo,
        'contact_info': contact_info,
        'floor_details': floor_details,
        'floor_no': floor_no,
    }

    return render(request, 'front-end/floor_details.html', context)

def fe_shop(request):

    # grabing shop list
    shop_or_store_list = Store.objects.all().order_by('-pk')[:9]

    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'shop_or_store_list': shop_or_store_list,
        'site_logo': site_logo,
        'contact_info':contact_info,
    }

    return render(request, 'front-end/shop.html', context)

def fe_shop_details(request):

    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'site_logo': site_logo,

        'contact_info':contact_info,
    }

    return render(request, 'front-end/shop_details.html', context)

def fe_convention_hall(request):
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    contact_info = SiteContactInfo.objects.filter().order_by('-pk').first()

    context = {
        'site_logo': site_logo,
        'contact_info': contact_info,
    }

    return render(request, 'front-end/convention-hall.html', context)


