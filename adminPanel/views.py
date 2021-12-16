from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import User, UserProfile
from adminPanel.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import uuid
import re
from core.models import Event, Store, Restaurants, BannerList




# admin panel index
@login_required(login_url='/ap/login/register')
def ap_index(request):
    # user profile
    userProfile = UserProfile.objects.get(user=request.user)

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context = {
        'userProfile': userProfile,
        'site_logo' : site_logo,
    }

    return render(request, 'back-end/admin_panel/index.html', context)

# admin panel home
@login_required(login_url='/ap/login/register')
def ap_home(request):
    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    user_list = User.objects.all()

    context = {
        'user_list' : user_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }


    return render(request, 'back-end/admin_panel/home.html', context)


# remove user
@login_required(login_url='/ap/login/register')
def ap_removeUser(request, pk):


    try:
        user = User.objects.get(pk=pk)
        user.delete()
        messages.success(request, "Successfully reoved user!")
        return redirect('apHome')
    except:
        messages.warning(request, "Can't be removed user! Try again!")
        return redirect('apHome')

    return redirect('apHome')


# add banner
@login_required(login_url='/ap/login/register')
def ap_addBanner(request):

    if request.method == "POST":
        banner = request.FILES['banner']

        if banner:
            banner = BannerList(img=banner)
            banner.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddBanner')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddBanner')

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    # banner list
    bannerList = BannerList.objects.all().order_by('-pk')[:5]

    context = {
        'userProfile': userProfile,
        'site_logo': site_logo,
        'bannerList': bannerList,
    }

    return render(request, 'back-end/admin_panel/add-banner.html', context)


# delete banner
@login_required(login_url='/ap/login/register')
def ap_delBanner(request, pk):

    try:
        banner = BannerList.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(banner.img.name)
        banner.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddBanner')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddBanner')

    return redirect('apAddBanner')

