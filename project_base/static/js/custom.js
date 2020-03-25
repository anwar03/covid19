/**
 * Created by ikhtiar on 7/27/18.
 */

var  Base_url = function() {
    var host = window.location.origin;
    return host
};

$(document).ready(function () {
    // for initializing select2
    $(".select2").select2({
        width: '100%'
    });


    //handles the disabled input fields in the submitted form
    $("form").submit(function () {
        $("form :disabled").removeAttr('disabled');
    });

    // handles date picker
    $(".datepicker").datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true
    });


});

$(".btn-file").on('click', function () {
    var url = $(this).attr('file-url');
    window.open(url, '_blank');
});

