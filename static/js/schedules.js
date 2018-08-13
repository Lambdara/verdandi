function post_schedule() {
    var date = document.getElementById('date_input').value;
    var name = document.getElementById('name_input').value;

    var data = {};
    if (date != '')
        data['date'] = date;
    if (name != '')
        data['name'] = name;

    $.ajax({
        type: "POST",
        url: '',
        data: JSON.stringify(data),
        success: function() {
            location.reload();
        }
    });
}

function delete_schedule(id) {
    $.ajax({
        type: "DELETE",
        url: id,
        data: '',
        success: function() {
            location.reload();
        }
    });
}
