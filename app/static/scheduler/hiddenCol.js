function editmode(){
    var row, new_row, send_server, edit_button,i;
    row = document.querySelectorAll('.content');
    new_row = document.getElementById("EditorAdd");
    send_server = document.getElementById("sendServer");
    edit_button = document.getElementById("editButton");
    deletion_row= document.querySelectorAll(".delete_row");
    delete_col = document.getElementById('delete_column');

    if(row[0].contentEditable == 'false'){
        delete_col.style.background = 'white';
        for(var x = 0; x < deletion_row.length; x ++){
            deletion_row[x].style.display ='block';
        }
    }
    else{
        for(var x = 0; x < deletion_row.length; x ++){
            deletion_row[x].style.display ='none';
        }
    }

    for (i = 0; i < row.length; i ++){
        if(row[i].contentEditable == 'false'){
            row[i].contentEditable = 'true';
            new_row.style.display = 'block';
            send_server.style.display = 'block';
            edit_button.innerHTML = 'Cancel';
        }
        else{
            row[i].contentEditable = 'false';
            new_row.style.display = 'none';
            send_server.style.display = 'none';
            edit_button.innerHTML = 'Edit';
        }
    }

} 