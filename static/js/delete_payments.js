var index, table = document.getElementById('PaymentsTable');
for (var i=1; i<table.rows.length; i++)
{
    table.rows[i].cells[4].onclick = function()
    {
        rowIndex = this.parentElement.rowIndex;
        rowIdValue = {paymentID: table.rows[rowIndex].cells[0].innerText}
        s = JSON.stringify(rowIdValue);
        table.deleteRow(rowIndex);

        $.ajax({
            url:"/delete_payment_info",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s)});

    };

}