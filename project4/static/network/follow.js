document.addEventListener('DOMContentLoaded', function(){
    follow_btn = document.querySelector("#follow-bttn");
    follow_btn.addEventListener(
        'click', function() {
            id = follow_btn.getAttribute("data-profile");
            follow_act(id);
        }
    );
})

function follow_act(profile_user){
    fetch( `/follow?profile_user=${profile_user}`)
        .then(response => response.json())
        .then(data => {
            document.querySelector("#followers_num").innerHTML = data.follower_num;
            follow_btn.innerHTML = data.text;
        })
};
