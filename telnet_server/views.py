from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes

from .models import Chek_update, Register_new, Version, Template, Admins
from django.contrib.auth import authenticate, login, logout

from .serializers import UpdaterSerializer, Check_updateSerializer
from .utils.updater import check_update


def htu(request):
    template_data = Template.objects.filter(page_name="htu")
    template_context = {'template': template_data[0], 'today_year': timezone.now().year}
    return HttpResponse(render(request, "telnet_server/htu.html", template_context))

def index(request):
    template_data = Template.objects.filter(page_name="main")
    template_context = {'template': template_data[0], 'today_year': timezone.now().year}
    return HttpResponse(render(request, "telnet_server/index.html", template_context))


def updater(request, version_input, call_input):
    new_version = check_update(float(version_input))
    if new_version:
        check_user = Chek_update(call=call_input, timestamp=timezone.now(), version=version_input)
        check_user.save()
        context = {'version': new_version}
        return HttpResponse(render(request, 'telnet_server/versions.html', context))
    return HttpResponse(render(request, 'telnet_server/nonew.html'))


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


class UpdaterAPIView(APIView):

    def get(self, request, version_current, callsign):
        # print(request.auth, request.data, request.query_params)
        version_model = Version.objects.filter(version__gt=float(version_current)).order_by("-version").values()
        if version_model:
            # check_user = Chek_update(call=callsign, timestamp=timezone.now(), version=version_current)
            # check_user.save()
            version_model[0]["status"] = True
            return Response(version_model[0])
        return Response({"status": False})


class RegisterUpdateComplete(APIView):
    # permission_classes = [IsAdminUser]
    def post(self, request):
        print(timezone.now().strftime("%Y-%m-%d %H:%M"))
        update_serializer = Check_updateSerializer(data=request.data)
        update_serializer.is_valid(raise_exception=True)
        update_serializer.save()
        return Response({"data": update_serializer.data})

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            print(request.query_params.get('start'), request.query_params.get('end'))
            if request.query_params.get('start') is not None and request.query_params.get('end') is not None:
                delete_data_list = []
                for pk in range(int(request.query_params["start"]), int(request.query_params["end"])):
                    instance_query_set = Chek_update.objects.filter(pk=pk)
                    if instance_query_set:
                        instance = instance_query_set.get()
                        delete = Check_updateSerializer(instance=instance)
                        delete.delete(instance=instance)
                        delete_data_list.append(delete.data)
                return Response({"data": delete_data_list})
            pk = kwargs.get("pk", None)
            if pk:
                try:
                    instance = Chek_update.objects.filter(pk=pk).get()
                    delete = Check_updateSerializer(instance=instance)
                    delete.delete(instance=instance)
                    return Response({"data": delete.data})
                except BaseException:
                    return Response({"error": "Object does not exist"})
            return Response({"error": "Wrong query. No pk"})
        return Response({"error":"Access denied"})


# class UpdaterAPIView(generics.ListAPIView):
#     queryset = Version.objects.all()
#     serializer_class = UpdaterSerializer



