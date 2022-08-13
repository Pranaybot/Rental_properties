index, table = document.getElementById("Mytable");

  for(var i=1; i<table.rows.length;i++)
  {
    table.rows[i].cells[5].onclick = function()
    {
        index = this.parentElement.rowIndex;
        document.querySelector(".editTable").style.display="block";

    };

  }

  function editRow() {
    table.rows[index].cells[1].innerHTML = document.getElementById("propvalue").value;
    table.rows[index].cells[2].innerHTML = document.getElementById("condition").value;
    table.rows[index].cells[3].innerHTML = document.getElementById("type").value;

    document.querySelector(".editTable").style.display="none";

    let property = {
        address: table.rows[index].cells[0].innerText,
        value: table.rows[index].cells[1].innerText,
        condition: table.rows[index].cells[2].innerText,
        type: table.rows[index].cells[3].innerText
    }

    s = JSON.stringify(property);
    document.forms[0].reset();

    $.ajax({
        url:"/update_houses",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
  };
