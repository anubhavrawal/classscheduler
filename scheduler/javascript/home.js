$(document).ready(function(){
    // example.php will be used to send the data to the sever database
    $('#example-1').Tabledit({
    url: 'example.php',
    editButton: false,
    deleteButton: false,
    hideIdentifier: true,
    columns: {
    identifier: [0, 'id'],
    editable: [[2, 'first'], [3, 'last'],[3, 'nickname']]
    }
    });
    
    });