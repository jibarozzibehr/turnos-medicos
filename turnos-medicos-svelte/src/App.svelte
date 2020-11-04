
<script>
	import Client from "./Client.svelte"
	//import {onMount} from "svelte"
	//export let name;
	var PressedButton=false;

	
	function myFunction(){
		/*
		 PressedButton=!PressedButton;
		 if(PressedButton){
			document.body.style.backgroundColor = "black";
		 }else{
			document.body.style.backgroundColor = "red";
		 }*/

		 //document.body = "<Client/>"
		 //document.getElementById("p1").innerHTML = "<Client/>";
		 PressedButton=!PressedButton
		// location.reload();
		
		//window.location.href = "./Client.svelte";
	}
</script>
<main>
	<button type="button" class="btn btn-success" on:click={myFunction}>Success</button>
	<Client/>
	{#if  PressedButton === true}
		<Client/>
		{:else}
		<h1>Hola222222</h1>
	{/if}​​



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