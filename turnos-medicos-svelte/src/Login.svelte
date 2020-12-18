<script>
    //import { getContext } from 'svelte';
    import { idGlobal, medico, codCliente, matricula } from './location.js';
    import { navigate } from 'svelte-routing';
    import { onMount } from 'svelte';

    /*onMount (
        async () => {
            //localStorage.clear();
            localStorage.getItem("codCliente");
        }
	)*/

    async function getUser(email, password) {
        const response = await fetch("http://localhost:5000/events/login?email=" + email + "&password=" + password);

        const user = await response.json();

        console.log(JSON.stringify(user))

        if (user.error == 0) {
            idGlobal.set(user.status[0].ID)
            console.log("Este es el nuevo idGlobal: " + $idGlobal)

            const response2 = await fetch("http://localhost:5000/events/isProfessional?userID=" + $idGlobal);
            const user2 = await response2.json();

            
            medico.set(JSON.stringify(user2.status.isProfessional))

            console.log("Es medico: " + $medico)

            if ($medico == "true") {
                //Cambiar Matricula
                matricula.set(user2.status.matricula)
                navigate("/profesional", { replace: true });
            } else {
                //Consultar y cambiar codCliente
                const response3 = await fetch("http://localhost:5000/events/isClient?userID=" + $idGlobal);
                const user3 = await response3.json();

                console.log("Anterior cod paciente: " + $codCliente)
                codCliente.set(JSON.stringify(user3.status.codPaciente))
                console.log("Nuevo cod paciente: " + $codCliente)
                navigate("/", { replace: true });
            }
            
            //console.log(user.status[0].ID)
        } else if (user.error == 1) {
            console.log("Incorrecto.")
            window.$("#email").val("");
            window.$("#password").val("");
        }
    }

    function comprobar() {
        var email = window.$("#email").val();
        var password = window.$("#password").val();

        //console.log(email + " " + password);

        getUser(email, password);
    }

</script>


<div class="login-form">
    <form action="/examples/actions/confirmation.php" method="post">
        <h2 class="text-center">Iniciar sesión</h2>       
        <div class="form-group">
            <input id="email" type="email" class="form-control" placeholder="Email" required="required">
        </div>
        <div class="form-group">
            <input id="password" type="password" class="form-control" placeholder="Contraseña" required="required">
        </div>
        <div class="form-group">
            <button type="button" class="btn btn-primary btn-block" on:click={() => comprobar()}>Iniciar sesión</button>
        </div>
        <!--<div class="clearfix">
            <label class="pull-left checkbox-inline"><input type="checkbox"> Remember me</label>
            <a href="#" class="pull-right">Forgot Password?</a>
        </div>-->
    </form>
    <!--<p class="text-center"><a href="#">Create an Account</a></p>-->
</div>



<style>
    .login-form {
		width: 340px;
    	margin: 50px auto;
	}
</style>