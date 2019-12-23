import json
import logging
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import FSCBatchTurnOver

from .forms import (
    FSCCheckListForm
)

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html', {})


def view_checklist(request):
    context = {}
    fsc_objs = FSCBatchTurnOver.objects.all().order_by('-id')
    print(fsc_objs)
    context['page_header'] = 'FSC Batch Turnover Checklist'
    context['fsc_objects'] = fsc_objs
    return render(request, 'view_check_list.html', context)


def check_list(request):
    context = {}
    context['checklist_form'] = FSCCheckListForm()
    context['page_header'] = 'FSC Batch Turnover Checklist Entry'
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
        if action == 'mail':
            __send_mail(context)
        fsc_obj.save()

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

    context['shift'] = request.POST.get('shift')
    context['current_Odate'] = request.POST.get('current_Odate')

    return context


def __send_mail(context):
    subject = 'Test: FSC Batch Turnover'
    recipient_list = ['abhijithbharadwaj27@gmail.com', 'rakesh.manjunatha@gmail.com', ]
    email_from = settings.EMAIL_HOST_USER

    description = render_to_string('email_body2.html', context)
    send_mail(subject, description, email_from, recipient_list, html_message=description)

@csrf_exempt
def send_fsc_mail(request):
    batch_id = request.POST.get('batch_id')
    fsc_batch_details = FSCBatchTurnOver.objects.filter(id=batch_id).values()
    if fsc_batch_details:
        __send_mail(fsc_batch_details[0])


