window.onload = function () {
    var switch_div = document.getElementById('switch_div')
    switch_div.addEventListener('click', function (e) {
        var ttarget = e.target;
        // console.log(ttarget);
        if (ttarget.id != 'switch') {
            return;
        }
        else {
            var card_num = ttarget.getAttribute('cardnumber');
            var full_path = 'card/' + card_num + '/relay_status';
            var txt_sts = ttarget.parentElement.previousElementSibling.firstChild.nextElementSibling;
            $.ajax(
                {
                    url: full_path,
                    method: 'get',
                    dataType: 'json',
                    success: function (response) {
                        if (response.card_status == true) {
                            ttarget.innerText = 'Дективировать карту';
                            ttarget.style.color = 'red';
                            txt_sts.innerHTML = response.card_status;
                        }
                        else {
                            ttarget.innerText = 'Активировать карту';
                            ttarget.style.color = 'green';
                            txt_sts.innerHTML = response.card_status;
                        }
                    }
                }
            );
            return false;
        }
    })
}




// function adress(card_num) {
//     var u = document.location.protocol + '//' + document.location.host + '/'
//     var uu = document.location.href.split('#!')[0]
//     if (u == uu) {
//         console.log('main')
//         f_u = document.location.href + 'card/' + card_num + '/relay_status/'
//         return f_u
//     }
//     else {
//         console.log('detail')
//         f_uu = document.location.href + 'relay_status/'
//         return f_uu
//     }
// }

