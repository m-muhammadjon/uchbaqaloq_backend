let searchInput = document.getElementById("searchField");
let logo = document.querySelector(".logo");
let searchBar = document.querySelector(".search-bar");
let pageHeader = document.querySelector(".page-header");

searchInput.addEventListener("focus", function (){
    logo.style.display = "none";
    searchBar.style.top = "-20px";
    pageHeader.style.marginTop = "40px"
})

searchInput.addEventListener("focusout", function (){
    logo.style.display = "block";
    searchBar.style.top = "61px";
    pageHeader.style.marginTop = "80px";
})