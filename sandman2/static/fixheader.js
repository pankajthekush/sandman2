$(document).ready(function() {
  $('tbody').scroll(function(e) { 
    $('thead').css("left", -$("tbody").scrollLeft());
    $('thead th:nth-child(1)').css("left", $("tbody").scrollLeft()-5); 
    $('tbody td:nth-child(1)').css("left", $("tbody").scrollLeft()-5); 
  });
});