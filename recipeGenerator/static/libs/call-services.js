//PRESETTING BY USER ACTION
$(document).ready(function(){
    const forceLoadURL = document.querySelector("img.img-loader").getAttribute('src');
    document.querySelector("img.img-loader").setAttribute('src', forceLoadURL);
    console.log(forceLoadURL);

    $('a.initGeneration').click(function () {
        $('#imgGenModal.modal').modal('hide');
        $('body').removeClass('modal-open');
        $('.modal-backdrop').remove();
        document.querySelector("div.insertLoader").classList.remove('d-none');
    })

    $('.option-item').click(function () {
        document.cookie = "selectedOption=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        console.log(this.getAttribute('data-src'))
        document.cookie = "selectedOption=" + this.getAttribute('data-src') + "; path=/";
        console.log(document.cookie)
    })
})



