//PRESETTING BY USER ACTION
$('a.initGeneration').click(function () {
    $('#imgGenModal.modal').attr('style','z-index=1');
})

$('.option-item').click(function () {
    document.cookie = "selectedOption=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    console.log(this.getAttribute('data-src'))
    document.cookie = "selectedOption=" + this.getAttribute('data-src') + "; path=/";
    console.log(document.cookie)
})