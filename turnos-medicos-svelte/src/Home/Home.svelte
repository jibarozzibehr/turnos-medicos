<script>
    import moment  from 'moment';
    import 'moment/locale/es';

    async function getTurnos(clientID) {
        const response = await fetch("http://localhost:5000/events/getClientPendingEvents?clientID=" + clientID.toString())

        const turnos = await response.json();

        //myTodo = todo.items
        
        console.log(turnos)

        
        var plantilla = ""
        

        if (turnos.error == 0) {
            var fechaHora = turnos.status[0].Fecha_Turno;
            console.log(fechaHora);

            moment.locale('es');
            var fecha = moment(fechaHora).format('LL');
            console.log(fecha);
            var hora = moment(fechaHora).format('hh:mm');
            console.log(hora);
            
            plantilla = '<h2 class="text-left">Su próximo turno es:</h2>'
            plantilla += '<h5 class="text-left">El ' + fecha + ' a las ' + hora + '</h5>';
            plantilla += '<h6 class="text-left">Con ' + turnos.status[0].Profesional + ' en la clínica ' + turnos.status[0].Clinica + '</h6>';
            plantilla += '<h6 class="text-left">Asunto: ' + turnos.status[0].Titulo + '</h6>';
            plantilla += '<div class="text-right"> <button type="button" class="btn btn-primary">Más detalles</button> </div>'
        } else if (turnos.error == 1) {
            //plantilla = '<h2 class="text-left">Su próximo turno es:</h2>'
            plantilla += "<h5>No tiene turnos pendientes.</h5>";
        } else {
            plantilla += "<h5>Error.</h5>";
        }
        
        window.$("#proximoTurno").html(plantilla);
    }

    //function getAllTurnos() {
    getTurnos(1);
    //}

</script>

    <div class="container">
        <br>
        <h1>Home</h1>
        <br>
        <!--<h2 class="text-left">Su próximo turno es:</h2>-->
        <div id="proximoTurno" class="alert alert-primary col-md-6"> 
        </div>
        <!--<button type="button" class="btn btn-danger" on:click={getAllTurnos}>Cancelar turno</button>-->

    </div>