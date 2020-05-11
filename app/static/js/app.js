$(document).ready(function(){
    $('.cnpj_cpf').mask('00000000000');

   $('#exampleModal').modal('show')

    $('#new_epi_modal_form').submit(function(e) {
        $('#epi_submit').prop('disabled', true);
    })
})
