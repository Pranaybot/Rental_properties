const addTenantInfo = (ev)=>{
    ev.preventDefault();
     let tenant_info = {
        tenantID: document.getElementById('tenantid').value,
        owner: document.getElementById('owner').value,
        number: document.getElementById('phonenumber').value,
        arrivedate: document.getElementById('moveindate').value,
        departdate: document.getElementById('moveoutdate').value,
        address: document.getElementById('propaddress').value
    }
    s = JSON.stringify(tenant_info);
    document.forms[0].reset();

    $.ajax({
        url:"/add_tenants",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});

}

document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('btn').addEventListener('click', addTenantInfo);
});