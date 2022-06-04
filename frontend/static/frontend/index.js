import { create_datepicker } from './datepicker.js'
import { create_chart } from './chart.js'
import { throw_error_modal } from './error_modal.js'


create_datepicker('startdate', new Date().setDate(new Date().getDate()-4));
create_datepicker('enddate');

let fetching_data = false;
const update_chart = () => {
    if (fetching_data == true){
        return;
    };
    fetching_data = true;

    $('#loader').show();
    $('#grafico').hide();

    let payload = {
        currency_from: $('#currency1 :first-child').data('currency'),
        currency_to: $('#currency2 :first-child').data('currency'),
        start_date: $('#startdate').val(),
        end_date: $('#enddate').val(),
    };
    $.ajax({
        url: "/cotacao/get-rate/",
        type: 'GET',
        dataType: 'json',
        data: payload,
        success: function(response) {
            let categories = [];
            let rates = {};
            response.map(function(item){
                categories.push(item.date);
                Object.entries(item.rates).map(
                    ([key, value]) => {
                        if (!(key in rates)){
                            rates[key] = [];
                        };
                        rates[key].push(value);
                    }
                );
            });
            create_chart('grafico', categories, rates);
        },
        error: function(response){
            throw_error_modal(response.responseText);
        },
        complete: function(){
            $('#loader').hide();
            $('#grafico').show();
            fetching_data = false;
        }
    });
};

document.addEventListener('DOMContentLoaded', function () {
    update_chart();
});

const switch_currencies = () => {
    let temp_flag = $('#currency1').html();
    $('#currency1').html($('#currency2').html());
    $('#currency2').html(temp_flag);
};

$('#switch_currencies').click(function(){
    switch_currencies();
    update_chart();
});

$('.dropdown-menu li a').click(function(event){
    event.preventDefault();

    let element = $(this).parent().parent().parent().find('.dropdown-toggle');
    let other_currency = element.is('#currency1') ? $('#currency2') : $('#currency1');

    if ($(this).html().trim() == other_currency.html().trim()){
        switch_currencies();
    } else {
        element.html($(this).html());
    };
    update_chart();
});

$('#startdate, #enddate').on('change', function(){
    update_chart();
});
