$(document).ready(function () {

  // fancybox
  $('.fancybox').fancybox();
  $(".input[name='phone']").mask("+7 (999) 999-99-99");
  $('form').each(function(){
    $(this).validate({
      rules: {
        name: {
          required: true,
          minlength: 3
        },
        phone: {
          required: true,
          minlength: 3
        },
        mail: {
          required: true,
          email: true
        }
      }
    });
  });
  $('form').ajaxForm({
      success: function(data){
        if (data.success) {
            location.replace("/thnx/");
        }
        $('form').trigger('reset');
      }
  });
  // slider
  $('.review-slider .owl-carousel').owlCarousel({
    loop: true,
    items: 1,
    nav: true,
    dots: false,
    //autoHeight : true,
    navText: [''],
    autoplay: true
  });

  // price select
  $(document).on('click','.price-img img',function(){
    $('.price-img img').removeClass('active');
    $(this).addClass('active');
  });

  // header city
  $(document).on('click','.header-city-link',function(e){
    e.preventDefault();
    if($(this).hasClass('active')){
      $(this).removeClass('active');
      $('.mask').removeClass('active');
      $('.city-hidden').slideUp();
    }else{
      $(this).addClass('active');
      $('.mask').addClass('active');
      $('.city-hidden').slideDown();
    }
  });
  $(document).on('click','.city-hidden-close',function(e){
    e.preventDefault();
    $('.header-city-link').removeClass('active');
    $('.mask').removeClass('active');
    $('.city-hidden').slideUp();
  });

  // phone img show
  $(document).on('click','.info-mid-img',function(e){
    e.preventDefault();
    if($(this).hasClass('active')){
      $(this).removeClass('active');
    }else{
      $(this).addClass('active');
    }
  });
  $(document).on('click','.info-mid-show',function(e){
    e.preventDefault();
    if($('.info-mid-img').hasClass('active')){
      $('.info-mid-img').removeClass('active');
    }else{
      $('.info-mid-img').addClass('active');
    }
  });


});


