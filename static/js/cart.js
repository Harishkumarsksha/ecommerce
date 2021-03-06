var updateBtn = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtn.length; i++) {

    updateBtn[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)
        console.log('User', user)

        if (user === 'AnonymousUser') {
            console.log('User is not loggedin ')
        }
        else {
            updateUserOrder(productId, action)
        }
    })

}

function updateUserOrder(productId, action) {
    console.log('User logged in and sending the data ')
    var url = '/update_itme/'
    console.log('csrf token', csrftoken)
    fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data', data)
            location.reload()
        })
}