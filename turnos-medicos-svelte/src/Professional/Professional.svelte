<script>
    import moment from 'moment';
    import 'moment/locale/es';
    import { link, navigate } from 'svelte-routing';
    import { idGlobal, medico, matricula } from './../location.js';
    import { onMount } from 'svelte';

	onMount (
        async () => {
			//var plantilla = "";
			console.log("ID Global: " + $idGlobal);

			if ($idGlobal == 0 || $medico != "true") {
				navigate("/", { replace: true });
            }

            getTurnos($matricula);
        }
	)

    async function getTurnos(professionalID) {
        console.log("Matricula: " + $matricula)
        var plantilla = ""
        const response = await fetch("http://localhost:5000/events/getProfessionalsClinics?professionalID=" + professionalID.toString());

        /*const response = await fetch("http://localhost:5000/events/getProfessionalEvents", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
            },
            body: JSON.stringify({ clinicID, professionalID }),
        });*/

        const clinicas = await response.json();

        //myTodo = todo.items
        
        console.log("Lo que devuelve status: " + JSON.stringify(clinicas.status))

        var response2 = {};

        console.log("Error de las clinicas: " + clinicas.error);

        if (clinicas.error == 0) {
            for (let index = 0; index < clinicas.status.length; index++) {
                response2 = await fetch("http://localhost:5000/events/getProfessionalEventsNotCancelled?clinicID=" + clinicas.status[index].ID + "&professionalID=" + professionalID);
                const turnos = await response2.json();
                
                

                plantilla += '<div id="proximoTurno" class="alert alert-primary col-md-5" style="margin: 5px auto;">'
                plantilla += '<h2 class="text-left">' + clinicas.status[index].Nombre + '</h2>'
                

                if (turnos.error == 0) {
                    var fechaHora = turnos.status[0].Fecha_Turno
                    moment.locale('es');
                    var fecha = moment(fechaHora).format('LL');
                    var hora = moment(fechaHora).format('HH:mm');

                    console.log("Hay turnos en " + clinicas.status[index].Nombre);
                    console.log("Turnos: " + JSON.stringify(turnos))
                    plantilla += '<h4 class="text-left">Su próximo turno es:</h4>'
                    plantilla += '<h5 class="text-left">El ' + fecha + ' a las ' + hora + '</h5>'
                    plantilla += '<h6 class="text-left">Asunto: ' + turnos.status[0].Titulo + '</h6>'
                    plantilla += '<h6 class="text-left">Descripción: ' + turnos.status[0].Descripcion + '</h6>'

                } else if (turnos.error == 1) {
                    console.log("No hay turnos en " + clinicas.status[index].Nombre);
                    plantilla += '<h4 class="text-left">No hay turnos próximos.</h4>'
                } else {
                    plantilla += '<h4 class="text-left">Error.</h4>'
                }
                plantilla += '</div>'
                //console.log("Estos son los turnos para este doctor en esta clinica: " + JSON.stringify(turnos))
                
            }
        } else {
            plantilla += "<h3> Usted no pertenece a ninguna clínica. </h3>"
        }

        
        //const response2 = await fetch("http://localhost:5000//events/getProfessionalsClinics?professionalID=" + professionalID.toString());
        

        var data = [];
        data = {

        }
        
        
        

        /*if (clinicas.error == 0) {
            var fechaHora = clinicas.status[0].Fecha_Turno;
            console.log(fechaHora);

            moment.locale('es');
            var fecha = moment(fechaHora).format('LL');
            console.log(fecha);
            var hora = moment(fechaHora).format('hh:mm');
            console.log(hora);
            
            plantilla += '<h2 class="text-left">Su próximo turno es:</h2>'
            plantilla += '<h5 class="text-left">El ' + fecha + ' a las ' + hora + '</h5>';
            plantilla += '<h6 class="text-left">Con ' + clinicas.status[0].Profesional + ' en la clínica ' + clinicas.status[0].Clinica + '</h6>';
            plantilla += '<h6 class="text-left">Asunto: ' + clinicas.status[0].Titulo + '</h6>';
            plantilla += '<div class="text-right"> <button type="button" class="btn btn-primary">Más detalles</button> </div>'
        } else if (clinicas.error == 1) {
            //plantilla = '<h2 class="text-left">Su próximo turno es:</h2>'
            plantilla += "<br><h5>No tiene clínicas.</h5>";
        }*/
        
        window.$("#clinicasTurnos").html(plantilla);
    }

    //function getAllTurnos() {
    
    //}

    async function getUsuario() {
        const response = await fetch("http://localhost:5000/events/getUserData?userID=" + $idGlobal);

        const userData = await response.json();
        
        console.log("Lo que devuelve status: " + JSON.stringify(userData.status))

        console.log("Error del getUserData: " + userData.error);

        if (userData.error == 0) {
            //Se cargan los datos y se muestra el modal
            console.log("Entra" + userData.status.nombre);
            window.$("#editNombre").val(userData.status.nombre);
            window.$("#editDNI").val(userData.status.dni);
            window.$("#editEmail").val(userData.status.email);
            window.$("#editTelefono").val(userData.status.telefono);

            window.$("#editUserModal").modal();
        } else {

        }
    }



    async function editUsuario() {
        var nombreInput = window.$("").val;

        let data = {
            userID: Number($idGlobal),
            nombre: ,
            dni: Number(),
            email: ,
            telefono: Number(),
        };
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
            window.$("#exampleModal").modal('hide');
            getTurnos($codCliente);
            //location.reload();
            //navigate("/misturnos", { replace: true });
            console.log("Success");
        } else {
            console.log("Error");
        }

    }

