<script>
    import moment  from 'moment';
    import 'moment/locale/es';
    import { onMount } from 'svelte';
  
    var valorcito = "";

    

    onMount (
        async () => {
            getTurnos(1);
            //loadCalendar();
        }
    )

    async function getTurnos(clientID) {
        const response = await fetch("http://localhost:5000/events/getClientPendingEvents?clientID=" + clientID.toString())

        const turnos = await response.json();

        //myTodo = todo.items
        
        console.log(turnos)

        
        var plantilla = ""

        var eventos = [];
        

        if (turnos.error == 0) {
            for (let index = 0; index < turnos.status.length; index++) {
                eventos[index] = [];
                eventos[index] = {
                    //Profesional, Clinica, Descripcion, Fecha_Turno, Titulo
                    title: turnos.status[index].Titulo,
                    start: turnos.status[index].Fecha_Turno,
                    professional: turnos.status[index].Profesional,
                    clinica: turnos.status[index].Clinica,
                    description: turnos.status[index].Descripcion,
                    turnoID: turnos.status[index].ID
                }

                

                

                
            }
            //console.log(eventos)
        } else {
            /*plantilla = "Hola ";*/
        }
        
        /*window.$("#proximoTurno").html(plantilla);*/

        loadCalendar(eventos);
    }

    async function listarEspecialidades() {
        const response = await fetch("http://localhost:5000/events/getSpecialities")

        const especialidades = await response.json();
        
        window.$("#Especialidades").empty();

        var x = document.getElementById("Especialidades");
        var c = document.createElement("option");
        c.text = "Seleccione una especialidad";
        x.options.add(c);
        c.selected = true;
        c.hidden = true;
        c.value = 0;
        x.options.add(c);
        //console.log(c);
        for (var i = 0; i < especialidades.status.length; i++) {
            c = document.createElement("option");
            c.text = especialidades.status[i].Nombre;
            c.value = especialidades.status[i].ID;
            x.options.add(c);
            //console.log(c);
        }
    }

    async function listarPracticas() {
        //console.log("Este es el valor de especialidad!! " + window.$("#Especialidades").val());
        const response = await fetch("http://localhost:5000/events/getPracticesBySpecialities?specialityID=" + window.$("#Especialidades").val())

        const practicas = await response.json();
        
        window.$("#Practicas").empty();


        var x = document.getElementById("Practicas");
        var c = document.createElement("option");

        if (practicas.error == 0) {
            c.text = "Seleccione una práctica";

            x.options.add(c);
            c.selected = true;
            c.hidden = true;
            c.value = 0;
            x.options.add(c);
            /*console.log(c);
            console.log(practicas);
            console.log(practicas.status.length);*/

            for (var i = 0; i < practicas.status.length; i++) {
                c = document.createElement("option");
                c.text = practicas.status[i].Nombre;
                c.value = practicas.status[i].ID;
                x.options.add(c);
                //console.log(c);
            }
            
            window.$("#Practicas").prop("disabled", false);

        } else {
            c.text = "Esta especialidad aún no tiene prácticas.";
            c.selected = true;
            c.hidden = true;
            c.value = 0;
            x.options.add(c);
            window.$("#Practicas").prop("disabled", true);
        }

        
    }

    async function listarProfesionales() {
        //console.log("Este es el valor de especialidad!! " + window.$("#Especialidades").val());
        const response = await fetch("http://localhost:5000/events/getProfessionalsBySpecialities?specialityID=" + window.$("#Especialidades").val())

        const profesionales = await response.json();
        
        console.log(profesionales);

        window.$("#Profesionales").empty();


        var x = document.getElementById("Profesionales");
        var c = document.createElement("option");

        if (profesionales.error == 0) {
            c.text = "Seleccione un profesional";

            x.options.add(c);
            c.selected = true;
            c.hidden = true;
            c.value = 0;
            x.options.add(c);
            /*console.log(c);
            console.log(profesionales);
            console.log(profesionales.status.length);*/

            for (var i = 0; i < profesionales.status.length; i++) {
                c = document.createElement("option");
                c.text = profesionales.status[i].Nombre;
                c.value = profesionales.status[i].ID;
                x.options.add(c);
                //console.log(c);
            }
            
            window.$("#Profesionales").prop("disabled", false);

        } else {
            c.text = "Esta especialidad aún no tiene profesionales.";
            c.selected = true;
            c.hidden = true;
            c.value = 0;
            x.options.add(c);
            window.$("#Profesionales").prop("disabled", true);
        }

        
    }

    

    function loadCalendar(eventos) {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            dateClick: function(info) {
                //window.$("#exampleModal").modal();
                console.log(info);
                
                listarEspecialidades();     //Pide datos y llena el select.

                window.$("#addTurnoModal").modal();


                


                /*var calendarDia = new FullCalendar.Calendar(calendarEl, {
                    initialView: 'timeGridWeek',

                    slotEventOverlap: true,

                    events: [
                        {

                        }





                    ]

                });
                
                window.$("#exampleModal").modal();*/


                /*calendar.addEvent({
                    title: "Evento 1",
                    date: info.dateStr
                });*/
            },

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
                window.$("#turnoID").val(info.event.extendedProps.turnoID.toString());
                valorcito = Number(info.event.extendedProps.turnoID);
                console.log("Este es valorcito: " + valorcito);

                console.log("Este es el ID de arriba: " + window.$("#turnoID").val());
            },

            events: eventos,
        });

        calendar.setOption('locale', 'Es');

        calendar.render();
    }



    /*document.addEventListener('DOMContentLoaded', function() {
        
    });*/

    /*function cancelarTurno(turnoID) {
        
    }*/

    async function cancelarTurno() {
        var turnoID = valorcito;
        console.log("Este es el ID del turno: " + turnoID);

        let data = { appointmentID : Number(turnoID) };
        console.log("Esta es la data: " + data);
        const res = await fetch("http://localhost:5000/events/deleteEvent", {
            method: 'PUT',
            headers: { 'Content-Type' : 'application/json;charset=utf-8' },
            body: JSON.stringify(data)
        })

        const json = await res.json()
        //let result = JSON.stringify(json)
        
        console.log(json);
        console.log(json.error);

        if (json.error == 0) {
            window.$("#exampleModal").hide();
            location.reload();
            console.log("Success");
        } else {
            console.log("Error");
        }

    }
    


</script>

<br>
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
            <input type="hidden" id="turnoID" bind:value={valorcito}>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" on:click={() => cancelarTurno()}>Cancelar turno</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
        
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="addTurnoModal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Añadir nuevo turno</h5>
        <button type="button" class="close" data-dismiss="modal">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="centrado">
        <div class="modal-body" id="eventDescription">

            <div class="form-group form-row align-items-end">
                <label class="col-md-12">Especialidad</label>
                <select name="Especialidades" id="Especialidades" class="form-control" on:change={() => {listarPracticas(); listarProfesionales();}}>
                </select>
            </div>

            <div class="form-group form-row align-items-end">
                <label class="col-md-12">Práctica</label>
                <select name="Practicas" id="Practicas" class="form-control">
                </select>
            </div>

            <div class="form-group form-row align-items-end">
                <label class="col-md-12">Profesionales</label>
                <select name="Profesionales" id="Profesionales" class="form-control">
                </select>
            </div>

        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-success" on:click={() => cancelarTurno()}>Agregar turno</button>
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