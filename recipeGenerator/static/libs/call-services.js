//PRESETTING BY USER ACTION
$('a.initGeneration').click(function () {
    $('#imgGenModal.modal').modal('hide');
    $('body').removeClass('modal-open');
    $('.modal-backdrop').remove();

    document.querySelector(".insertLoader").innerHTML = `
    <div class="loader" style="background-color:#FFE5B4;">
      <div>
        <img src="/static/assets/loadscreen.gif" class="img-fluid">
        <h3 class="loader-text mt-3" style="color:black">Generating your recipe, please wait..
        <div class="spinner-grow text-warning" role="status"></div></h3>
      </div>
    </div>`;
})

$('.option-item').click(function () {
    document.cookie = "selectedOption=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    console.log(this.getAttribute('data-src'))
    document.cookie = "selectedOption=" + this.getAttribute('data-src') + "; path=/";
    console.log(document.cookie)
})


