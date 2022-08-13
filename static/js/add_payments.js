 const addPayment = (ev)=>{
    ev.preventDefault();
     let payment_info = {
        paymentID: document.getElementById('paymentid').value,
        payment: document.getElementById('monpayment').value,
        tenantID: document.getElementById('tenantid').value,
        loanamount: document.getElementById('loanamount').value,
    }
    s = JSON.stringify(payment_info);
    document.forms[0].reset();

    $.ajax({
        url:"/add_payments",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});

}

document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('btn').addEventListener('click', addPayment);
});