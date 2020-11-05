<script>
    export let page;

    window.onload = function () {
        var plantilla = "Hola";

        switch (page) {
            case "Home":
                plantilla = '<a class="nav-item nav-link active" href="./">Home</a> <a class="nav-item nav-link" href="#">Mis turnos</a> <a class="nav-item nav-link" href="#">Agregar turno</a>';
                break;
            case "Mis turnos":
                plantilla = '<a class="nav-item nav-link" href="./">Home</a> <a class="nav-item nav-link active" href="#">Mis turnos</a> <a class="nav-item nav-link" href="#">Agregar turno</a>';
                break;
            case "Agregar turno":
                plantilla = '<a class="nav-item nav-link" href="./">Home</a> <a class="nav-item nav-link" href="#">Mis turnos</a> <a class="nav-item nav-link active" href="#">Agregar turno</a>';
                break;
        }

        window.$("#navBar").html(plantilla);
    }

</script>













<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="#">Turnos</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div id="navBar" class="navbar-nav ml-auto">
                <!--<a class="nav-item nav-link active" href="#">Home</a>
                <a class="nav-item nav-link" href="#">Features</a>
                <a class="nav-item nav-link" href="#">Pricing</a>
                <a class="nav-item nav-link disabled" href="#">Disabled</a>-->
            </div>
        </div>
    </div>
</nav>