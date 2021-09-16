let searchInput = document.getElementById("searchField");
let logo = document.querySelector(".logo");
let searchBar = document.querySelector(".search-bar");
let pageHeader = document.querySelector(".page-header");

searchInput.addEventListener("focus", function (){
    logo.style.display = "none";
    searchBar.style.marginTop = "0%";
    pageHeader.style.marginTop = "40px";
    logo.style.marginBottom = "0px";
})

searchInput.addEventListener("focusout", function (){
    logo.style.display = "block";
    searchBar.style.marginTop = "25%";
    pageHeader.style.marginTop = "50px";
    logo.style.marginBottom = "100px";
})