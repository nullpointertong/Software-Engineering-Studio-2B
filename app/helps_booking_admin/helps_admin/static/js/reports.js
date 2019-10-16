
$(document).ready(function(){
    $('#startdatetime').datetimepicker({
            format:'YYYY-MM-DD HH:MM:ss',
            icons: {
    			time: 'far fa-clock',
    			date: 'far fa-calendar',
    			up: 'fas fa-arrow-up',
    			down: 'fas fa-arrow-down',
    			previous: 'fas fa-chevron-left',
    			next: 'fas fa-chevron-right',
    			today: 'far fa-calendar-check-o',
    			clear: 'far fa-trash',
    			close: 'far fa-times'
    		},
    		allowInputToggle: true,
        });
        $('#enddatetime').datetimepicker({
            format:'YYYY-MM-DD HH:MM:ss',
            icons: {
    			time: 'far fa-clock',
    			date: 'far fa-calendar',
    			up: 'fas fa-arrow-up',
    			down: 'fas fa-arrow-down',
    			previous: 'fas fa-chevron-left',
    			next: 'fas fa-chevron-right',
    			today: 'far fa-calendar-check-o',
    			clear: 'far fa-trash',
    			close: 'far fa-times'
    		},
    		allowInputToggle: true,
        });
        $("#search_btn").on("click", function() {
            var start_time = $("#startdatetime").val();
            var end_time = $("#enddatetime").val();

            $.ajax({
                type: "POST",
                url: "/search_reports/",
                method: "POST",
                data: { start_time: start_time, end_time: end_time, csrfmiddlewaretoken: $("#csrf-token").val() },
                beforeSend: function () {
                    console.log("Before Send");
                },
                success: function (response) {
                    $("#reports").html(response);
                    $("#created-on").html("<span class='alert alert-primary'>Created on: "  + start_time + " ~ " + end_time + "</span>" );
                },
                error: function () {
                    alert("Error! Please try again")
                }
            });
        });

});
