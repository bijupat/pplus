
	(function($){
        var ico = $('<i class="fa fa-angle-down sks_custom"></i>');
        $('nav#menu li:has(ul) > a').append(ico);
        
        $('nav#menu li:has(ul)').on('click',function(){
          $(this).toggleClass('open');
        });
        
        $('a#toggle').on('click',function(e){
              $('html').toggleClass('open-menu');
              $('div.header-links').hide();
              $('.menuTitle').removeClass('arrow-up');
              return false;
            });
            
            $('div#overlay').on('click',function(){
              $('html').removeClass('open-menu');
            })  
      })($)
  
  $( document ).ready(function() {
          
          $('.sks_custom').on('click',function(e) {
              $('#menu ul li').not($(this).parent().parent()).find('.sub-menu').stop(true, true).delay(200).fadeOut(500);
              $('#menu ul li a i').not($(this)).removeClass('openedmenu');
              $('#menu ul li a i').not($(this)).addClass('closemenu');
  
              e.preventDefault();
              if($(this).hasClass('openedmenu')) {
             
                  $(this).parent().parent().find('.sub-menu').stop(true, true).delay(200).fadeOut(500);
                  $(this).removeClass('openedmenu');
                  $(this).addClass('closemenu');
  
              } else {
                  
                  $(this).parent().parent().find('.sub-menu').stop(true, true).delay(200).fadeIn(500);
                  $(this).removeClass('closemenu');
                  $(this).addClass('openedmenu');
              }
          });
      });
  
   
  $('a.box-href-link').hover(function(){
              $(this).find('img.icon_img').hide();
              $(this).find('img.icon_hover_img').show();
              },
              function(){
                  $(this).find('img.icon_hover_img').hide();
                  $(this).find('img.icon_img').stop().show();
          });
          
              /*-----FIXED HEADER-----*/
      $(window).scroll(function () {
          if (($(window).scrollTop() > 100) && ($(window).width() >= 320)) {
              $('body').addClass('fixed-header');
          } else {
              $('body').removeClass('fixed-header');
          }
      });
  