//rut
function modifyText() {
    var letters = 
                [   "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                    "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", 
                    "v", "w", "x", "y", "z", ",", ".", "!", "'", "$", "%", "&",
                    "/", "(", ")", "=", "?", "¿", "¡", ".", ","
                ]
    var txtRut = document.getElementById("txtRut")
    txtRut.value = txtRut.value.toLowerCase()
    for(let i in letters){
        txtRut.value = txtRut.value.replace(letters[i], "")
    }
    if(txtRut.value.includes("-")) {
        txtRut.value = txtRut.value.replace(/-/g, "")
        txtRut.value = txtRut.value.slice(0, txtRut.value.length - 1) + "-" + txtRut.value.slice(txtRut.value.length - 1)
    }else
    {
        txtRut.value = txtRut.value.slice(0, txtRut.value.length - 1) + "-" + txtRut.value.slice(txtRut.value.length - 1)
    }
    if(txtRut.value.includes("k")) {
        txtRut.value = txtRut.value.replace(/k/g, "")
        txtRut.value += "k"
    }
}
 //1) Definir Las Variables Correspondintes
            var opt_1 = new Array ("-", "Arica", "Camarones", "Putre","General Lagos", "...");
            var opt_2 = new Array ("-", "Iquique", "Alto Hospocio", "Pozo Almonte",  "Camiña" , "Colchane" , "Huara" , "Pica", "...");
            var opt_3 = new Array ("-", "Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollague", "San Pedro de Atacama", "Tocopilla", "María Elena", "...");
            var opt_4 = new Array ("-", "Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar","Alto del Carmen", "Freirina", "Huasco","...");
            var opt_5 = new Array ("-", "La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña","Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui","Río Hurtado","...");
            var opt_6 = new Array ("-", "Valparaíso", "Casa Blanca", "Concón", "Juan Fernàndez", "Puchuncaví", "Quintero","Viña del Mar", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo","Petorca", "Zapallar", "Quillota", "Calera","Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "El Quisco", "Cartagena", "El Tabo","Santo Domingo","San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo","Santa María","...");
            var opt_7 = new Array ("-", "Santiago", "Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estaciòn Central","Huechuraba", "Independencia", "La Cisterna", "La FLorida", "La Granja", "La Pintana", "La Reina", "Las Condes","Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul","Maipú", "Ñuñoa", "Pedro Aguierra Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal","Recoleta","Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura","Puente Alto","Pirque", "San Joaquín de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango","Paine","Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro","Talagante","El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor","...");
            // 2) crear una funcion que permita ejecutar el cambio dinamico
            
            function cambia(){
                var cosa;
                //Se toma el vamor de la "cosa seleccionada"
                cosa = document.formulario1.cosa[document.formulario1.cosa.selectedIndex].value;
                //se chequea si la "cosa" esta definida
                if(cosa!=0){
                    //selecionamos las cosas Correctas
                    mis_opts=eval("opt_" + cosa);
                    //se calcula el numero de cosas
                    num_opts=mis_opts.length;
                    //marco el numero de opt en el select
                    document.formulario1.opt.length = num_opts;
                    //para cada opt del array, la pongo en el select
                    for(i=0; i<num_opts; i++){
                        document.formulario1.opt.options[i].value=mis_opts[i];
                        document.formulario1.opt.options[i].text=mis_opts[i];
                    }
                    }else{
                        //si no habia ninguna opt seleccionada, elimino las cosas del select
                        document.formulario1.opt.length = 1;
                        //ponemos un guion en la unica opt que he dejado
                        document.formulario1.opt.options[0].value="-";
                        document.formulario1.opt.options[0].text="-";
                    }
                    //hacer un reset de las opts
                    document.formulario1.opt.options[0].selected = true;
                }
   //telefono
    function validar(number){
	var numeroTelefono=document.getElementById('id_delInputText');
	var expresionRegular1=/^([0-9]+){9}$/;//<--- con esto vamos a validar el numero
	var expresionRegular2=/\s/;//<--- con esto vamos a validar que no tenga espacios en blanco
   
	if(numeroTelefono.value=='')
	   alert('campo es obligatorio');
	else if(expresionRegular2.test(numeroTelefono.value))
	  alert('error existen espacios en blanco');
	else if(!expresionRegular1.test(numeroTelefono.value))
	  alert('Numero de telefono incorrecto');
  }
   
function valida(){
tecla = (document.all) ? e.keyCode : e.which;


//email
function validar_email( email ) 
{
var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
return regex.test(email) ? true : false;
}

//Tecla de retroceso para borrar, siempre la permite
if (tecla==8){
    return true;
    }
    
    // Patron de entrada, en este caso solo acepta numeros
    patron =/[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
    }