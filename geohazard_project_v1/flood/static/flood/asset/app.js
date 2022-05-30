
// Mobile Sidebar Function
$('#bar').click(function(){

    $('nav').toggleClass('navhideshow')
    $('.fa-arrow-left').toggleClass('fa-arrow-left-show')
    $('.fa-arrow-right').toggleClass('fa-arrow-right-show')

});

$('#dropdown').click(function(){

    $('.uldropdown').toggleClass('hideshowdropdown')
    
})