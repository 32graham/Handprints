function codeAddress() {
    var data1 = {
        labels : {{ comp_names|safe }},
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                data : {{ comp_counts }}
            },
        ]
    };

    var data2 = {
        labels : {{ tier_names|safe }},
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                data : {{ tier_counts }}
            },
        ]
    };

    //Get the context of the canvas element we want to select
    var c1 = $('#myChart1');
    var ctx1 = document.getElementById("myChart1").getContext("2d");
    new Chart(ctx1).Bar(data1);

    var c2 = $('#myChart2');
    var ctx2 = document.getElementById("myChart2").getContext("2d");
    new Chart(ctx2).Bar(data2);

    //Run function when window resizes
    $(window).resize(respondCanvas);

    function respondCanvas() {
        c1.attr('width', jQuery("#chartholder1").width());
        c1.attr('height', jQuery("#chartholder1").height());
        new Chart(ctx1).Bar(data1);

        c2.attr('width', jQuery("#chartholder2").width());
        c2.attr('height', jQuery("#chartholder2").height());
        new Chart(ctx2).Pie(data2);
    }

    //Initial call
    respondCanvas();
}


window.onload = codeAddress;


