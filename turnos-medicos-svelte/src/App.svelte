<script>
	export let name;
</script>

<main>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
  		<a class="navbar-brand" href="#">Navbar w/ text</a>
  		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    		<span class="navbar-toggler-icon"></span>
  		</button>
  		<div class="collapse navbar-collapse" id="navbarText">
    		<ul class="navbar-nav mr-auto">
      			<li class="nav-item active">
        			<a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      			</li>
      			<li class="nav-item">
        			<a class="nav-link" href="#">Features</a>
      			</li>
      			<li class="nav-item">
        			<a class="nav-link" href="#">Pricing</a>
      			</li>
    		</ul>
			<span class="navbar-text">
			Navbar text with an inline element
			</span>
  		</div>
	</nav>

	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

	<button type="button" class="btn btn-success">Success</button>
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

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>