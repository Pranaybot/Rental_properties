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
    table.rows[index].cells[1].innerHTML = document.getElementById("monpayment").value;
    table.rows[index].cells[2].innerHTML = document.getElementById("tenantid").value;
    table.rows[index].cells[2].innerHTML = document.getElementById("loanamount").value;

    document.querySelector(".editTable").style.display="none";

    let property = {
        paymentID: table.rows[index].cells[0].innerText,
        payment: table.rows[index].cells[1].innerText,
        tenantID: table.rows[index].cells[2].innerText
        loan: table.rows[index].cells[3].innerText
    }

    s = JSON.stringify(property);
    document.forms[0].reset();

    window.alert(s)
    $.ajax({
        url:"/update_payments",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
  };
