
function like(element){
    postId = element.getAttribute("post-id");
    isLiked = element.getAttribute("is-liked");
    icon = document.querySelector(`#post-like-${postId}`);
    numLike = document.querySelector(`#post-numLike-${postId}`);

    form = new FormData();
    form.append("postId", postId);
    form.append("isLiked", isLiked);
    fetch(`/like?postId=${postId}`, {
        method: "POST",
        body: form,
    })
    .then((response) => {})

    if(isLiked == "True"){
        icon.src="https://img.icons8.com/carbon-copy/100/000000/like--v2.png"
        element.setAttribute("is-liked", "False");
        numLike.textContent = parseInt(numLike.textContent) - 1;
    }
    else{
        icon.src="https://img.icons8.com/plasticine/100/000000/like.png"
        element.setAttribute("is-liked", "True");
        numLike.textContent = parseInt(numLike.textContent) + 1;
    }
}
