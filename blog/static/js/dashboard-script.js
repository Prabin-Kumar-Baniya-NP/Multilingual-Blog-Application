pagination_num = 0;
async function getCategories() {
    domainName = "http://127.0.0.1:8000/"
    pagination_num = pagination_num + 1;
    url = domainName + 'category/get-categories/' + pagination_num;
    
    params = {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            credentials: 'same-origin',
        },
    }
    try{
        response = await fetch(url, params);
    data = await response.json();
    ul = document.querySelector("ul")
    for (let i = 0; i < data.length; i++) {
        li = document.createElement("li");
        li.classList.add("list-group-item", "d-flex", "justify-content-between", "align-items-start");
        div = document.createElement("div");
        div.classList.add("ms-2", "me-auto");
        div.innerText = data[i].name;
        li.appendChild(div);
        ul.appendChild(li);
    }
    }
    catch(error){
        document.alert("Failed to load");
    }
    
}

loadMoreButton = document.getElementById("load-more")
loadMoreButton.addEventListener("click", getCategories);