export const create_chart = (element, categories, rates) => {
    let chart = Highcharts.chart(element, {
        chart: {
            type: 'line',
        },
        title: {
            text: '',
        },
        xAxis: {
            categories: categories,
        },
        yAxis: {
            title: {
                text: '',
            },
            labels: {
                format: '{value:.2f}',
            },
        },
        series: Object.entries(rates).map(
            ([key, value]) => {
                return {
                    name: key,
                    data: value,
                };
            }
        ),
    });
    chart.series.map((serie)=>{
        if (serie.name == $('#currency1 :first-child').data('currency')){
            serie.setVisible();
        };
    });
};
