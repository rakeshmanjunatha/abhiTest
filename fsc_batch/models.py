from django.db import models


class FSCBatchTurnOver(models.Model):
    SHIFT_TYPES = (
        ('DAY_SHIFT', 'Day Shift'),
        ('Night_SHIFT', 'Night Shift'),
    )

    shift = models.CharField(max_length=30, choices=SHIFT_TYPES,
                             verbose_name=('Shift'), blank=False, null=False)
    current_Odate = models.DateTimeField("Current ODate", blank=False, null=False)

    verify_abends = models.BooleanField(default=False)
    verify_no_abend = models.BooleanField(default=False)
    wla_valid_notes = models.BooleanField(default=False)
    bot_tickets = models.BooleanField(default=False)
    all_abends_incident = models.BooleanField(default=False)
    ucc_override = models.BooleanField(default=False)
    service_req = models.BooleanField(default=False)
    group_emails = models.BooleanField(default=False)
    held_jobs = models.BooleanField(default=False)
    fsc_report_reviewed = models.BooleanField(default=False)

    notable_inc = models.CharField("Notable Incidents", max_length=1000, blank=True,
                            null=True)
    qr_changes = models.CharField("QR Changes", max_length=1000, blank=True,
                            null=True)
    bim = models.CharField("BIM", max_length=1000, blank=True,
                            null=True)
    other_shift_notes = models.CharField("Other Shift Notes", max_length=1000, blank=True,
                            null=True)

    # def __str__(self):
    #     return self.id

    @staticmethod
    def update_or_create_object(shift, current_Odate, context):
        obj = None

        obj, created = FSCBatchTurnOver.objects.update_or_create(
            shift=shift, current_Odate=current_Odate, defaults=context)
        return obj


