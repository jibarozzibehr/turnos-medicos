<script>
	import Home from "./Home/Home.svelte";
	import Client from "./Client/Client.svelte";

	export let page;


	function funcioncita() {
		if (page == "Home") {
			page = "Mis turnos";
		}
		else {
			page = "Home";
		}
	}

</script>





<main>
	<Client />

	{#if page === "Home"}
	<Home />
	{:else if page === "Mis turnos"}
	<Client />
	​​
	{/if}

	<button type="button" on:click={funcioncita}>Change</button>

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