(function($) {
  "use strict"; // Start of use strict

  // Closes the sidebar menu
  $(".menu-toggle").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
    $(this).toggleClass("active");
  });

  // Smooth scrolling
  $('.js-scroll-trigger').click(function () {
      $('html, body').animate({
          scrollTop: $( $.attr(this, 'href') ).offset().top
      }, 600);
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('#sidebar-wrapper .js-scroll-trigger').click(function() {
    $("#sidebar-wrapper").removeClass("active");
    $(".menu-toggle").removeClass("active");
  });

  //Check validity of form info using regEx
  $('#submit').click(function(e){
    $('p.error').remove();
    let regTest = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);
    let email = regTest.test($("#email").val());
    if(!email){
      $('#email').addClass('error');
      $('#email').after('<p class = "error">Incorrent Email</p>')
    }else $('#email').removeClass('error');

    regTest = new RegExp('([a-z]){2,}');
    let name = regTest.test($("#name").val());
    if(!name){
      $('#name').addClass('error');
      $('#name').after('<p class = "error">Enter a valid name</p>')
    }else $('#name').removeClass('error');

    regTest = new RegExp('([a-z]){1,}');
    let message = regTest.test($("#message").val());
    if(!message){
      $('#message').addClass('error');
      $('#message').after('<p class = "error">Message box can\'t be empty!</p>')
    }else $('#message').removeClass('error');

    if(!(name && message && email))e.preventDefault();
  });

  // Scroll to top button appear
  $('#button').fadeOut();
  $(document).scroll(function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 400) {
      $('#button').fadeIn();
      $('nav').addClass('shaded');
    } else {
      $('#button').fadeOut();
      $('nav').removeClass('shaded');
    }
  });
  $('#button').on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0}, '800');
  });

})(jQuery); // End of use strict
