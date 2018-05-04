

$(function(){
    $(".task").click(function() {
        completeTask();
    });

    $("#logout_btn").click(function () {
        window.location.replace("logout")
    });

    $("#add_task").click(function () {
        addTask();
    });
});

function completeTask() {
  $( "#dialog-confirm" ).dialog({
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
};

function addTask() {
  $( "#dialog-add-task" ).dialog({
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