ACTIONS={
    'index':'',
    'new':'api/quote/'
}
ROOT_URL='http://localhost:8000/'
function prvDefaultbtns() {
    btns = document.getElementsByClassName('action')
    for (btn of btns) {
        btn.addEventListener("click", function (event) {
            event.preventDefault()
        });
    }
}
window.addEventListener('load', prvDefaultbtns)
let result = document.createElement("div")
function set_token(event){
    console.log('values',document.getElementById('id_username').value, document.getElementById('id_password').value)
    $.ajax({
    url: 'http://localhost:8000/api/user/login/',
    method: 'post',
    data: JSON.stringify({username: `${document.getElementById('id_username').value}`, password: `${document.getElementById('id_password').value}`}),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){localStorage.setItem('apiToken', response.token)},
    error: function(response, status){console.log(response);}
});
}
function remove_token(){
    localStorage.removeItem('apiToken');
}
function list(event) {
    let requestURL = `http://localhost:8000/api/quote/`
    main_content = document.getElementById('main-content')


    function sendRequest(method, url) {
        const headers = {
            'Content-Type': "application/json",
        }
        return fetch(url, {
            method: method,
            headers: headers
        }).then(response => {
            return response.json()
        })
    }
    sendRequest('GET', requestURL)
        .then(data => {
            console.log(data)

            result.innerHTML = '';
            for (obj of data) {
                console.log(obj)
                result.innerHTML +=
                    `<h5>Text:</h5>${obj['text']}<br>
                        <h5>Date:</h5>${obj['created_at']}<br>
                        <a href="#">View</a><br>
                        <h5>Rate:</h5>${obj['rate']}<br>
                        <button>+</button>
                        <button>-</button>
                            <hr>`

            }
            if (data.error){
                result.innerText=data['error']
                result.className=('text-danger')
            }

        })
    main_content.append(result)
}
console.log('hello')