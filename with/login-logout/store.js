import {writable} from 'svelte/store';

function userStore(){
	const { suscribe, set} = writable(getStorageUser());

	return {
		suscribe,
		loginUser: (arg) => set(arg),
		logoutUser: () => set(null)
	}
}

export function setStorageUser(user){	//Permite que no se salga el usuario al refrescar a pagina
	localStorage.setItem('user', JSON.stringify(user));
}

function getStorageUser(){
	localStorage.getItem('user') ? JSON.parse(localStorage.getItem(user)) : null;
}

export const user = userStore();