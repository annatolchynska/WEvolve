// Code from jQuery Timepicker that shows time in the form
$(document).ready(function () {
    $('#id_time_for_visit').timepicker({
        timeFormat: 'HH:mm',
        interval: 30,
        minTime: '9',
        maxTime: '19:00',
        defaultTime: '13',
        startTime: '9:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});

// Making the alerts dissapear after 3 seconds
setTimeout(fade_out, 3000);

function fade_out() {
    $('.alert').fadeOut().empty();
}
