<script>
    import { idGlobal, medico, codCliente, matricula } from './location.js';
    import { navigate } from 'svelte-routing';

    idGlobal.set("0");
    medico.set("false");
    codCliente.set("0");
    matricula.set("0");
    

    navigate("/login", { replace: true });

</script>