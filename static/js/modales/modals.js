//Abrir modal para editar 
var $ = jQuery.noConflict();
function abrirModalEdicion(url){
    $('#edicion').load(url, function(){
        $(this).modal('show'); 
    });
}

//Abrir modal para eliminar 
function abrirModalEliminacion(url){
  $('#eliminacion').load(url,function(){
    $(this).modal('show'); 
  });
}