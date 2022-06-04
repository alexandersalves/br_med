export const throw_error_modal = (error) => {
    const extract_errors = (messages) => {
        if (messages instanceof Object && !Array.isArray(messages)){
            Object.entries(messages).map(([key, value]) => {
                $('#modal-error-content').append(`
                    <p class="h5" style="text-transform:capitalize;">
                        ${key == 'non_field_errors' ? '' : key.replace(/_/g, ' ')}
                    </p>
                    <p>${value}</p>
                `);
            })
        } else if (Array.isArray(messages)){
            messages.map((value) => {
                $('#modal-error-content').append(`
                    <p>${value}</p>
                `);
            })
        } else {
            $('#modal-error-content').append(`
                <p>${messages}</p>
            `);
        };
    };

    $('#modal-error-content').empty();
    extract_errors(JSON.parse(error));
    $('#modal-error').modal('show');
};
