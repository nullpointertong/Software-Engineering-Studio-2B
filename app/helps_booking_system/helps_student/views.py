from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import StudentAccount, Workshop, Session
from .forms import StudentForm

from django.db import connection
import datetime
from .helpers import send_email
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json


def login_request(request):
    context = {'login_request': 'active'}
    return render(request, 'registration/login.html', context)


def profile(request):
    context = {'profile_page': 'active'}
    return render(request, 'pages/layouts/profile.html', context)


def submit_profile(request):
    print("DEBUG FORM ADDED")
    # Debug message
    # SQL Query to retrieve current Student ID - temp field:
    student_id = request.POST["student_id"]
    # Retrieve Information from HTML
    student_first_name = request.POST["student_first_name"]
    student_last_name = request.POST["student_last_name"]
    student_preferred_first_name = request.POST["student_preferred_first_name"]
    #student_preferred_last_name = request.POST["student_preferred_last_name"]
    student_faculty = request.POST["student_faculty"]
    student_course = request.POST["student_course"]
    student_email = request.POST["student_email"]
    student_home_phone = request.POST["student_home_phone"]
    student_mobile = request.POST["student_mobile"]
    student_best_contactno = request.POST["student_best_contactno"]
    student_DOB = request.POST["student_DOB"]
    student_gender = request.POST["student_gender"]
    student_degree = request.POST["student_degree"]
    #student_year = request.POST["student_year"]
    student_status = request.POST["student_status"]
    student_language = request.POST["student_language"]
    student_country = request.POST["student_country"]
    #student_name = request.POST["student_name"]
    student_account = StudentAccount(
        # Piping Infomration into Model
        student_id=student_id,
        first_name=student_first_name,
        last_name=student_last_name,
        email=student_email,
        faculty=student_faculty,
        course=student_course,
        preferred_first_name=student_preferred_first_name,
        #preferred_last_name = student_preferred_last_name,
        phone=student_home_phone,
        mobile=student_mobile,
        best_contact_no=student_best_contactno,
        DOB=student_DOB,
        gender=student_gender,
        degree=student_degree,
        status=student_status,
        first_language=student_language,
        country_of_origin=student_country

        # Needs to be made into an array educational_background = models.CharField(max_length=30)
    )
    student_account.save()
    context = {'profile_page': 'active'}
    return render(request, 'pages/layouts/profile.html', context)


def bookings(request):
    currentSessions = Session.objects.filter(
        date__gte=datetime.datetime.now()).order_by('date', 'start_time')
    pastSessions = Session.objects.filter(
        date__lt=datetime.datetime.now()).order_by('date', 'start_time')

    context = {'booking_page': 'active',
               'currentSessions': currentSessions, 'pastSessions': pastSessions}
    return render(request, 'pages/layouts/booking.html', context)


def cancelSession(request):
    print('cancel sessions')
    sesid = request.GET.get('sessionid', None)
    session = Session.objects.filter(session_ID=sesid)[0]
    session.delete()
    html_message = render_to_string('email/email.html', {'date': session.date.strftime("%d/%m/%y"), 'starttime': session.start_time.strftime(
        '%I:%M %p'), 'endtime': session.end_time.strftime('%I:%M %p'), 'location': session.location, 'staffname': session.staff.first_name, 'word': 'cancelled'})
    plain_message = strip_tags(html_message)
    emailContent = {
        'subject': 'Your UTS HELPS session with {} on {} {} has been cancelled'.format(session.staff.first_name, session.date.strftime("%d/%m/%y"), session.start_time.strftime('%I:%M %p')),
        'html_message': html_message,
        'plain_message': plain_message,
        'contacts': [session.student.email, session.staff.email]
    }
    send_email(emailContent)
    return redirect('bookings')


def workshops(request):
    # Retrieve all available workshops
    workshops = Workshop.objects.all()
    # Retrieve logged in user's enrolled workshops TODO: Remove hard-coded user and use authentication
    #### DEBUG ONLY:
    student = StudentAccount.objects.all().get(student_id="10000000")
    ####
    # student = request.user
    enrolled_workshops = [workshop for workshop in workshops if student in workshop.students.all()]
    date_context = {'date_filters': []}
    # If POST, retrieve filters
    if request.method == "POST":
        # Retrieve data
        data = request.POST
        # Determine if form submission was a withdrawal, filter or registration
        if 'withdraw_post' in data:
            # Search for workshop
            workshop_id = data['withdrawal_id']
            for workshop in workshops:
                if str(workshop.workshop_ID) == workshop_id:
                    # Remove student from workshop
                    workshop.students.remove(student)
                    enrolled_workshops.remove(workshop)
        elif 'filter_post' in data:
            # Filter workshops by dates (if valid)
            if data['start_date']:
                workshops = workshops.filter(end_date__gte=data['start_date'])
                date_context['date_filters'].append('After: {}'.format(data['start_date']))
            if data['end_date']:
                workshops = workshops.filter(start_date__lte=data['end_date'])
                date_context['date_filters'].append('Before: {}'.format(data['end_date']))
        # Form submission was for registration of workshop
        elif 'registration_post' in data:
            # Retrieve Workshop to be registered to
            workshop_id = data['workshop_id']
            for workshop in workshops:
                if str(workshop.workshop_ID) == workshop_id:
                    # Add student to workshop if not in workshop
                    if student not in workshop.students.all():
                        workshop.students.add(student)
                        enrolled_workshops.append(workshop)
    context = {
        **date_context,
        'workshops_page': 'active',
        'enr_workshops': enrolled_workshops,
        'workshops': workshops
    }
    # Pass content for js
    context['workshops_for_js'] = [str(workshop.workshop_ID) for workshop in workshops]
    context['workshops_skills_js'] = [workshop.skill_set_name for workshop in workshops]
    return render(request, 'pages/layouts/workshops.html', context)


def programs(request):
    context = {'programs_page': 'active'}
    return render(request, 'pages/layouts/programs.html', context)


def faq(request):
    context = {'faq_page': 'active'}
    return render(request, 'pages/layouts/faq.html', context)


def exit(request):
    logout(request)
    return redirect_view(request)


def redirect_view(request):
    response = redirect('/accounts/login/')
    return response
