$('document').ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const param = { lang: $('INPUT#language_code').val() };
  $('INPUT#btn_translate').click(() => {
    $.get(url + $.param(param), (data) => $('DIV#hello').html(data.hello));
  });
});
