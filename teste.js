// // Supondo que o id do input seja 'id_dependentes_111698' e o id do botão seja 'submit_fieltorcedor_booking_by_dependente_form'
// function(){
//     var idDoInput = 'id_dependentes_111698';
//     var idDoBotao = 'submit_fieltorcedor_booking_by_dependente_form';

//     // Definir o intervalo
//     var intervalo = setInterval(function() {
//         var input = document.getElementById(idDoInput);

//         // Se o input existir
//         if (input) {
//             // Adicionar o atributo
//             input.setAttribute('data-gtm-form-interact-field-id', '0');

//             // Obter o botão
//             var botao = document.getElementById(idDoBotao);

//             // Se o botão existir
//             if (botao) {
//                 // Clicar no botão
//                 botao.click();
//             }

//             // Parar o intervalo
//             clearInterval(intervalo);
//         }
//     }, 500);  // Verificar a cada 500 milissegundos
// };

function marcarCheckBoxesDisponiveis() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:not(:checked)');
  
    for (const checkbox of checkboxes) {
      checkbox.checked = true;
    }
}
marcarCheckBoxesDisponiveis();
document.getElementById("submit_fieltorcedor_booking_by_dependente_form").disabled = false;
