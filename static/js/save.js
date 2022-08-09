
const Save = (ev)=>{
    ev.preventDefault();
        var cv_data = [];

        // Get each row data
        var Rows = document.getElementsByTagName('tr');
        for (var i = 0; i < rows.length; i++) {

            // Get each column data
            var Cols = rows[i].querySelectorAll('td,th');

            // Stores each csv row data
            var csvrow = [];
            for (var j = 0; j < cols.length; j++) {

                // Get the text data of each cell
                // of a row and push it to csvrow
                csvrow.push(Cols[j].innerHTML);
            }

            // Combine each column value with comma
            cv_data.push(csvrow.join(","));
        }

        // Combine each row data with new line character
        cv_data = cv_data.join('\n');

        // Call this function to download csv file
        downloadCSVFile(cv_data);

    }

    function downloadCSVFile(csv_data) {

        // Create CSV file object and feed
        // our csv_data into it
        CSVFile = new Blob([csv_data], {
            type: "text/csv"
        });

        // Create to temporary link to initiate
        // download process
        var temp_link = document.createElement('a');

        // Download csv file
        temp_link.download = "Houses.csv";
        var url = window.URL.createObjectURL(CSVFile);
        temp_link.href = url;

        // This link should not be displayed
        temp_link.style.display = "none";
        document.body.appendChild(temp_link);

        // Automatically click the link to
        // trigger download
        temp_link.click();
        document.body.removeChild(temp_link);
    }
}


document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('btn3').addEventListener('click', Save);
});