$('.arrow').click(function(){
	$('.mobile_navbar').toggleClass('mobile_navbar_show')
	$('.fa-chevron-right').toggleClass('fa-chevron-right-show')
	$('.fa-chevron-left').toggleClass('fa-chevron-left-show')
})

$('.dropdown').click(function(){
	$('.dropdown_menu').toggleClass('dropdown_menu_show')
})

$(document).ready(function(){
	
	$('ul.tabs li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})

})
