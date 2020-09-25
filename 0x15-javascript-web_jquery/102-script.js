
$(document).ready(function () {
    $('#btn_translate').on('click', function (event) {
      const lang_param =  $('#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/?lang='+ lang_param, function (data) {
        $('#hello').html(data.hello);
      });
    });
  });