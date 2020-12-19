export async function getUsuario() {
    const response = await fetch("http://localhost:5000/events/getUserData?userID=" + $idGlobal);

    const userData = await response.json();
    
    console.log("Lo que devuelve status: " + JSON.stringify(userData.status))

    console.log("Error del getUserData: " + userData.error);

    if (userData.error == 0) {
        //Se cargan los datos y se muestra el modal
        window.$("#editUserModal").modal();
    } else {

    }
}