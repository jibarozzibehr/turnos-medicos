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
        window.$("#Practicas").empty();
        window.$("#Profesionales").empty();
        window.$("#Practicas").prop("disabled", true);
        window.$("#Profesionales").prop("disabled", true);
        window.$("#Horarios").prop("disabled", true);
    }


    async function listarClinicas() {
        const response = await fetch("http://localhost:5000/events/getClinics")

        const clinicas = await response.json();
        
        window.$("#Clinicas").empty();

        var x = document.getElementById("Clinicas");
        var c = document.createElement("option");
        c.text = "Seleccione una clinica";
        x.options.add(c);
        c.selected = true;
        c.hidden = true;
        c.value = 0;
        x.options.add(c);
        //console.log(c);
        for (var i = 0; i < clinicas.status.length; i++) {
            c = document.createElement("option");
            c.text = clinicas.status[i].Nombre;
            c.value = clinicas.status[i].ID;
            x.options.add(c);
            //console.log(c);
        }
        window.$("#Practicas").empty();
        window.$("#Profesionales").empty();
        window.$("#Practicas").prop("disabled", true);
        window.$("#Profesionales").prop("disabled", true);
        window.$("#Horarios").prop("disabled", true);
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
            var cantidad = 0;
            for (var i = 0; i < profesionales.status.length; i++) {

                let data = { clinicID : window.$("#Clinicas").val(),professionalID : profesionales.status[i].Matricula ,date: Number(window.$("#Diaa").val()) };
                console.log(data);
                const response = await fetch("http://localhost:5000/events/getProfessionalDaySchedule", {
                    method: 'POST',
                    headers: { 'Content-Type' : 'application/json;charset=utf-8' },
                    body: JSON.stringify(data)
                })

                const horarios = await response.json();
            
                //console.log(horarios);
                if(horarios.error == 0){
                    c = document.createElement("option");
                    c.text = profesionales.status[i].Nombre;
                    c.value = profesionales.status[i].Matricula;
                    x.options.add(c);
                    console.log(c);
                    cantidad++;
                }
                
            }

            if(cantidad>0){
                window.$("#Profesionales").prop("disabled", false);
            }else{
                c.text = "Esta especialidad no tiene profesionales trabajando el dia seleccionado.";
                c.selected = true;
                c.hidden = true;
                c.value = 0;
                x.options.add(c);
                window.$("#Profesionales").prop("disabled", true);
                window.$("#Horarios").empty();
                window.$("#Horarios").prop("disabled", true);
            }
            

        } else {
            c.text = "Esta especialidad aún no tiene profesionales.";
            c.selected = true;
            c.hidden = true;
            c.value = 0;
            x.options.add(c);
            window.$("#Profesionales").prop("disabled", true);
            window.$("#Horarios").empty();
            window.$("#Horarios").prop("disabled", true);
        }

        listarHorarios();

        
    }



    function listarAll(){
        if(window.$("#Especialidades").val()!=0 && window.$("#Clinicas").val()!=0){
            listarProfesionales();
            //console.log(moment().format('YYYY-MM-DD HH:MM'));
        }
    }


    

    function loadCalendar(eventos) {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            dateClick: function(info) {
                //window.$("#exampleModal").modal();
                console.log(info);
                
                volver();
                window.$("#Titulo").val("");
                
                window.$("#Descripcion").val("");

                listarEspecialidades();     //Pide datos y llena el select.
                listarClinicas();

                
                window.$("#DiaTurno").html(moment(info.dateStr).format('DD/MM/YYYY'));
                window.$("#Fechaa").val(moment(info.dateStr).format('YYYY-MM-DD'));
                var dt = new Date(moment(info.dateStr));
                
                //window.$("#DiaTurno").html(moment(info.dateStr).format('DD/MM/YYYY'));
                

                window.$("#Diaa").val(dt.getDay());
                window.$("#addTurnoModal").modal();
                console.log(window.$("#Diaa").val());

                


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



    function siguientePaso(){
        //alert("To Do!");
        window.$("#divEspecialidades").hide();
        window.$("#divPracticas").hide();
        window.$("#divClinicas").hide();
        window.$("#divProfesionales").hide();
        window.$("#divFecha").hide();
        window.$("#divBotones1").hide();
        window.$("#divTitulo").show();
        window.$("#divDescripcion").show();
        window.$("#divBotones2").show();
        window.$("#divHorarios").hide();
    }


    function volver(){
        //alert("To Do!");
        window.$("#divEspecialidades").show();
        window.$("#divPracticas").show();
        window.$("#divClinicas").show();
        window.$("#divProfesionales").show();
        window.$("#divFecha").show();
        window.$("#divBotones1").show();
        window.$("#divTitulo").hide();
        window.$("#divDescripcion").hide();
        window.$("#divBotones2").hide();
        window.$("#divHorarios").show();
    }

    function agregarTurno(){
        alert("To Do!");
    }
    
    async function listarHorarios() {
        console.log("a aaaa aaa");
        //console.log("Este es el valor de especialidad!! " + window.$("#Especialidades").val());
        let data = { clinicID : window.$("#Clinicas").val(),professionalID : window.$("#Profesionales").val(),date: Number(window.$("#Diaa").val()) };
        console.log(data);
        const response = await fetch("http://localhost:5000/events/getProfessionalDaySchedule", {
            method: 'POST',
            headers: { 'Content-Type' : 'application/json;charset=utf-8' },
            body: JSON.stringify(data)
        })

        const horarios = await response.json();
        
        console.log(horarios);

        var FechaInicio = window.$("#Fechaa").val() + " 00:00";
        var FechaFin = window.$("#Fechaa").val()+ " 23:59";

        let data2 = { clinicID : window.$("#Clinicas").val(),professionalID : window.$("#Profesionales").val(),beginDate: FechaInicio, finishDate: FechaFin};
        console.log(data2);

        const response2 = await fetch("http://localhost:5000/events/getProfessionalDayEvents", {
            method: 'POST',
            headers: { 'Content-Type' : 'application/json;charset=utf-8' },
            body: JSON.stringify(data2)
        })

        const turnos = await response2.json();
        console.log(turnos);
        //console.log("bbbbbbbbbbbbb");
       // console.log(moment(window.$("#Fechaa").val() +" "+ (horarios.status[0].Horario_Fin)));


            if(window.$("#Profesionales").val() == 0){
                console.log("a verrrrrrrrrrrrrrr");
                window.$("#Horarios").empty();
                window.$("#Horarios").prop("disabled", true);
                return;
            }

       var x = document.getElementById("Horarios");
        var c = document.createElement("option");
       if(horarios.error ==0 && turnos.error ==0){
            var arrayHorarios = []
            var pos=0;
            //var str =  "2020-11-01 00:00";
            //console.log(str.replace(/-/g,"/"));
            var inicio = moment(window.$("#Fechaa").val() +" "+ (horarios.status[0].Horario_Inicio));
            //console.log("   AAAAAAAAAAAAAAAA");
            //console.log((horarios.status[0].Horario_Fin).replace(/-/g,"/"))
            var fin = moment(window.$("#Fechaa").val() +" "+ (horarios.status[0].Horario_Fin));
            var actual = inicio;
            console.log(fin);
            //console.log("Hol2222a");
                console.log(actual);
            var cont = 0;
            //console.log(moment(turnos.status[0].Fecha_Turno).format("HH:mm"));

            while(cont < turnos.status.length){
                //console.log("11111111111111")
                //console.log(actual)
                if(moment(turnos.status[cont].Fecha_Turno).format("HH:mm") != actual.format("HH:mm")){
                    //console.log("asdasd");
                    //console.log(actual.format("HH:mm"));
                    arrayHorarios[pos] = actual.format("HH:mm");
                    pos++;
                }else{
                    cont++;
                }
                actual.add(1, 'hours');
                
                
            }

            

            while(actual < fin ){
                //console.log("22222222222222");
                //console.log(actual)
                //console.log(actual.format("HH:mm"));
                arrayHorarios[pos] = actual.format("HH:mm");
                pos++;
                actual = actual.add(1, 'hours');
            }

            //console.log(arrayHorarios);

            window.$("#Horarios").empty();


           

           
               console.log("a ver");
                c.text = "Seleccione un horario";

            x.options.add(c);
            c.selected = true;
            c.hidden = true;
            c.value = 0;
            x.options.add(c);
            /*console.log(c);
            console.log(practicas);
            console.log(practicas.status.length);*/

            for (var i = 0; i < arrayHorarios.length; i++) {
                c = document.createElement("option");
                c.text = arrayHorarios[i];
                c.value = arrayHorarios[i];
                x.options.add(c);
                console.log(c);
            }
            window.$("#Horarios").prop("disabled", false);
           

       }

        //var status = moment(myDate).add(5, 'hours').format('YYYY-MM-DD hh:mm:ss');
        
        

        
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

<div class="modal fade " id="addTurnoModal" tabindex="-1" role="dialog">
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

            <div id="divEspecialidades" class="form-group form-row align-items-end">
                <label class="col-md-12" for="Especialidades">Especialidad</label>
                <select name="Especialidades" id="Especialidades" class="form-control" on:change={() => {listarPracticas(); listarAll();}}>
                </select>
            </div>

            <div id="divPracticas" class="form-group form-row align-items-end">
                <label class="col-md-12" for="Practicas"> Práctica</label>
                <select name="Practicas" id="Practicas" class="form-control">
                </select>
            </div>

            <div id="divClinicas" class="form-group form-row align-items-end">
                <label class="col-md-12" for="Clinicas"> Clínica</label>
                <select name="Clinicas" id="Clinicas" class="form-control" on:change={() => {listarAll();}}>
                </select>
            </div>

            <div id="divProfesionales" class="form-group form-row align-items-end">
                <label class="col-md-12" for="Profesionales">Profesional</label>
                <select name="Profesionales" id="Profesionales" class="form-control" on:change={() => {listarHorarios();}}>
                </select>
            </div>
            <div id="divFecha" class="form-group form-row align-items-end">
                <label class="col-md-4" for="DiaTurno">Fecha del turno:</label> 
                <p class="col-md-8" id="DiaTurno" name="DiaTurno"></p>
                <!--<input type="date" class="form-control" id="DiaTurno" name="DiaTurno" placeholder="DD/MM/YYY" disabled> -->
            </div>

            <div id="divDiaa" class="form-group form-row align-items-end" hidden>
                <label class="col-md-4" for="Dias">Dia:</label> 
                <input type="text" id="Diaa">
                <input type="text" id="Fechaa">
                <!--<input type="date" class="form-control" id="DiaTurno" name="Dias" placeholder="DD/MM/YYY" disabled> -->
            </div>

            <div id="divHorarios" class="form-group form-row align-items-end">
                <label class="col-md-12" for="Horarios"> Horario</label>
                <select name="Horarios" id="Horarios" class="form-control">
                </select>
            </div>


            <div id="divTitulo" class="form-group form-row align-items-end">
                <label class="col-md-4" for="Titulo">Razón de su visita:</label> 
                <input type="text" class="form-control" id="Titulo" name="Titulo" placeholder="Razón">
            </div>

            <div id="divDescripcion" class="form-group form-row align-items-end">
                <label class="col-md-4" for="Descripcion">Descipción</label> 
                <textarea class="form-control" id="Descripcion" name="Descripcion" rows="3" placeholder="Describa brevemente sus síntomas"></textarea>
            </div>


            
            

        </div>
      </div>
      <div class="modal-footer">
        <div id="divBotones1">
            <button type="button" class="btn btn-primary" on:click={() => siguientePaso()}>Siguiente</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
        </div>
        <div id="divBotones2">
            <button type="button" class="btn btn-secondary" on:click={() => volver()}>Volver</button>
            <button type="button" class="btn btn-success" on:click={() => agregarTurno()}>Agregar</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
            
        </div>
        
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