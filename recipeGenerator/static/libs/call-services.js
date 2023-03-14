ACTION_ENDPOINT = '/app/recipe/'

//CRSF TOKEN SETUP
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

//PRESETTING BY USER ACTION
$('.option-item').click(function () {
    localStorage.setItem("selectedOption", this.getAttribute('data-src'));
})

$('a.initGeneration').click(function () {
    localStorage.setItem("genMode", this.getAttribute('data-src'));

    let params =  localStorage.getItem("genMode") + "/" + localStorage.getItem("selectedOption");
    console.log(ACTION_ENDPOINT + params);
    fetch(ACTION_ENDPOINT + params, {
        method: 'GET',
        headers:{
            'X-CSRFToken': csrftoken
        }
    })
    .then((response) => {
        console.log(response.url)
        return location.replace(response.url);
    })
})