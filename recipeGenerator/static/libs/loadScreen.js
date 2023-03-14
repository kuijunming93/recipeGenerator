// SHOW LOAD CANVAS WHEN CLICKED
function showLoader(){
    document.querySelector(".insertLoader").innerHTML = `
        <div class="loader" style="background-color:#FFE5B4;">
          <div>
            <img src="/static/assets/loadscreen.gif" class="img-fluid">
            <h3 class="loader-text mt-3" style="color:black">Generating your recipe, please wait..
            <div class="spinner-grow text-warning" role="status"></div></h3>
          </div>
        </div>`;

  }

let loader = document.getElementsByClassName('insertLoader-btn');
if (loader !== null){
    for (i=0; i < loader.length; i++){
        loader[i].addEventListener('click', function(){
            showLoader();
        })
    }
}
