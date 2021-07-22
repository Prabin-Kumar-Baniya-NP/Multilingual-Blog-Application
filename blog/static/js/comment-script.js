let pnum = 0;

function displayComments(data) {
    commentsContainer = document.getElementById("post-comments-container");
    for (let i = 0; i < data.length; i++) {
        let divCommentItem = document.createElement("div");
        divCommentItem.classList.add("comment-item", "row", "mt-3", "mb-3");

        let divProfileImage = document.createElement("div");
        divProfileImage.classList.add("user-profile-image", "col-2", "col-md-1", "d-flex", "align-items-center", "justify-content-center");
        let itag = document.createElement("i");
        itag.classList.add("bi", "bi-person");
        divProfileImage.appendChild(itag);
        divCommentItem.appendChild(divProfileImage);

        let divUsername = document.createElement("div");
        divUsername.classList.add("username", "col-10", "d-flex", "align-items-center", "justify-content-start")
        let btag = document.createElement("b");
        btag.innerText = data[i].commented_by;
        divUsername.appendChild(btag);
        divCommentItem.appendChild(divUsername);

        let divComment = document.createElement("div");
        divComment.classList.add("comment", "offset-2", "col-10", "offset-md-1", "col-md-11");
        divComment.innerText = data[i].body;
        divCommentItem.appendChild(divComment);

        let divCommentVotes = document.createElement("div");
        divCommentVotes.classList.add("user-comments-vote", "offset-2", "col-10", "offset-md-1", "col-md-11")

        divCommentItem.appendChild(divCommentVotes);

        commentsContainer.appendChild(divCommentItem);
    }
}

async function getComments() {
    pnum = pnum + 1;
    const getCommentsURL ='/comments/get-comments/' + postID + '/' + pnum;

    const params = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
        credentials: 'same-origin',
    }
    try {
        const response = await fetch(getCommentsURL, params);
        const data = await response.json();
        const commentsData = data.commentsData
        if (Object.keys(commentsData).length === 0){
            loadCommentsbtn.style.display = "None"
            document.querySelector(".comments-container").appendChild(document.createTextNode("No Other Comments Found"));
        }else{
            displayComments(commentsData);
        }
    } catch (error) {
        console.log(error);
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
            const commentArray = [commentObject];
            displayComments(commentArray);
        }
    }
    catch(error){
        console.log("Error");
    }
}
formSubmitBtn.addEventListener("click", postComment);