"""Views for user package"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from dashboard.models import HealthData
from .utils import date_to_str

@login_required(login_url='user:login')
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
   
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    # Get current year
    now = datetime.now()
    current_year = now.year
    # Get current time
    time = now.strftime('%I:%M:%S %p')

    qs = HealthData.objects.filter(user= request.user)
   
    x_gl = [0]
    x_w = [0]
    x_h = [0]
    prediab = [0]
    diab = [0]
    y = []
    for data in qs:
        x_gl.append(data.gl_level)
        x_w.append(data.weight)
        x_h.append(data.height)
        prediab.append(140)
        diab.append(200)
        y.append(date_to_str(data.day))


    context = {"year": year,
                "month": month,
                "month_number": month_number,
                "cal": cal,
                "current_year": current_year,
                "time": time,
                "health_data": qs,
                "glucose": x_gl,
                "prediab": prediab,
                "diab": diab,
                "weight": x_w,
                "height": x_h,
                "date": y,
                }

    return render(request, 'base/home.html', context)



class RegisterView(View):
    """View class for registration"""

    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'auth/registration.html'

    def dispatch(self, request, *args, **kwargs):
        """redirect to the home page if a user tries to access
        the register page while logged in"""

        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """get registration form"""
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """post registration form data"""
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    """View class for login"""

    form_class = LoginForm

    def form_valid(self, form):
        """validate login form"""
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session
            # after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time
        # "SESSION_COOKIE_AGE" defined in settings.py

        return super(CustomLoginView, self).form_valid(form) # noqa


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """View class for reseting passwords"""

    template_name = 'auth/password_reset.html'
    email_template_name = 'auth/password_reset_email.html'
    subject_template_name = 'auth/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
        "if an account exists with the email you entered. You should receive them shortly." \
        " If you don't receive an email, please make sure you've entered the address you " \
        "registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    """View class for changing passwords"""

    template_name = 'auth/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-profile')


@login_required(login_url='user:login')
def profile(request):
    """update profile data"""
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user:users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'auth/profile.html', {'user_form': user_form, 
    'profile_form': profile_form})
