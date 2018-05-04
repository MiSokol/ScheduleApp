function openComplete() {
  $( "#dialog" ).dialog({
    resizable: false,
    height: "auto",
    width: 400,
    modal: true,
    buttons: {
      "Да": function() {
        $( this ).dialog( "close" );
      },
      "Орда": function() {
        $( this ).dialog( "close" );
      }
    }
  });
}

function openAdd() {
    
}