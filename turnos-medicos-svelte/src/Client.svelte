<script>
    //import * as $j from 'jquery';




    
	document.addEventListener('DOMContentLoaded', function() {
	  var calendarEl = document.getElementById('calendar');
	  var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth'
	  });
	  calendar.render();
    });


    

    window.onload = function() {
        window.$("#Confirm").hide();
    };

    

    //window.$("#Confirm").hide();
    //document.getElementById('Confirm').style.visibility = 'hidden';
/*
    function Holaa(){
        console.log("Holaaaa");
        console.log(window.$("#Fecha").val());
    }*/
    
    function AddEvent(){
        console.log("Holaaaa");
        document.getElementById("Datos").innerHTML = '<input id="Fecha" type="date">';
        window.$("#Confirm").show();
    }

    function SendEvent(){
        //console.log("Hol222222aaaa");
        console.log( window.$("#Fecha").val());
        //document.getElementById("Datos").innerHTML = '<input id="Fecha" type="date">';
        var date = moment(window.$("#Fecha").val());
        console.log(date);

        
                if (date.isValid()) {
                    window.$('#calendar').fullCalendar('renderEvent', {
                    title: 'dynamic event',
                    start: date,
                    allDay: true
                    });
                    alert('Great. Now, update your database...');
                } else {
                    alert('Invalid date.');
                }

        //calendar.addEvent()
    }

    

    


</script>

<button type="button" class="btn btn-success" on:click={AddEvent}>Agregar</button>
<button id="Confirm" type="button" class="btn btn-danger"  on:click={SendEvent}> Confirmar</button>
<div id="Datos">
    
</div>
<div id='calendar'></div>
