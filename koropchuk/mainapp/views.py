# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.reverse import reverse_lazy

from bookingapp.models import *
from mainapp.forms import BookingAPierForm, LoginUserForm
from mainapp.models import *
from datetime import datetime


# def index(request):
#     return render(request, 'mainapp/index.html', {'title': 'Головна сторінка'})


# def index(request):
#     pier_1 = BookingPier.objects.filter(pier_id=1)[:1]
#     pier_2 = BookingPier.objects.filter(pier_id=2)[:1]
#     pier_3 = BookingPier.objects.filter(pier_id=3)[:1]
#     context = {
#         'pier_1': pier_1,
#         'pier_2': pier_2,
#         'pier_3': pier_3,
#         'title': 'Головна сторінка Коропчук',
#         'cat_selected': 0,
#     }
#     return render(request, 'mainapp/index.html', context=context)
from mainapp.utils import DataMixin

menu = [{'title': 'Про нас', 'url_name': 'about'},
       {'title': 'Договір', 'url_name': 'contract'},
       {'title': "Зворотній зв'язок", 'url_name': 'contact'},
       {'title': 'Авторизація', 'url_name': 'login'}
       ]

def index(request):
    # posts = Article.objects.all()
    head_posts = Article.objects.filter(cat_id=1)[:1]
    news_posts = Article.objects.filter(cat_id=2)[:1]
    advert_posts = Article.objects.filter(cat_id=3)[:1]
    # cats = Category.objects.all()
    piers = Pier.objects.all()
    now = datetime.now()
    book_free = BookingPier.objects.filter(pier_id=111)[:1]
    pier_1 = BookingPier.objects.filter(pier_id=1, time_booking_start__lte=now, time_booking_finish__gte=now)
    pier_2 = BookingPier.objects.filter(pier_id=2, time_booking_start__lte=now, time_booking_finish__gte=now)
    pier_3 = BookingPier.objects.filter(pier_id=3, time_booking_start__lte=now, time_booking_finish__gte=now)
    # if pier_1('time_booking_start'>='time_booking_start', time_booking_finish__gte='time_booking_finish'):
    #     raise Http404()
    context = {
        # 'posts': posts,
        'head_posts': head_posts,
        'news_posts': news_posts,
        'advert_posts': advert_posts,
        # 'cats': cats,
        'piers': piers,
        # 'menu': menu,
        'pier_1': pier_1 or book_free,
        'pier_2': pier_2 or book_free,
        'pier_3': pier_3 or book_free,
        'title': 'Головна сторінка Коропчук',
        'cat_selected': 0,
    }
    return render(request, 'mainapp/index.html', context=context)


# def bookingSubmit(request):
#     #     # Get stored data from django session:
#     time_booking_start = request.session.get('time_booking_start')
#     time_booking_finish = request.session.get('time_booking_finish')
#     pier_status = request.session.get('pier_status')
#     pier_id = request.session.get('pier_id')
# #     today = datetime.now()
# #     minDate = today.strftime('%Y-%m-%d')
# #     deltatime = today + timedelta(days=21)
# #     strdeltatime = deltatime.strftime('%Y-%m-%d')
# #     maxDate = strdeltatime
#     #Only show the time of the day that has not been selected before:
#     check_pier_id = checkPierID()
#     check_time_booking_start = checkDateTime(time_booking_start)
#     if request.method == 'POST':
#         time = request.POST.get("time")
# #        date = dayToWeekday(day)


# def checkPierID(pier_id):
#     #Only show the time of the day that has not been selected before:
#     x = []
#     for k in pier_id:
#         if BookingPier.objects.filter(pier_id=k, k=k).count() < 1:
#             x.append(k)
#     return x
#
#
# def checkDateTime(time_booking_start, time_booking_finish):
#     #Only show the time of the day that has not been selected before:
#     x = []
#     for k in time_booking_start:
#         if BookingPier.objects.filter(time_booking_start=k) >= BookingPier.objects.filter(time_booking_finish=k).count():
#             x.append(k)
#     return x


#
#
#     # Only show the time of the day that has not been selected before:
#     hour = checkTime(times, day)
#     if request.method == 'POST':
#         time = request.POST.get("time")
#         date = dayToWeekday(day)
#
#         if service != None:
#             if day <= maxDate and day >= minDate:
#                 if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
#                     if Appointment.objects.filter(day=day).count() < 11:
#                         if Appointment.objects.filter(day=day, time=time).count() < 1:
#                             AppointmentForm = Appointment.objects.get_or_create(
#                                 user=user,
#                                 service=service,
#                                 day=day,
#                                 time=time,
#                             )
#                             messages.success(request, "Appointment Saved!")
#                             return redirect('index')
#                         else:
#                             messages.success(request, "The Selected Time Has Been Reserved Before!")
#                     else:
#                         messages.success(request, "The Selected Day Is Full!")
#                 else:
#                     messages.success(request, "The Selected Date Is Incorrect")
#             else:
#                 messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
#         else:
#             messages.success(request, "Please Select A Service!")
#
#     return render(request, 'bookingSubmit.html', {
#         'times': hour,
#     })


def about(request):
    return render(request, 'mainapp/about.html', {'title': 'Про нас'})


def contract(request):
    return render(request, 'mainapp/doc/contract.html', {'title': 'Договір'})


def instruction(request):
    return render(request, 'mainapp/doc/instruction.html', {'title': 'Інструкція'})


def rules(request):
    return render(request, 'mainapp/doc/rules.html', {'title': 'Правила'})


def information(request):
    iposts = Article.objects.filter(cat_id=3)[:9]
    cats = Category.objects.all()
    context = {
        'iposts': iposts,
        'cats': cats,
        'title': 'Інформація',
        'cat_selected': 0,
    }
    return render(request, 'mainapp/information.html', context=context)

# def login(request):
#     return render(request, 'mainapp/login.html', {'title': 'Логін'})


def pier(request, pier_id):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Page of piers</h1>"
                        f"<p>{pier_id}</p>")


def show_post(request, post_slug):
    # return HttpResponse(f"Відображення допису з id = {post_id}")
    post = get_object_or_404(Article, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'mainapp/post.html', context=context)


# def show_category(request, cat_id):
#     return HttpResponse (f"Відображення статті з id = {cat_id}")

# def show_category(request, cat_id):
#      return HttpResponse(f"Відображення категорії з id = {cat_id}")

def show_category(request, cat_id):
    posts = Article.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        # 'cats': cats,
        # 'menu': menu,
        'title': 'Відображення за категоріями',
        'cat_selected': cat_id,
    }
    return render(request, 'mainapp/index.html', context=context)


def bookingapier(request):
    # form = BookingAPierForm()
    if request.method == 'POST':
        form = BookingAPierForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = BookingAPierForm()
    return render(request, 'mainapp/bookingapier.html', {'form': form, 'title': 'Бронювання місця'})


# def bookingapier(request):
#     if request.method == 'POST':
#         form = BookingAPierForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = BookingAPierForm()
#     return render(request, 'mainapp/bookingapier.html', {'form': form, 'menu': menu, 'title': 'Бронювання пірсу'})

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    # form_class = AuthenticationForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизація')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        # return reverse_lazy('bookingapier_rest')
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

# class LoginUser(DataMixin, LoginView):
#     form_class = LoginUserForm
#     template_name = 'mainapp/login.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Авторизація')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     # def get_success_url(self):
#     #     return reverse_lazy('bookingapier')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінки не ісує</h1>')
