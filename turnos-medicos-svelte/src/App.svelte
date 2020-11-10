<script>
	import { Router, Route, Link, link } from 'svelte-routing';
	import Home from "./Home/Home.svelte";
	import Client from "./Client/Client.svelte";

	export let page;

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
		<nav class="navbar navbar-expand-lg navbar-light bg-light">
			

			<div class="container">
				<a class="navbar-brand" href="#">Turnos</a>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
					<div id="navBar" class="navbar-nav ml-auto">
						
						<a href="/" use:link class="nav-item nav-link">Home</a>
						<a href="/misturnos" use:link class="nav-item nav-link">Mis turnos</a>
						
						<!--<Link to="/" class="nav-item nav-link"> Home </Link>
						<Link to="/misturnos" class="nav-item nav-link"> Mis turnos </Link>-->



					</div>
				</div>
			</div>






		</nav>

		<div>
			<Route path="/" component={Home}>  </Route>
			<Route path="/misturnos" component={Client}>  </Route>
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