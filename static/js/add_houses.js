const addProperty = (ev)=>{
    ev.preventDefault();
     let property = {
        address: document.getElementById('propaddress').value,
        value: document.getElementById('propvalue').value,
        condition: document.getElementById('condition').value,
        type: document.getElementById('type').value
    }
    s = JSON.stringify(property);
    document.forms[0].reset();

    $.ajax({
        url:"/add_houses",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});

}
document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('btn').addEventListener('click', addProperty);
});