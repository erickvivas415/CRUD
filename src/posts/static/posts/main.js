console.log("test0")

const helloWorldBox = document.getElementById('hello-world')
const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')

// helloWorldBox.innerHTML = 'Hello <b>World</b>'

$.ajax({
    type: 'GET',
    url: '/hello-world/',
    success: function(response) {
        console.log('success', response)
        helloWorldBox.textContent = response.text
    },
    error: function(error) {
        console.log('error', error)
    }
})

$.ajax({
    type: 'GET',
    url: '/data/',
    success: function(response) {
        console.log('response', response)
        //const data = JSON.parse(response.data)
        //console.log(data)
        const data = response.data
        setTimeout(()=>{
            spinnerBox.classList.add('not-visible')
        console.log('data', data)
        data.forEach(el=> {
            postsBox.innerHTML += `
                ${el.title} - <b>${el.body}</b><br>
            `
        });
        },150)
    },
    error: function(error) {
        console.log('error', error)
    }
})