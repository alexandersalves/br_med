let pickaday_i18n = {
    previousMonth : 'Anterior',
    nextMonth     : 'Próximo',
    months        : ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
    weekdays      : ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
    weekdaysShort : ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb'],
};
let pickaday_format = 'DD/MM/YYYY';
let pickaday_minDate = new Date(1999, 0, 4); // 04-01-1999

export const create_datepicker = (element, initial_date) => {
    let datepicker = new Pikaday({
        field: document.getElementById(element),
        i18n: pickaday_i18n,
        format: pickaday_format,
        maxDate: new Date(),
        minDate: pickaday_minDate,
    });
    datepicker.setDate(new Date(initial_date || Date()));
};
