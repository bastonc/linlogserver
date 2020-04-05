from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from .models import Chek_update, Register_new, Version, Template, Admins
from django.contrib.auth import authenticate, login, logout

def htu(request):
    template_data = Template.objects.filter(page_name="htu")
    template_context = {'template': template_data[0], 'today_year': timezone.now().year}
    return HttpResponse(render(request, "telnet_server/htu.html", template_context))

def index(request):
    template_data = Template.objects.filter(page_name="main")
    template_context = {'template': template_data[0], 'today_year': timezone.now().year}
    return HttpResponse(render(request, "telnet_server/index.html", template_context))


def updater(request, version_input, call_input):
    flag=0
    new_version_list = []
    print(call_input)
    try:
        version_list = Version.objects.all()
        for ver in version_list:
            version_url =float(version_input)
            version_in_base = float(ver.version)

            if version_in_base > version_url:
                new_version_list.append(ver)
                new_version_list.reverse()
                #new_version_list.sort()
                #sorted(new_version_list)

                flag = 1
            if version_in_base == version_url and flag == 0:
                flag = 2

        if flag == 1:
            context = {'version_list': new_version_list}
            check_user = Chek_update(call=call_input, timestamp=timezone.now(), version=version_input)
            check_user.save()
            return HttpResponse(render(request, 'telnet_server/versions.html', context))
        elif flag == 2:
            return HttpResponse(render(request, 'telnet_server/nonew.html'))
        else:
            return HttpResponse(render(request, "telnet_server/nothing.html"))
    except:
        raise Http404("Oops. We have a problem")
# Create your views here.

def login (request):
    if request.user.is_authenticated:
        return HttpResponse("You are Loged")
    else:

        template_data = Template.objects.filter(page_name="login")

        template_context = {'template': template_data[0]}

        return HttpResponse(render(request, "telnet_server/login.html", template_context))

def enter(request):


        if request.user.is_authenticated:
                template = Template.objects.filter(page_name="admin_page")
                context = {'template': template[0]}
                return HttpResponse(render(request, "telnet_server/admin.html", context))
        else:
            try:
                login_user = request.POST['login']
                password = request.POST['pass']
                user = authenticate(request, username=login_user, password=password)
                if user is not None:
                    login(request)
                    template = Template.objects.filter(page_name="admin_page")
                    context = {'template': template[0]}
                    return HttpResponse(render(request, "telnet_server/admin.html", context))
                else:

                    return HttpResponse("No")
            except Exception:
                #template_data = Template.objects.filter(page_name="login")
                #template_context = {'template': template_data[0]}
                #return HttpResponse(render(request, "telnet_server/login.html", template_context))
                #return HttpResponse("No Ples")
                return HttpResponseRedirect("login")

            #if request.user.is_authenticated:




def logout_view(request):
    logout(request)
    template = Template.objects.filter(page_name="admin_page")
    context = {'template': template[0]}
    return HttpResponse(render(request, "telnet_server/login.html", context))




