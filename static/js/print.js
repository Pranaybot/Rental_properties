
const Print = (ev)=>{
    ev.preventDefault();
    window.print()
}


document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('btn2').addEventListener('click', Print);
});