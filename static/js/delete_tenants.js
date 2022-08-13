var index, table = document.getElementById('Mytable');
for (var i=1; i<table.rows.length; i++)
{
    table.rows[i].cells[6].onclick = function()
    {
        rowIndex = this.parentElement.rowIndex;
        rowIdValue = {tenantid: table.rows[rowIndex].cells[0].innerText}
        s = JSON.stringify(rowIdValue);
        table.deleteRow(rowIndex);

        $.ajax({
            url:"/delete_tenant_info",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s)});

    };

}