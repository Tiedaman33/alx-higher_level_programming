//adds red to the header element
const $ = window.$;
$('#red_header').bind('click', function () {
  $('header').addClass('red');
});
