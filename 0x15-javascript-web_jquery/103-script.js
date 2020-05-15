
$(document).ready(() => {
  $('INPUT#language_code').keypress((e) => {
    if (e.originalEvent.charCode === 13) $('INPUT#btn_translate').click();
  });

  $('INPUT#btn_translate').on('click', () => {
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/',
      data: { lang: $('INPUT#language_code').val() },
      success: (translate) => $('DIV#hello').text(translate.hello)
    });
  });
});
