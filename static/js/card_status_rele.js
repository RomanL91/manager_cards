window.onload = function () {
    var a = document.getElementById('switch');
    var b = document.getElementById('st')
    a.onclick = function () {
        $.ajax(
            {
                url: "relay_status",
                method: 'get',
                dataType: 'json',
                success: function (response) {
                    if (response.card_status == true) {
                        b.innerHTML = response.card_status
                        a.innerText = 'Дективировать карту'
                        a.style.color = 'red'

                    }
                    else {
                        b.innerHTML = response.card_status
                        a.innerText = 'Активировать карту'
                        a.style.color = 'green'

                    }
                }
            }
        );
        return false;
    }
}