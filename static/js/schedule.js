function post_event(schedule_id) {
    var name = document.getElementById('name_input').value;
    var start_time = document.getElementById('start_time_input').value;
    var end_time = document.getElementById('end_time_input').value;

    var data = {};
    data['schedule_id'] = schedule_id;
    if (name != '')
        data['name'] = name;
    if (start_time != '')
        data['start_time'] = start_time;
    if (end_time != '')
        data['end_time'] = end_time;

    $.ajax({
        type: 'POST',
        url: window.location.origin + '/events/',
        contentType: 'application/json; charset=utf8',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function() {
            location.reload();
        }
    });
}

$(document).ajaxStop(function(){
    window.location.reload();
});
