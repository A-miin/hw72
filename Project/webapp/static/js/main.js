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
                    `<h3>Text:</h3>${obj['text']}<br>
                        <h3>Date:</h3>${obj['created_at']}<br>
                        <a href="#">View</a><br>
                        <h3>Rate:</h3>${obj['rate']}<br>
                        <button>+</button>
                        <button>-</button>`
            }
            if (data.error){
                result.innerText=data['error']
                result.className=('text-danger')
            }

        })
    main_content.append(result)
}
console.log('hello')
list()