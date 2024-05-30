//fetches from https:///foruthfish.com.hellosalut
//displayes hello from that fecth
const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  console.log(data.hello);
  $('#hello').html(data.hello);
});
