$(document).ready(function() {             
    var $this = $(this);
    function serviceboxheight() {
    var max = 0;
    $('.service-slider .service-box.sameheight', $this).each(function () {
        $(this).height('');
        var h = $(this).height();
        max = Math.max(max, h);
      }).height(max);
    }
    //setHeight();
    $(window).on('load resize orientationchange', serviceboxheight);       
  });
  $(document).ready(function() {             
    var $this = $(this);
    function serviceboxheight() {
    var max = 0;
    $('.package-1.sameheight', $this).each(function () {
        $(this).height('');
        var h = $(this).height();
        max = Math.max(max, h);
      }).height(max);
    }
    //setHeight();
    $(window).on('load resize orientationchange', serviceboxheight);       
  });
  
  $(document).ready(function() {             
    var $this = $(this);
    function serviceboxheight() {
    var max = 0;
    $('.equipment-box .equipment-bx-btm.sameheight', $this).each(function () {
        $(this).height('');
        var h = $(this).height();
        max = Math.max(max, h);
      }).height(max);
    }
    //setHeight();
    $(window).on('load resize orientationchange', serviceboxheight);       
  });
  
  $(document).ready(function(){
    $('.testimonial-slider').slick({
      dots:true,
      autoplay:true,
      infinite:true,
      speed:5000
    });
  });
  $(document).ready(function(){
    $('.banner-slide').slick({
      dots:false,
      autoplay:true,
      infinite:true,
      speed:3000
    });
  });
  
  $(document).ready(function(){
    $('.package-slider').slick({
      dots:false,
      infinite:true,
      fade:true,
      autoplay:true,
      speed:1000,
      autoplay:true,
      cssEase: 'linear'
    });
  });
  
  $(document).ready(function(){
    $('.service-slider').slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      autoplay: true,
      infinite:true,
      autoplaySpeed: 2000,
      responsive: [
      {
        breakpoint: 1520,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint:520,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  
    });
  });
  
    $(document).ready(function(){
        $('.aboutus-tp-wr ul li').mouseenter(function(){
          $(this).find('.range-wr').children('.default-img').hide();
          $(this).find('.range-wr').children('.hover-img').show();
  
        });
        $('.aboutus-tp-wr ul li').mouseleave(function(){
          $(this).find('.range-wr').children('.hover-img').hide();
          $(this).find('.range-wr').children('.default-img').show();
        });
    });
    $(document).ready(function(){
        $('.service-box').mouseenter(function(){
          $(this).find('.service-bx-lf').children('.default-img').hide();
          $(this).find('.service-bx-lf').children('.hover-img').show();
  
        });
        $('.service-box').mouseleave(function(){
          $(this).find('.service-bx-lf').children('.hover-img').hide();
          $(this).find('.service-bx-lf').children('.default-img').show();
        });
    });
  
    $(document).ready(function() {             
    var $this = $(this);
    function serviceboxheight() {
    var max = 0;
    $('.service-box.sameheight', $this).each(function () {
        $(this).height('');
        var h = $(this).height();
        max = Math.max(max, h);
      }).height(max);
    }
    //setHeight();
    $(window).on('load resize orientationchange', serviceboxheight);       
  });
  
      $(window).load( function() {
  
      $('#container').masonry({
          "itemSelector": ".item",
          "columnWidth": ".grid-sizer",
      });
  
  });
    $(document).ready(function() {
             setTimeout(function() {
                 $('body').addClass('loaded');
          }, 500);
       });
  
  $(document).ready(function(){  
  if($(window).width() >= 992){
     $(window).scroll(function() {
              if ($(this).scrollTop() > 200){  
                  $('.sticky-nav').addClass("sticky");
  
              }
              else{
                  $('.sticky-nav').removeClass("sticky");
              }
          });
  }
  });