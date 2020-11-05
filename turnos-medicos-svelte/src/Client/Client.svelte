<script>
    import moment  from 'moment';
    import 'moment/locale/es';

    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            /*dateClick: function(info) {
                window.$("#exampleModal").modal();
                console.log(info);

                calendar.addEvent({
                    title: "Evento 1",
                    date: info.dateStr
                });
            },*/

            eventClick: function(info) {
                console.log(info.event.title);
                console.log(info.event.start);
                console.log(info.event.extendedProps.description); 

                moment.locale('es');

                console.log(moment.locale('es'));

                var dia = moment(info.event.start).format('LL');
                var hora = moment(info.event.start).format('LT');

                window.$("#exampleModalLabel").text(info.event.title);

                window.$(".modal-title").css("color: 'red' !important;");

                var plantilla = "<p><strong>Fecha:</strong> " + dia + " a las " + hora + "  </p>"
                plantilla += "<p><strong>Profesional:</strong> " + info.event.extendedProps.professional + " </p>"
                plantilla += "<p><strong>Descripción:</strong> " + info.event.extendedProps.description + " </p>"

                window.$("#eventDescription").html(plantilla);
                
                window.$("#exampleModal").modal();
            },

            events: [
                {
                    title: "Odontología",               //Titulo: especialidad.
                    start: "2020-11-05 15:45:00",
                    professional: "Dr. Butros Asis",     //
                    description: "Esta es una descripción.", //Extended props
                },
                {
                    title: "Consulta con Dios",
                    start: "2020-11-06 15:45:00",
                    professional: "Dr House",
                },
                {
                    title: "Evento 3",
                    start: "2020-11-06 20:45:00",
                },
            ]
        });

        calendar.setOption('locale', 'Es');

        calendar.render();
    });

    function funcioncita() {
        alert("Todo");
    }
    


</script>

<h1>Mis turnos</h1>




<div id='calendar'></div>

<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">""</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="centrado">
        <div class="modal-body" id="eventDescription">
            
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" on:click={funcioncita}>Cancelar</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
        
      </div>
    </div>
  </div>
</div>


<style>
    #calendar {
        max-width: 50%;
        margin: 0 auto;
    }

    .modal-title {
        font-weight: 600;
    }

    .centrado {
        text-align: left !important;
    }
</style>