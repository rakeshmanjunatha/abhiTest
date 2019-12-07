from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Submit, Field, LayoutObject,
    TEMPLATE_PACK, MultiField, Reset
    )
from crispy_forms.bootstrap import (
    AppendedText, PrependedText, FormActions,
    InlineRadios, InlineCheckboxes
    )
from crispy_forms.layout import (
    Layout, Fieldset, MultiField, HTML, Div, Field, Row, Column
)
from crispy_forms.bootstrap import InlineRadios


class FSCCheckListForm(forms.Form):
    SHIFT_TYPES = (
        ('DAY_SHIFT', 'Day Shift'),
        ('Night_SHIFT', 'Night Shift'),
    )
    YesOrNo = (
        (True, 'Yes'),
        (False, 'No'),
    )
    shift = forms.ChoiceField(
        required=True, label='Shift:',
        choices=SHIFT_TYPES)

    current_Odate = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '.datetimepicker-input'
        })
    )

    verify_abends = forms.ChoiceField(required=True, label="Verify Abends match alerts in WLA:", choices=YesOrNo,
                                      widget=forms.RadioSelect())
    verify_no_abend = forms.ChoiceField(required=True, label="Verify jMagic No-abend alerts have been addressed:",
                                        choices=YesOrNo,
                                        widget=forms.RadioSelect())
    wla_valid_notes = forms.ChoiceField(required=True, label="Verify all Abends in WLA have valid notes:",
                                        choices=YesOrNo,
                                        widget=forms.RadioSelect())
    bot_tickets = forms.ChoiceField(required=True, label="Batch One Time tickets are current to end of shift:",
                                    choices=YesOrNo,
                                    widget=forms.RadioSelect())
    all_abends_incident = forms.ChoiceField(required=True, label="Verify that all Abends in jMagic have"
                                            " valid updates in the associated incident:",
                                            choices=YesOrNo,
                                            widget=forms.RadioSelect())
    ucc_override = forms.ChoiceField(required=True, label="Verify any cyclic jobs in UCC7.OVERRIDE:", choices=YesOrNo,
                                     widget=forms.RadioSelect())
    service_req = forms.ChoiceField(required=True, label="Service Request have been handled:", choices=YesOrNo,
                                    widget=forms.RadioSelect())
    group_emails = forms.ChoiceField(required=True, label="Group emails have been addressed:", choices=YesOrNo,
                                     widget=forms.RadioSelect())
    held_jobs = forms.ChoiceField(required=True, label="Held jobs reviewed:", choices=YesOrNo,
                                  widget=forms.RadioSelect())
    fsc_report_reviewed = forms.ChoiceField(required=True, label="FSC Production Report reviewed:", choices=YesOrNo,
                                            widget=forms.RadioSelect())

    notable_inc = forms.CharField(required=False, label='Notable Incidents:',
                                  widget=forms.Textarea(attrs={'cols': 500, 'rows': 5, }))

    qr_changes = forms.CharField(required=False, label='QR Changes:',
                                 widget=forms.Textarea(attrs={'cols': 50, 'rows': 5, }))

    bim = forms.CharField(required=False, label="BIM's to watch closely:",
                          widget=forms.Textarea(attrs={'cols': 50, 'rows': 5, }))

    other_shift_notes = forms.CharField(required=False, label="Other shift notes and special instructions:",
                                        widget=forms.Textarea(attrs={'cols': 50, 'rows': 5, }))

    def __init__(self, *args, **kwargs):
        super(FSCCheckListForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-FSCCheckListForm'
        self.helper.disable_csrf = True
        # self.helper.form_class = 'blueForms'
        # self.helper.html5_required = True

        self.helper.layout = Layout(
            Div(
                Div("shift", css_class="col-md-6", ),
                css_class="row",
            ),
            Div(
                Div("current_Odate", css_class="col-md-6", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("verify_abends"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("verify_no_abend"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("wla_valid_notes"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("bot_tickets"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("all_abends_incident"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("ucc_override"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("service_req"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("group_emails"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("held_jobs"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div(InlineRadios("fsc_report_reviewed"), css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div("notable_inc", css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div("qr_changes", css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div("bim", css_class="col-md-12", ),
                css_class="row",
            ),
            Div(
                Div("other_shift_notes", css_class="col-md-12", ),
                css_class="row",
            ),
        )
