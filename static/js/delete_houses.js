var index, table = document.getElementById('Mytable');
for (var i=1; i<table.rows.length; i++)
{
    table.rows[i].cells[4].onclick = function()
    {
        rowIndex = this.parentElement.rowIndex;
        rowIdValue = {address: table.rows[rowIndex].cells[0].innerText}
        s = JSON.stringify(rowIdValue);
        table.deleteRow(rowIndex);

        $.ajax({
            url:"/delete_rental_property",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s)});

    };

}