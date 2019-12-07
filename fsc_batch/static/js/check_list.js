var action = 'save'
$(document).ready(function(){
    $('input[type="radio"]').attr('required', 'required')

//    $('.nav-link').click(function(){
//        var tab = $(this).attr('href')
//        if(tab == '#div_checklist_entry'){
//            $('#div_view_checklist').removeClass('show')
//        }else{
//            $('#div_checklist_entry').removeClass('show')
//        }
//        $(tab).addClass(' show')
//    })

    $('#btn_save_data').click(function(){
        action = 'save'
        $('#form-entry_checklist').submit()
    });

    $('#btn_send_mail').click(function(){
        action = 'mail'
        $('#form-entry_checklist').submit()
    });
    $('#form-entry_checklist').submit(function(event){
        event.preventDefault();
        submit_form()
    });

    function submit_form(){
        jsonObj = {}
        jsonObj['shift'] = $('#id_shift').val()
        jsonObj['current_Odate'] = $('#id_current_Odate').val()
        jsonObj['verify_abends'] = $("input[name='verify_abends']:checked").val()
        jsonObj['verify_no_abend'] = $("input[name='verify_no_abend']:checked").val()
        jsonObj['wla_valid_notes'] = $("input[name='wla_valid_notes']:checked").val()
        jsonObj['bot_tickets'] = $("input[name='bot_tickets']:checked").val()
        jsonObj['all_abends_incident'] = $("input[name='all_abends_incident']:checked").val()
        jsonObj['ucc_override'] = $("input[name='ucc_override']:checked").val()
        jsonObj['service_req'] = $("input[name='service_req']:checked").val()
        jsonObj['group_emails'] = $("input[name='group_emails']:checked").val()
        jsonObj['held_jobs'] = $("input[name='held_jobs']:checked").val()
        jsonObj['fsc_report_reviewed'] = $("input[name='fsc_report_reviewed']:checked").val()
        jsonObj['notable_inc'] = $("#id_notable_inc").val()
        jsonObj['qr_changes'] = $("#id_qr_changes").val()
        jsonObj['bim'] = $("#id_bim").val()
        jsonObj['other_shift_notes'] = $("#id_other_shift_notes").val()
        jsonObj['action'] = action

        $.ajax({
            url : "/create_fsc_batch/",
            type : "POST",
            data : jsonObj,
            success : function(response) {
                console.log(response)
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
});