function displayCommentsForGetMethods(data) {
    commentsContainer = document.getElementById("post-comments-container");
    for (let i = 0; i < data.length; i++) {
        let divCommentItem = document.createElement("div");
        divCommentItem.classList.add("comment-item", "row", "mb-3");

        let divProfileImage = document.createElement("div");
        divProfileImage.classList.add("user-profile-image", "col-1", "d-flex", "align-items-center", "justify-content-center");
        let itag = document.createElement("i");
        itag.classList.add("bi", "bi-person");
        divProfileImage.appendChild(itag);
        divCommentItem.appendChild(divProfileImage);

        let usernameCommentWrapper = document.createElement("div")
        usernameCommentWrapper.classList.add("col-11", "row")

        let divUsername = document.createElement("div");
        divUsername.classList.add("username", "col-12")
        let btag = document.createElement("b");
        btag.innerText = data[i].fields.commented_by;
        divUsername.appendChild(btag);
        usernameCommentWrapper.appendChild(divUsername);

        let divComment = document.createElement("div");
        divComment.classList.add("comment-body", "col-12");
        divComment.innerText = data[i].fields.body;
        usernameCommentWrapper.appendChild(divComment);

        divCommentItem.appendChild(usernameCommentWrapper);
        commentsContainer.appendChild(divCommentItem);
    }
}

function displayCommentsForPostMethod(data) {
        commentsContainer = document.getElementById("post-comments-container");
        let divCommentItem = document.createElement("div");
        divCommentItem.classList.add("comment-item", "row", "mb-3");

        let divProfileImage = document.createElement("div");
        divProfileImage.classList.add("user-profile-image", "col-1", "d-flex", "align-items-center", "justify-content-center");
        let itag = document.createElement("i");
        itag.classList.add("bi", "bi-person");
        divProfileImage.appendChild(itag);
        divCommentItem.appendChild(divProfileImage);

        let usernameCommentWrapper = document.createElement("div")
        usernameCommentWrapper.classList.add("col-11", "row")

        let divUsername = document.createElement("div");
        divUsername.classList.add("username", "col-12")
        let btag = document.createElement("b");
        btag.innerText = data.commented_by;
        divUsername.appendChild(btag);
        usernameCommentWrapper.appendChild(divUsername);

        let divComment = document.createElement("div");
        divComment.classList.add("comment-body", "col-12");
        divComment.innerText = data.body;
        usernameCommentWrapper.appendChild(divComment);

        divCommentItem.appendChild(usernameCommentWrapper);
        commentsContainer.appendChild(divCommentItem);
}

var startIndex = 0;
async function getComments() {
    const getCommentsURL ='/comments/get-comments/' + postID + '/' + startIndex;
    startIndex = startIndex + 4;
    const params = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
        credentials: 'same-origin',
    }
    const response = await fetch(getCommentsURL, params);
    const data = await response.json();
    if (data.length != 0){
        displayCommentsForGetMethods(data);
    }
    else{
        loadCommentsbtn.style.display = "None"
        document.querySelector(".comments-container").appendChild(document.createTextNode("No Other Comments Found"));
    }
}

getComments();
loadCommentsbtn = document.getElementById("load-comments");
loadCommentsbtn.addEventListener("click", getComments);

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let form = document.getElementById("new-comment");
let formSubmitBtn = document.getElementById("form-submit-btn");

async function postComment() {
    const formData = new FormData(form);
    const plainFormData = Object.fromEntries((formData.entries()));
    const formDataJSONString = JSON.stringify(plainFormData);
    const csrftoken = getCookie('csrftoken');
    const postCommentURL = '/comments/post-comment/'

    const params = {
        method: 'POST',
        mode: 'same-origin',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formDataJSONString,
    }
    try{
        const new_request = await fetch(postCommentURL, params);
        const response = await new_request.json();
        if (response.status == "success"){
            let commentObject = JSON.parse(formDataJSONString);
            commentObject.commented_by = username;
            displayCommentsForPostMethod(commentObject);
        }
    }
    catch(error){
        console.log(error);
    }
}
formSubmitBtn.addEventListener("click", postComment);