
let ham = document.getElementById("hamburger");
let nav = document.getElementById("nav-bar");
function show_tab(){
    let navclass = nav.classList.toggle("show");
}
const root = document.documentElement;
const currentTransform = getComputedStyle(root).getPropertyValue('--Htransform');
root.style.setProperty('--Htransform', -560);