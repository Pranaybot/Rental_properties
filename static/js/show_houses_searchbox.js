const showSearchBox = (ev)=>{
  ev.preventDefault();
  var x = document.getElementById("myInput");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }

}

document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('f1').addEventListener('click', showSearchBox);
});