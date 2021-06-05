ACTIONS={
    'index':'',
    'new':'api/quote/'
}
ROOT_URL='http://localhost:8000/'

let create_form = document.getElementById('new_quote_form')
let result = document.createElement("div")
let view_content = document.getElementById('view')
view_content.style.display = 'none'
create_form.style.display='none'
result.style.display='none'

function prvDefaultbtns() {
    let btns = document.getElementsByClassName('action')
    for (let btn of btns) {
        btn.addEventListener("click", function (event) {
            event.preventDefault()
        });
    }
}
window.addEventListener('load', prvDefaultbtns)

function set_token(event){
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
function new_quote() {
    view_content.style.display = 'none'
    result.style.display='none'
    create_form.style.display = 'block';
}
function create_quote(){
    $.ajax({
    url: 'http://localhost:8000/api/quote/',
    method: 'post',
    data: JSON.stringify({
        text: `${document.getElementById('new_quote_text').value}`,
        name: `${document.getElementById('new_quote_name').value}`,
        email: `${document.getElementById('new_quote_email').value}`
        }),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);alert("Цитата удачно создана!"); list();  },
    error: function(response, status){console.log(response);alert("Что-то пошло не так");}
});
}

function quote_view(id){
    $.ajax({
    url: `http://localhost:8000/api/quote/${id}`,
    method: 'get',
    data: JSON.stringify(),
    dataType: 'json',
    contentType: 'application/json',
    success: function one_quote(response){
            create_form.style.display='none'
            result.style.display='none'
            view_content.style.display = 'block'
            view_content.innerHTML =
                            `<h5>Text:</h5>${response['text']}<br>
                                <h5>Name:</h5>${response['name']}<br>
                                <h5>Email:</h5>${response['email']}<br>
                                <h5>Date:</h5>${response['created_at']}<br>
                                <h5>Rate:</h5>${response['rate']}<br>
                                <button>+</button>
                                <button>-</button>
                                    <hr>`

                },
    error: function(response, status){console.log(response);alert("Что-то пошло не так");}
});
}

function list(event) {
    view_content.style.display = 'none'
    create_form.style.display='none'
    result.style.display='block'
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
                        <a href="#" onclick="quote_view(${obj['id']})" >View</a><br>
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