# add new event
@login_required(login_url='/ap/login/register')
def ap_addNew_Event(request):
    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    if request.method == 'POST':
        event__img = request.FILES['event__img']
        title = request.POST['event_title']
        place = request.POST['event_place']
        date = request.POST['event_date']
        starting_time = request.POST['event_time_start']
        ending_time = request.POST['event_end_time']
        publisher_name = request.POST['event_publisher_name']

        event_guest_1_name = request.POST['event_guest_1_name']
        event_guest_2_name = request.POST['event_guest_2_name']
        event_guest_3_name = request.POST['event_guest_3_name']

        event_guest_1_desig = request.POST['event_guest_1_desig']
        event_guest_2_desig = request.POST['event_guest_2_desig']
        event_guest_3_desig = request.POST['event_guest_3_desig']

        print(starting_time)


        try:
           try:
               guest_3_img = request.FILES['event_guest_3_img']
               event_model = Event(event_defualt_img=event__img,title=title,place=place,date=date,time_start=starting_time,time_end=ending_time,
                                   writer=publisher_name,guest3_img=guest_3_img,guest1_name=event_guest_1_name,guest2_name=event_guest_2_name,guest3_name=event_guest_3_name,
                                   guest_1_designation=event_guest_1_desig,guest_2_designation=event_guest_2_desig,guest_3_designation=event_guest_3_desig)
               event_model.save()
               messages.success(request, "Successfully added!")
               return redirect('apAddNewEvent')
           except:
               guest_2_img = request.FILES['event_guest_2_img']
               event_model = Event(event_defualt_img=event__img, title=title,place=place,date=date,time_start=starting_time,time_end=ending_time, writer=publisher_name, guest2_img=guest_2_img,
                                    guest1_name=event_guest_1_name, guest2_name=event_guest_2_name, guest3_name=event_guest_3_name, guest_1_designation=event_guest_1_desig,
                                   guest_2_designation=event_guest_2_desig, guest_3_designation=event_guest_3_desig)
               event_model.save()
               messages.success(request, "Successfully added!")
               return redirect('apAddNewEvent')
        except:
            try:
                guest_1_img = request.FILES['event_guest_1_img']
                event_model = Event(event_defualt_img=event__img, title=title,place=place,date=date,time_start=starting_time,time_end=ending_time, writer=publisher_name, guest1_img=guest_1_img,
                                    guest1_name=event_guest_1_name, guest2_name=event_guest_2_name,
                                    guest3_name=event_guest_3_name, guest_1_designation=event_guest_1_desig,
                                    guest_2_designation=event_guest_2_desig, guest_3_designation=event_guest_3_desig)
                event_model.save()
                messages.success(request, "Successfully added!")
                return redirect('apAddNewEvent')
            except:
                event_model = Event(event_defualt_img=event__img, title=title,place=place,date=date,time_start=starting_time,time_end=ending_time, writer=publisher_name,
                                    guest1_name=event_guest_1_name, guest2_name=event_guest_2_name,
                                    guest3_name=event_guest_3_name, guest_1_designation=event_guest_1_desig,
                                    guest_2_designation=event_guest_2_desig, guest_3_designation=event_guest_3_desig)
                event_model.save()
                messages.success(request, "Successfully added!")
                return redirect('apAddNewEvent')

    context = {
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add-new-event.html', context)


#  event list
@login_required(login_url='/ap/login/register')
def ap_EventList(request):
    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    eventList = Event.objects.all().order_by('-pk')[:10]

    context = {
        'eventList': eventList,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/event_list.html', context)

# add new store
@login_required(login_url='/ap/login/register')
def ap_addNew_store(request):

    if request.method == 'POST':
        brand_img = request.FILES['store_img']
        name = request.POST['brand_name']
        floor_no = request.POST['floor_no']
        product_for = request.POST['product_for']
        web_link = request.POST['store_web_link']

        if brand_img and name:
            store = Store(store_img=brand_img, brand_name=name,floor_no=floor_no, product_person_type=product_for, store_website_link=web_link)
            store.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddNewStore')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddNewStore')

    return render(request, 'back-end/admin_panel/add-store.html')


# store list
@login_required(login_url='/ap/login/register')
def ap_storeList(request):

    storeList = Store.objects.all().order_by('-pk')[:10]

    context = {
        'storeList': storeList,
    }

    return render(request, 'back-end/admin_panel/store_list.html', context)


# add new restaurants
@login_required(login_url='/ap/login/register')
def ap_addNew_restaurants(request):

    if request.method == 'POST':
        restaurant_img = request.FILES['restaurant_img']
        restaurant_name = request.POST['restaurant_name']
        floor_no = request.POST['floor_no']
        web_link = request.POST['restaurant_web_link']

        if restaurant_name and restaurant_img:
            restaurant = Restaurants(restaurants_img=restaurant_img, name=restaurant_name, floor_no=floor_no, resrants_website_link=web_link)
            restaurant.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddNewRestaurants')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddNewRestaurants')

    return render(request, 'back-end/admin_panel/add_restaurants.html')


# restaurant list
@login_required(login_url='/ap/login/register')
def ap_restauRantList(request):

    restaurantList = Restaurants.objects.all().order_by('-pk')[:10]

    context = {
        'restaurantList': restaurantList,
    }

    return render(request, 'back-end/admin_panel/restaurant_list.html', context)

# admin panel edit breaking news
@login_required(login_url='/ap/login/register')
def ap_addSiteLogo(request):

    if request.method == 'POST':

        logo = request.FILES['upload_logo']

        list_of_logo_extension = str(logo).split('.')
        allowed_logo_extensions = ['png', 'jpg', 'jpeg', 'webp']

        if list_of_logo_extension[len(list_of_logo_extension)-1] in allowed_logo_extensions:
            site_logo_model = SiteLogo(logo=logo)
            site_logo_model.save()
            messages.success(request, "Successfully uploaded!")
            return redirect('apAddSiteLogo')
        else:
            messages.warning(request, "Can't be uploaded logo! Please tyr again!")
            return redirect('apAddSiteLogo')

    # grab all logos
    logo_list = SiteLogo.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()
    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'logo_list': logo_list,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }



    return render(request, 'back-end/admin_panel/add-logo.html', context)


