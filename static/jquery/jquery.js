$(document).ready(function () {
    $('#menu-bars').click(function () {
        $("#collapse").toggle("blind", 1000);
    })

    $('#repeated-upvote-btn').click(function() {
        $('.upvote-btn-hidden').show('fade', 500)
    })
    $('#upvote-no').click(function() {
        $('.upvote-btn-hidden').hide('fade', 500)
    })
})