<script>

	import { user, setStorageUser } from "./stores/store";
	import { navigate } from "svelte-routing"; //Para el redireccionamiento a donde querramos ir

	if($user){
		navigate("/");	//Si existe se va a home directamente
	}

	let name = "";
	let password = "";

	function login() {
		setTimeout(() => {
			let usuarioRegistrado = {
				username: name,
				token: 1234,//Jason Web Token
			};
			user.loginUser(usuarioRegistrado);
			setStorageUser(usuarioRegistrado); //Persistencia del dato
			navigate("/home")//Ruta a donde nos redirigimos
		}, 1000);
	}
</script>

<h1>Login</h1>
<label for="name"> 
	Name:
	<input type="text" id="name" bind:value={name} /> 
</label>

<label for="password"> 
	Name:
	<input type="password" id="password" bind:value={password} /> 
</label>

<button> on:click={login}>Login</button>