# admin panel delete breaking news
@login_required(login_url='/ap/login/register')
def ap_delSiteLogo(request, logo_id):

    try:
        logo_by_its_id = get_object_or_404(SiteLogo, pk=logo_id)
        fs = FileSystemStorage()
        fs.delete(logo_by_its_id.logo.name)
        logo_by_its_id.delete()
        messages.success(request, "Successfully deleted!")
        return redirect("apAddSiteLogo")
    except:
        messages.warning(request, "Can't deleted! Please try again!")
        return redirect("apAddSiteLogo")

    return redirect('apAddSiteLogo')

# admin panel delete breaking news
@login_required(login_url='/ap/login/register')
def ap_editSiteLogo(request, logo_id):

    if request.method == 'POST':
        logo = request.FILES['edit_site_logo']
        list_of_logo_extension = str(logo).split('.')
        allowed_logo_extensions = ['png', 'jpg', 'jpeg', 'webp']

        if list_of_logo_extension[len(list_of_logo_extension) - 1] in allowed_logo_extensions:
            try:
                site_logo_model = get_object_or_404(SiteLogo, pk=logo_id)
                fs = FileSystemStorage()
                fs.delete(site_logo_model.logo.name)
                site_logo_model.logo = logo
                site_logo_model.save()
                messages.success(request, "Site logo updated successfully!")
                return redirect('apAddSiteLogo')
            except:
                messages.warning(request, "Site logo can't update! Please try again!")
                return redirect('apAddSiteLogo')
        else:
            messages.warning(request, "Logo can't be updated! Please try again!")
            return redirect('apAddSiteLogo')

    return redirect('apAddSiteLogo')

# admin panel contact information
@login_required(login_url='/ap/login/register')
def ap_addSiteContactInfo(request):

    if request.method == "POST":

        phone_number = request.POST.get("mobile_no")
        email = request.POST.get("email")
        address = request.POST.get("address")

        try:
            siteContactInfor = SiteContactInfo(phone=phone_number, email=email, address=address)
            siteContactInfor.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddSiteContactInfo')
        except:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAddSiteContactInfo')

    # site contact info
    siteContactInforList = SiteContactInfo.objects.all()

    # site contact info in bangla
    siteContactInforListBangla = SiteContactInfoBangla.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'siteContactInforList' : siteContactInforList,
        'siteContactInforListBangla': siteContactInforListBangla,
        # user profile

        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/contact_information.html', context)


# admin panel delete contact information
@login_required(login_url='/ap/login/register')
def ap_delSiteContactInfo(request, contact_id):

    try:
        siteContactInfo_by_id = get_object_or_404(SiteContactInfo, pk=contact_id)
        siteContactInfo_by_id.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddSiteContactInfo')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')

# admin panel edit contact information
@login_required(login_url='/ap/login/register')
def ap_editSiteContactInfo(request, contact_id):

    if request.method == 'POST':
        phone = request.POST.get('edit_phone')
        email = request.POST.get('edit_email')
        address = request.POST.get('edit_address')

        try:
            siteContactInfo_by_id = get_object_or_404(SiteContactInfo, pk=contact_id)
            siteContactInfo_by_id.phone = phone
            siteContactInfo_by_id.email = email
            siteContactInfo_by_id.address = address
            siteContactInfo_by_id.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddSiteContactInfo')
        except:
            messages.warning(request, "Can't be updated! Try again!")
            return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')


