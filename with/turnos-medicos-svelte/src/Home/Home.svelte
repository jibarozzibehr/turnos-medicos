<script>
    import moment  from 'moment';
    import 'moment/locale/es';
    import { codCliente, idGlobal, medico} from './../location.js';
    import { link, navigate } from 'svelte-routing';
    import { onMount } from 'svelte';

    onMount (
        async () => {
            if ($idGlobal != 0) {
                if($medico == "true"){
                    navigate("/profesional", { replace: false });
                }else{
                    getTurnos($codCliente);
                }
                
            } else {
                navigate("/login", { replace: false });
            }
        }
    )

    

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
            var hora = moment(fechaHora).format('HH:mm');
            console.log(hora);
            
            plantilla = '<h2 class="text-left">Su próximo turno es:</h2>'
            plantilla += '<h5 class="text-left">El ' + fecha + ' a las ' + hora + '</h5>';
            plantilla += '<h6 class="text-left">Con ' + turnos.status[0].Profesional + ' en la clínica ' + turnos.status[0].Clinica + '</h6>';
            plantilla += '<h6 class="text-left">Asunto: ' + turnos.status[0].Titulo + '</h6>';
            //plantilla += '<div class="text-right"> <button type="button" class="btn btn-primary">Más detalles</button> </div>'
        } else if (turnos.error == 1) {
            //plantilla = '<h2 class="text-left">Su próximo turno es:</h2>'
            plantilla += "<h5>No tiene turnos pendientes.</h5>";
        } else {
            plantilla += "<h5>Error.</h5>";
        }
        
        window.$("#proximoTurno").html(plantilla);
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
            window.$("#editNombre").val(userData.status.nombre);
            window.$("#editDNI").val(userData.status.dni);
            window.$("#editEmail").val(userData.status.email);
            window.$("#editTelefono").val(userData.status.telefono);

            window.$("#editUserModal").modal();
        } else {

        }
    }



    async function editUsuario() {
        var nombreInput = window.$("#editNombre").val();
        var dniInput = window.$("#editDNI").val();
        var emailInput = window.$("#editEmail").val();
        var telefonoInput = window.$("#editTelefono").val();

        let data = {
            userID: Number($idGlobal),
            nombre: nombreInput,
            dni: Number(dniInput),
            email: emailInput,
            telefono: Number(telefonoInput),
        };

        console.log("Esta es la data: " + JSON.stringify(data));
        const res = await fetch("http://localhost:5000/events/editUser", {
            method: 'PUT',
            headers: { 'Content-Type' : 'application/json;charset=utf-8' },
            body: JSON.stringify(data)
        })

        const json = await res.json()
        //let result = JSON.stringify(json)

        if (json.error == 0) {
            window.$("#editUserModal").modal('hide');
            console.log("Success");
        } else {
            window.$("#userDescription").html("<p>No se pudieron editar los datos.</p>")
        }

    }

</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">	

    <div class="container">
        <a class="navbar-brand" href="/">Turnos</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div id="navBar" class="navbar-nav ml-auto">

                <a href="/" use:link class="nav-item nav-link">Home</a>
                <a href="/misturnos" use:link class="nav-item nav-link">Mis turnos</a>
                <a href="/logout" use:link class="nav-item nav-link">Cerrar sesión</a>

            </div>
        </div>
    </div>

</nav>
<style>
    .titulo {
        text-align: center;
    }
</style>

<div class="container">
    <br>
    <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4">
            <h1 class="titulo">Home</h1>
        </div>
        <div class="col-md-4">
            <button type="button" class="btn btn-primary float-right" style="margin: 10px 5px 0 0;" on:click={() => getUsuario()}>Mis datos</button>
        </div>
    </div>
    <br>


    <!--<h2 class="text-left">Su próximo turno es:</h2>-->
    <div id="proximoTurno" class="alert alert-primary col-md-6"> 
    </div>
    <!--<button type="button" class="btn btn-danger" on:click={getAllTurnos}>Cancelar turno</button>-->

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
