$(document).ready(function () {
    $('#menu-bars').click(function () {
        $("#collapse").toggle("blind", 1000);
    })

    $('#repeated-upvote-btn').click(function () {
        $('.upvote-btn-hidden').show('fade', 500)
    })
    $('#upvote-no').click(function () {
        $('.upvote-btn-hidden').hide('fade', 500)
    })


    $('#arrow-down').click(function () {
        $('html, body').animate({
            scrollTop: $("#charts").offset().top
        }, 2000)
    })

    $(document).scroll(function () {
        var y = $(this).scrollTop();
        if (y > 0) {
            $('#arrow-down').hide('fade', 1000);
        } else {
            $('#arrow-down').fadeIn();
        }
    });

    $(document).scroll(function () {
        var y = $(this).scrollTop();
        if (y > 250) {

            $('.fade1').show('fade', 700);
            setTimeout(function () {

                // your stuff here
                $('.fade2').show('fade', 700);

            }, 500);
            setTimeout(function () {

                // your stuff here
                $('.fade3').show('fade', 700);

            }, 1000);
            setTimeout(function () {

                // your stuff here
                $('.fade4').show('fade', 700);

            }, 1500);
            setTimeout(function () {

                // your stuff here
                $('.fade5').show('fade', 700);

            }, 2000);
            setTimeout(function () {

                // your stuff here
                $('.fade6').show('fade', 700);

            }, 2500);
            setTimeout(function () {

                // your stuff here
                $('.fade7').show('fade', 700);

            }, 3000);

        }
    });

    $(".bug-btn").click(function () {
        $(".bug-chart-container").hide()
        $(".bug-btn").removeClass('btn-selected')
        $(this).addClass('btn-selected')
        $(this).next().next().next().next().show('fade', 200)
    })

    $(".feature-btn").click(function () {
        $(".features-chart-container").hide()
        $(".feature-btn").removeClass('btn-selected')
        $(this).addClass('btn-selected')
        $(this).next().next().next().next().show('fade', 200)
    })

    setTimeout(function () {
        $('.message-success').hide('fade', 1000);

    }, 3000);

})