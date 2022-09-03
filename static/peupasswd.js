// PEUPASSWD
function peupasswd(event, th) {
    event.preventDefault();
    $form = th
    var formData = new FormData(th);
    $.ajax({
        url: "peupasswd",
        type: "POST",
        data: formData,
        contentType: false,
        processData: false,
        cache: false,
        success: function(message) {
            $("#result").html(message)
        },
        error: function(message) {
            alert(message)
        }
    });
};
