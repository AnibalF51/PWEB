function message_error(obj) {
    var html = '';
    if (typeof(obj) === 'object') {
        html = '<ul style="text-align: left;" >';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ':' + value + '</li>';
        });
        html += '</ul>'
    } else {
        html = '<p>' + obj + '</p>';
    }

    Swal.fire({
        title: 'ERROR',
        html: html,
        icon: 'error'
    });
}