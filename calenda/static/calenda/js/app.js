function eliminarEntrada(entrada) {
    //console.log("Eliminando entrada...")
    var $entrada = $(entrada)
    $entrada.parent().remove();
    var id = $entrada.data('id');
    console.log(id)

    $.ajax({
        url: 'entrada/eliminar/'+ id,
        method: 'DELETE',
        beforeSend: function(xhr){
            xhr.setRequestHeader('X-CSRFToken',csrf_token)
        }
    });

}
