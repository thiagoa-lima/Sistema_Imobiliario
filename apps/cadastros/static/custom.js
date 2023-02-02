// Máscara para formularios
var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
};
  


django.jQuery(function(){
  // Incluir aqui abaixo as máscaras de entrada do formulário no Admin do Django
  django.jQuery('.mask-telefone').mask(SPMaskBehavior, spOptions);
  django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});
  django.jQuery('.mask-data').mask('00/00/0000');
  django.jQuery('.mask-cep').mask('00.000-000');
  

  // Permitir que a máscara fucione apenas no formulário e não deixar que vá para o banco de dados após salvar
  django.jQuery('#clientes_form').submit(function(){
    django.jQuery('#clientes_form').find(":input[class*='mask-']").unmask();
  });

});