</script>

<style>
    .titulo {
        text-align: center;
    }
</style>

<nav class="navbar navbar-expand-lg navbar-light bg-light">	
    <div class="container">
        <a class="navbar-brand" href="/">Turnos</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div id="navBar" class="navbar-nav ml-auto">

                <a href="/profesional" use:link class="nav-item nav-link">Home</a>
                <a href="/turnosprofesional" use:link class="nav-item nav-link">Mis turnos</a>
                <a href="/logout" use:link class="nav-item nav-link">Cerrar sesión</a>

            </div>
        </div>
    </div>
</nav>

<div class="container">
    <!--<div id="navBar"></div>-->
        



    <br>
    <!--Arreglar esto!!!-->
    <div class="text-center">
        <h1 class="titulo text-center">Home</h1>
        <button type="button" class="btn btn-primary" on:click={() => getUsuario()}>Mis datos</button>
    </div>
    
    <br>
    
    <div id="clinicasTurnos" class="row">
    </div>

    

        <!--<div class="row">
            <div id="turno1" class="alert alert-primary col-md-5" style="margin: auto;">Turno1</div>
            <div id="turno2" class="alert alert-primary col-md-5" style="margin: auto;">Turno2</div>
        </div>-->
        <!--<div id="proximoTurno" class="alert alert-primary col-md-6"> 
        </div>-->
        

</div>

<div class="modal fade" id="editUserModal" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Editar mis datos</h5>
                <button type="button" class="close" data-dismiss="modal">
                </button>
            </div>
            

            <div class="modal-body" id="userDescription">
                <div class="form-group">
                    <label for="editNombre">Nombre y Apellido</label>
                    <input type="text" class="form-control" placeholder="Nombre y Apellido" id="editNombre">
                </div>

                <div class="form-group">
                    <label for="editDNI">DNI</label>
                    <input type="number" class="form-control" placeholder="DNI" id="editDNI">
                    <small id="editDNIHelp" class="form-text text-muted">Sólo números.</small>
                </div>   
                
                <div class="form-group">
                    <label for="editEmail">Email</label>
                    <input type="text" class="form-control" placeholder="Email" id="editEmail">
                </div>
                    
                <div class="form-group">
                    <label for="editTelefono">Teléfono</label>
                    <input type="number" class="form-control" placeholder="Teléfono" id="editTelefono">
                    <small id="editTelefonoHelp" class="form-text text-muted">Sólo números.</small>
                </div>
            </div>

            
            <div class="modal-footer">
                <button type="button" class="btn btn-success" on:click={() => editUsuario()}>Guardar cambios</button>
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                
            </div>
        </div>
    </div>
</div>