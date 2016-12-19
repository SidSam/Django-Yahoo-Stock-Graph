$(document).ready(function() {
  
  var $demo = $(".card-menu");
  var numOfSections = $(".card-menu__section").length;
  
  $(document).on("click", ".card-menu__menu-btn", function() {
    $demo.addClass("menu-active");
  });
  
  $(document).on("click", ".card-menu__close-menu", function() {
    $demo.removeClass("menu-active");
  });
  
  $(document).on("click", ".card-menu.menu-active .card-menu__section", function() {
    var $section = $(this);
    var index = +$section.data("section");
    
    $(".card-menu__section.active").removeClass("active");
    $(".card-menu__section.inactive").removeClass("inactive");
    $section.addClass("active");
    $demo.removeClass("menu-active");
    
    for (var i = index + 1; i <= numOfSections; i++) {
      $(".card-menu__section[data-section="+ i +"]").addClass("inactive");
    }
  });
  
});