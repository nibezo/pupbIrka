
fetch("http://127.0.0.1:8000/")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        let post = document.createElement('div');
        // Add to post variable class .post
        post.classList.add("post")
        post.textContent = data.message;
        console.log(post);
        document.getElementById('main').appendChild(post);
    }
);
