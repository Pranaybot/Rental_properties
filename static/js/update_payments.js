index, table = document.getElementById("PaymentsTable");

for(var i=1; i<table.rows.length;i++)
{
    table.rows[i].cells[5].onclick = function()
    {
        index = this.parentElement.rowIndex;
        document.querySelector(".editPaymentTable").style.display="block";

    };

};

function editPayment() {
    table.rows[index].cells[1].innerHTML = document.getElementById("monpayment").value;
    table.rows[index].cells[2].innerHTML = document.getElementById("tenantid").value;
    table.rows[index].cells[3].innerHTML = document.getElementById("amount").value;

    document.querySelector(".editPaymentTable").style.display="none";

    let payment_info = {
        paymentID: table.rows[index].cells[0].innerText,
        payment: table.rows[index].cells[1].innerText,
        tenantID: table.rows[index].cells[2].innerText,
        loan: table.rows[index].cells[3].innerText
    }

    s = JSON.stringify(payment_info);
    document.forms[0].reset();

    $.ajax({
        url:"/update_payments",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
    };
