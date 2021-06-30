let pagination_num = 2;
async function getCategories() {
    const domainName = "http://127.0.0.1:8000/"
    const url = domainName + 'category/get-categories/' + pagination_num;
    pagination_num = pagination_num + 1;

    const params = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
        credentials: 'same-origin',
    }
    try {
        const response = await fetch(url, params);
        const data = await response.json();
        let ul = document.querySelector("ul")
        for (let i = 0; i < data.length; i++) {
            let li = document.createElement("li");
            li.classList.add("list-group-item", "d-flex", "justify-content-between", "align-items-start");
            let div = document.createElement("div");
            div.classList.add("ms-2", "me-auto");
            div.innerText = data[i].name;
            li.appendChild(div);
            ul.appendChild(li);
        }
    } catch (error) {
        document.alert("Failed to load");
    }

}
loadMoreButton = document.getElementById("load-more");
loadMoreButton.addEventListener("click", getCategories);