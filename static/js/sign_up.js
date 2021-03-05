function example1() {
    alert('Привет, пользователь!');
    let client = prompt('Как Вас зовут?');
    alert('Будем знакомы, ' + client + '!');
}


function example2() {
    let answer = confirm('Вы хотите посетить сайт bing.com?');
    if (answer == true) {
        window.location = 'https://www.bing.com';
    } else {
        alert('Ну, не хотите, и не надо!')
    }
}


$(document).ready(() => {
    // Сценарий валидации данных, вводимых в форму регистрации:
    let r1 = false;
    let r2 = false;

    $('#login').blur(() =>{
        let loginX = $('#login').val();
        let loginRe = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
        if (loginRe.test(loginX)) {
            // Проверка занятости логина:
            $.ajax({
                url: '/accounts/ajax_reg',
                data: 'login=' + loginX,
                success: (result) => {
                    if (result.message == 'Занят') {
                        $('#login_err').text('Логин занят!');
                        r1 = false;
                    } else {
                        r1 = true;
                    }
                }
            });
        } else {
            r1 = false;
            $('#login_err').text('Ошибка формата ввода -> от 6 до 16 символов: буквы, цифры,  _ ' + loginX);
        }
    });

    $('#pass2').blur(() =>{
        let pass1_x = $('#pass1').val();
        let pass2_x = $('#pass2').val();
        if (pass1_x != pass2_x) {
            $('#pass2_err').text('Пароли не совпадают!');
            r2 = false;
        } else {
            r2 = true;
        }
    })

    $('#submit').click(() => {
        if (r1 === true && r2 === true) {
            $('#form-1').attr('onsubmit', 'return true');
        } else {
            $('#form-1').attr('onsubmit', 'return false');
            alert('Форма содержит некорректные данные! \nОтправка данных заблокирована');
        }
    });

    $('#login').focus(() => {
        $('#login_err').text('');
    })

    $('#pass2').focus(() => {
        $('#pass2_err').text('');
    })

});
