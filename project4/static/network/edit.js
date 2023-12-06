
function edit(editbttn){
    postId = editbttn.getAttribute("post-id");
    hideEditDiv(postId);
    hide(editbttn);
    showSaveDiv(postId);
}

function saveHandler(savebttn){
    postId = savebttn.getAttribute("post-id");
    postTextara = document.querySelector(`#post-text-${postId}`);
    newContent = postTextara.value;

    form = new FormData();
    form.append("postId", postId);
    form.append("newContent", newContent);
    fetch("/edit", {
        method: "POST",
        body: form,
    }).then((response) => {
            hideSaveDiv(postId);
            postContent = document.querySelector(`#post-content-${postId}`);
            postContent.innerHTML = newContent;
            show(postContent); 
            showEditDiv(postId);
        })
}

function hideEditDiv(postId){
    postContent = document.querySelector(`#post-content-${postId}`);
    hide(postContent); 
}
function hideSaveDiv(postId){
    postTextara = document.querySelector(`#post-text-${postId}`);
    hide(postTextara); 
    postSavebttn = document.querySelector(`#post-save-${postId}`)
    hide(postSavebttn);
}
function showSaveDiv(postId){
    postTextara = document.querySelector(`#post-text-${postId}`);
    postTextara.innerHTML = postContent.innerHTML;
    show(postTextara); 
    postSavebttn = document.querySelector(`#post-save-${postId}`)
    show(postSavebttn);
}
function showEditDiv(postId){
    editbttn = document.querySelector(`#post-edit-${postId}`);
    show(editbttn);
}

function hide(div){
    div.style.display = "none";
}
function show(div){
    div.style.display = "block";
}

