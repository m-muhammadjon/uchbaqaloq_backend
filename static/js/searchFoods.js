const searchField = document.querySelector("#searchField");
const foods = document.querySelector("#foods");
const foodsTable = document.querySelector("#searched-foods");
const category = document.querySelector("#category").textContent;

foodsTable.style.display = "block";

searchField.addEventListener('keyup', (e) =>{
    searchValue = e.target.value;
    // console.log(searchValue.trim(), category);
    if (searchValue.trim().length > 0 ){
        foodsTable.style.display = "block";
        foodsTable.innerHTML = "";
        foods.style.display = "none";
        fetch("/search-foods/", {
            body: JSON.stringify({
                searchText: searchValue,
                category: category
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) =>{
            console.log(data);
            foodsTable.innerHTML = "";
            if (data.length == 0){
                foodsTable.innerHTML += `<h4>No results</h4>`
            } else {
                data.forEach(food => {
                    foodsTable.innerHTML += `                    
                    <li><a href="${food.url}">${food.name}</a></li>
                    `
                });
            }
        })

    } else {
        foodsTable.style.display = "none";
        foods.style.display = "block";

    }
})