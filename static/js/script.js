var name = $("#name_inp").val(),
      time = $("#time_inp").val(),
      deadline = $("#deadline_inp").val();

$(function(){
    $(".task").click(function() {
        completeTask();
    });

    $("#logout_btn").click(function () {
        window.location.replace("logout")
    });

    $("#add_task").click(function () {
        askTask();
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

function askTask() {
  $( "#dialog-add-task" ).dialog({
    resizable: false,
    height: "auto",
    width: 400,
    modal: true,
    buttons: {
      "Да": function() {
        addTask()
        $( this ).dialog( "close" );
      },
      "Орда": function() {
        $( this ).dialog( "close" );
      }
    }
  });
}


function addTask() {

  console.log(name);

  $( "#tasklist" ).append( "<div class='task'>" +
        "<p class='name'>" + name + "</p>" +
        "<p class='time'>" +  time + " минут </p>" +
        "<p class='deadline'> Deadline: " + deadline + "</p>" +
      "</div>" );

  $(function(){
    $(".task").click(function() {
        completeTask();
    });

    $("#logout_btn").click(function () {
        window.location.replace("logout")
    });

    $("#add_task").click(function () {
        askTask();
    });
});
}
