
import { writable } from 'svelte/store'

//export const idGlobal = writable(1);
//export const medico = writable(false);

//export const codCliente = writable(1);
//export const matricula = writable(0);



export const idGlobal = writable(localStorage.getItem("idGlobal") || "0");
idGlobal.subscribe(val => localStorage.setItem("idGlobal", val));

export const medico = writable(localStorage.getItem("medico") || "false");      //localStorage sólo soporta strings.
medico.subscribe(val => localStorage.setItem("medico", val));

export const codCliente = writable(localStorage.getItem("codCliente") || "0");
codCliente.subscribe(val => localStorage.setItem("codCliente", val));

export const matricula = writable(localStorage.getItem("matricula") || "0");
matricula.subscribe(val => localStorage.setItem("matricula", val));

export const especialidadID = writable(localStorage.getItem("especialidadID") || "0");
especialidadID.subscribe(val => localStorage.setItem("especialidadID", val));