# admin panel contact information in bangla
@login_required(login_url='/ap/login/register')
def ap_addSiteContactInfoBangla(request):

    if request.method == "POST":

        phone_number = request.POST.get("mobile_no")
        email = request.POST.get("email")
        address = request.POST.get("address")

        try:
            siteContactInforBangla = SiteContactInfoBangla(phone=phone_number, email=email, address=address)
            siteContactInforBangla.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddSiteContactInfo')
        except:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAddSiteContactInfo')

    # site contact info
    siteContactInforListBangla = SiteContactInfoBangla.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'siteContactInforListBangla' : siteContactInforListBangla,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/contact_information.html', context)

# delete site contact info bangla
@login_required(login_url='/ap/login/register')
def ap_deleteSiteContactInfoBangla(request, pk):

    try:
        site_contact_info_bd = SiteContactInfoBangla.objects.get(pk=pk)
        site_contact_info_bd.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddSiteContactInfo')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')


# delete site contact info bangla
@login_required(login_url='/ap/login/register')
def ap_editSiteContactInfoBangla(request, pk):

    if request.method == "POST":
        phone = request.POST['edit_phone']
        email = request.POST['edit_email']
        address = request.POST['edit_address']

        if phone and email and address:
            siteContactInfoBd = SiteContactInfoBangla.objects.get(pk=pk)
            siteContactInfoBd.phone = phone
            siteContactInfoBd.email = email
            siteContactInfoBd.address = address
            siteContactInfoBd.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')


# about us
@login_required(login_url='/ap/login/register')
def ap_aboutUs(request):

    if request.method == 'POST':
        about_us_txt = request.POST['about_us']

        if about_us_txt:
            about_us_model = AboutUs(about_us=about_us_txt)
            about_us_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAboutUs')
        else:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAboutUs')

    # about us model
    aboutUs = AboutUs.objects.filter().first()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'about_us' : aboutUs,
        # user profile
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/about_us.html', context)

# delete about us
@login_required(login_url='/apLoginRegister/')
def ap_delAboutUs(request, pk):

    try:
        about_us_model = AboutUs.objects.get(pk=pk)
        about_us_model.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAboutUs')
    except:
        messages.warning(request, "Try again!")
        return redirect('apAboutUs')

    return redirect('apAboutUs')

# edit about us
@login_required(login_url='/ap/login/register')
def ap_editAboutUs(request, pk):

    if request.method == 'POST':
        about_us = request.POST['about_us']

        if about_us:
            about_us_model_byPK = AboutUs.objects.get(pk=pk)
            about_us_model_byPK.about_us = about_us
            about_us_model_byPK.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAboutUs')
        else:
            messages.warning(request, "Try again!")
            return redirect('apAboutUs')

    return redirect('apAboutUs')

# msg list
@login_required(login_url='/ap/login/register')
def ap_VisitorMsgList(request):

    # msg model
    msg_list = Message.objects.all()


    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'msg_list' : msg_list,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, "back-end/admin_panel/msg_list.html", context)

# msg delete
@login_required(login_url='/ap/login/register')
def ap_DelVisitorMsg(request, pk):

    try:
        msg = Message.objects.get(pk=pk)
        msg.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apVisitorMessageList')
    except:
        messages.warning(request, "Something wrong! Try again!")
        return redirect('apVisitorMessageList')

    return redirect('apVisitorMessageList')


# add social media link
@login_required(login_url='/ap/login/register')
def ap_addSocialMediaLink(request):

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    if request.method == 'POST':
        fb = request.POST['fb_link']
        tw = request.POST['tw_link']
        insta = request.POST['insta_link']
        linkedIn = request.POST['linkIn_link']

        if fb != '' or tw != '' or insta != '' or linkedIn != '':
            socialMediaLink_model = SocailMediaLinks(fb=fb, tw=tw, insgrm=insta,linkedin=linkedIn)
            socialMediaLink_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddSocialMediaLink')

        else:
            messages.warning(request, "Something wrong! Try again!")
            return redirect('apAddSocialMediaLink')

    existing_links = SocailMediaLinks.objects.filter().first()

    context = {
        'social_media_links' : existing_links,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }


    return render(request, 'back-end/admin_panel/add_social_media_link.html', context)


