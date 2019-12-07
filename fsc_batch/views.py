import json
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import FSCBatchTurnOver

from .forms import (
    FSCCheckListForm
)


def index(request):
    return render(request, 'index.html', {})


def view_checklist(request):
    fsc_objs = FSCBatchTurnOver.objects.all().order_by('-id')
    for obj in fsc_objs:
        print('******************object=', obj.shift)
        print('******************object=', obj.verify_abends)
        print('******************object=', obj.qr_changes)
    return render(request, 'view_check_list.html', {'fsc_objects': fsc_objs})


def check_list(request):
    context = {}
    context['checklist_form'] = FSCCheckListForm()
    return render(request, 'check_list.html', context)


@csrf_exempt
def create_fsc_batch(request):
    if request.method == 'POST':
        response_data = {}
        shift = request.POST.get('shift')
        current_Odate = request.POST.get('current_Odate')
        action = request.POST.get('action')

        context = create_context_data(request)
        fsc_obj = FSCBatchTurnOver.update_or_create_object(shift, current_Odate, context)
        fsc_obj.save()
        if action == 'mail':
            send_checklist('Subject Rakesh', 'body message')

        response_data['result'] = 'Create post successful!'
        response_data['id'] = fsc_obj.id

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def create_context_data(request):
    context = {}
    context['verify_abends'] = request.POST.get('verify_abends')
    context['verify_no_abend'] = request.POST.get('verify_no_abend')
    context['wla_valid_notes'] = request.POST.get('wla_valid_notes')
    context['bot_tickets'] = request.POST.get('bot_tickets')
    context['all_abends_incident'] = request.POST.get('all_abends_incident')
    context['ucc_override'] = request.POST.get('ucc_override')
    context['service_req'] = request.POST.get('service_req')
    context['group_emails'] = request.POST.get('group_emails')
    context['held_jobs'] = request.POST.get('held_jobs')
    context['fsc_report_reviewed'] = request.POST.get('fsc_report_reviewed')
    context['notable_inc'] = request.POST.get('notable_inc')
    context['qr_changes'] = request.POST.get('qr_changes')
    context['bim'] = request.POST.get('bim')
    context['other_shift_notes'] = request.POST.get('other_shift_notes')

    return context

from django.core.mail import send_mail
from django.conf import settings


def send_checklist(subject, msg):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['rakesh.manjunatha@gmail.com', ]
    send_mail(subject, msg, email_from, recipient_list)
