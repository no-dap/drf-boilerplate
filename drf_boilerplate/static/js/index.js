$('document').ready(function () {
    let csrftoken = $.cookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    function drawQuestions (dataArray) {
        let parent = document.getElementById('questions-container');
        for (let i = 0; i < dataArray.length; i++) {
            let data = dataArray[i];
            let child = document.createElement('div');
            child.classList.add('question-container');
            let img = document.createElement('img');
            img.src = data['image'];
            child.appendChild(img);
            parent.appendChild(child);
        }
    }

    function flushQuestions() {
        let parent = document.getElementById('questions-container');
        parent.innerHTML = '';
    }

    function getQuestions(parameter) {
        $.ajax({
            url: '/api/v1/post/2/' + parameter,
            type: 'GET',
            success: function (res) {
                flushQuestions();
                drawQuestions(res['comments']);
            }
        })
    }

    getQuestions();


});