# delete social media link
@login_required(login_url='/ap/login/register')
def ap_delSocialMediaLink(request, pk):

    try:
        social_media_link_model = SocailMediaLinks.objects.get(pk=pk)
        social_media_link_model.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddSocialMediaLink')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apAddSocialMediaLink')

    return redirect('apAddSocialMediaLink')


# edit social media link
@login_required(login_url='/ap/login/register')
def ap_editSocialMediaLink(request, pk):

    if request.method == 'POST':
        fb_link = request.POST['fb_link']
        tw_link = request.POST['tw_link']
        insta_link = request.POST['insta_link']
        linkIn_link = request.POST['linkIn_link']

        if fb_link != '' or tw_link != '' or insta_link != '' or linkIn_link != '':
            social_media_model = SocailMediaLinks.objects.get(pk=pk)
            social_media_model.fb = fb_link
            social_media_model.tw = tw_link
            social_media_model.insgrm = insta_link
            social_media_model.linkedin = linkIn_link

            social_media_model.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddSocialMediaLink')
        else:
            messages.warning(request, "Can't be updated! Try again!")
            return redirect('apAddSocialMediaLink')


    return redirect('apAddSocialMediaLink')


# book appointment img
@login_required(login_url='/ap/login/register')
def ap_bookApointment(request):

    if request.method == 'POST':
        img = request.FILES['img']

        if img:
            book_apntment = BookAppointment(img=img)
            book_apntment.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddBookAppointment')
        else:
            messages.warning(request, "Something wrong try again!")
            return redirect('apAddBookAppointment')

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    listOf_appointment_img = BookAppointment.objects.filter().order_by('-pk')

    context = {
        'listOf_appointment_img': listOf_appointment_img,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_img_beside_appointmnt.html', context)

# delete book appointment img
@login_required(login_url='/ap/login/register')
def ap_delBookAppointment(request, pk):

    try:
        book_appointment_img = BookAppointment.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(book_appointment_img.img.name)
        book_appointment_img.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddBookAppointment')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddBookAppointment')

    return redirect('apAddBookAppointment')


# booking appointment list
@login_required(login_url='/ap/login/register')
def ap_bookingAppointmentList(request):

    # grab request list
    appointment_request_list = BookingAppointmentRequest.objects.all().order_by('-pk')

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context = {
        'appointment_request_list': appointment_request_list,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/ap_booking_appointment_list.html', context)


# booking appointment list
@login_required(login_url='/ap/login/register')
def ap_delBookingRequest(request, pk):

    try:
        appointment_request = BookingAppointmentRequest.objects.get(pk=pk)
        appointment_request.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apBookingAppointmentList')
    except:
        messages.warning(request, "Sorry can't be deleted. Try again")
        return redirect('apBookingAppointmentList')

    return redirect('apBookingAppointmentList')



# add items to floor
@login_required(login_url='/ap/login/register')
def ap_addItems_toFloor(request):

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    floor_list = FloorList.objects.all()


    if request.method == 'POST':
        floor_no = request.POST['floor_no']
        store_img = request.FILES['store_img']
        store_name = request.POST['store_name']

        print(floor_no, store_img, store_name)

        if floor_no and store_img and store_img:

            floor_item_model = FloorDetails(floor_no=FloorList.objects.get(pk=floor_no), img=store_img, title=store_name)
            floor_item_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddItemsToFloor')
        else:
            messages.warning(request, "Can't be added. Try again!")
            return redirect('apAddItemsToFloor')

    context = {
        'floor_list': floor_list,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_items_to_floor.html', context)


# list of items to floor
@login_required(login_url='/ap/login/register')
def ap_listItems_toFloor(request):

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    floor_items_list = FloorDetails.objects.all()


    context = {
        'floor_items_list': floor_items_list,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/floor_items_list.html', context)