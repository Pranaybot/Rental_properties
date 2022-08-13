index, table = document.getElementById("Mytable");

  for(var i=1; i<table.rows.length;i++)
  {
    table.rows[i].cells[7].onclick = function()
    {
        index = this.parentElement.rowIndex;
        document.querySelector(".editTable").style.display="block";

    };

  }

  function editRow() {
    table.rows[index].cells[1].innerHTML = document.getElementById("owner").value;
    table.rows[index].cells[2].innerHTML = document.getElementById("phonenumber").value;
    table.rows[index].cells[3].innerHTML = document.getElementById("moveindate").value;
    table.rows[index].cells[4].innerHTML = document.getElementById("moveoutdate").value;
    table.rows[index].cells[5].innerHTML = document.getElementById("propaddress").value;

    document.querySelector(".editTable").style.display="none";

    let tenant_info = {
        ID: table.rows[index].cells[0].innerText,
        owner: table.rows[index].cells[1].innerText,
        number: table.rows[index].cells[2].innerText,
        arrivaldate: table.rows[index].cells[3].innerText,
        departuredate: table.rows[index].cells[4].innerText,
        address: table.rows[index].cells[5].innerText,
    }

    s = JSON.stringify(house_info);
    document.forms[0].reset();

    window.alert(s)
    $.ajax({
        url:"/update_tenants",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
  };