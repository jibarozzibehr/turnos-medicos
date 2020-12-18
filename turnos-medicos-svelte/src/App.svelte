<script>
	import { Router, Route, Link, link, navigate } from 'svelte-routing';
	import Home from "./Home/Home.svelte";
	import Client from "./Client/Client.svelte";
	import Professional from "./Professional/Professional.svelte";
	import ProfessionalCalendar from "./Professional/ProfessionalCalendar.svelte";
	import Login from "./Login.svelte";
	import Logout from "./Logout.svelte";

	import { idGlobal, medico } from "./location.js";
    import { onMount } from 'svelte';

	onMount (
        async () => {
			//var plantilla = "";
			console.log("ID Global al inicio: " + $idGlobal);

			if ($idGlobal != 0 && $medico == "false") {	//Si inició sesión y no es médico.
				

				navigate("/", { replace: true });

			} else if ($idGlobal != 0 && $medico == "true") {
				
				navigate("/profesional", { replace: true });
			} else if (idGlobal == 0) {
				
				//window.$("#navBar").html(plantilla);	

				//navigate("/login", { replace: true });
			}

			//plantilla = "Hola";

			//window.$("#navBar").html(plantilla);
					//loadCalendar();
		}
	)

	//export let page;



	


	/*window.onload = function () {
        var plantilla = "Hola";

        switch (page) {
            case "Home":
                plantilla = '<a href="/" use:link class="nav-item nav-link active">Home</a> <a class="nav-item nav-link" href="#" use:link>Mis turnos</a> <a class="nav-item nav-link" href="#" use:link>Agregar turno</a>';
                break;
            case "Mis turnos":
                plantilla = '<a class="nav-item nav-link" href="./" use:link>Home</a> <a class="nav-item nav-link active" href="#" use:link>Mis turnos</a> <a class="nav-item nav-link" href="#" use:link>Agregar turno</a>';
                break;
            case "Agregar turno":
                plantilla = '<a class="nav-item nav-link" href="./" use:link>Home</a> <a class="nav-item nav-link" href="#" use:link>Mis turnos</a> <a class="nav-item nav-link active" href="#" use:link>Agregar turno</a>';
                break;
        }

        window.$("#navBar").html(plantilla);
    }*/

</script>





<main>


	
	<Router>
		
		<div id="navBar"></div>
		<!--<nav class="navbar navbar-expand-lg navbar-light bg-light">
			

			<div class="container">
				<a class="navbar-brand" href="/">Turnos</a>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
					<div id="navBar" class="navbar-nav ml-auto">
						
						<a href="/" use:link class="nav-item nav-link">Home</a>
						<a href="/misturnos" use:link class="nav-item nav-link">Mis turnos</a>
						<a href="/profesional" use:link class="nav-item nav-link">Profesional</a>
						<a href="/turnosprofesional" use:link class="nav-item nav-link">Turnos Profesional</a>
						<a href="/login" use:link class="nav-item nav-link">Login</a>
						



					</div>
				</div>
			</div>






		</nav>-->

		<div>
			<Route path="/" component={Home}>  </Route>
			<Route path="/misturnos" component={Client}>  </Route>
			<Route path="/profesional" component={Professional}>  </Route>
			<Route path="/turnosprofesional" component={ProfessionalCalendar}>  </Route>
			<Route path="/login" component={Login}>  </Route>
			<Route path="/logout" component={Logout}>  </Route>
		</div>
	</Router>





	

</main>


<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		/*margin: 0 auto;*/
		margin: 0 !important;
		padding: 0 !important;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>