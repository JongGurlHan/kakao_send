
// Disable form submissions if there are invalid fields
(function () {
    'use strict';
    window.addEventListener('load', function () {
        // Get the forms we want to add validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

//전송시간 체크
function sendTimeCheck() {
    if (document.getElementById('timeReserve').checked) {
        document.getElementById('ifReserve').style.display = 'block';
    }
    else document.getElementById('ifReserve').style.display = 'none';

}
$(function () {
    $('#datetimepicker1').datetimepicker();
});




var btnSet = 0; // 버튼갯수

function tplAddBtn() {
    // 버튼추가하기
    var tplCode = $('#tplAddBtnList').val();
    if (tplCode && btnSet < 5) {
        var tplAreaTemp = ''
        var tplAreaTempTitle = '<button type="button" class="tpl_btn_del" onclick="removeBtn($(this))"><img src="../static/images/remove.png" width="18" alt="remove"></button><button type="button" class="up" onclick="isBtnUp($(this), true)"><i class="bi bi-arrow-down-circle"></i></button><button type="button" class="down" onclick="isBtnUp($(this), false)"><img src="../static/images/down.png" alt="down"  width="18"></button></h2>'
        tplAreaTempTitle += '<input type="text" class="form-control" name="btn_name" placeholder="버튼명을 입력하세요.(최대 14자)" onkeyup="updateBtnArea($(this), \'title\')" onchange="setVariable()" />'
        switch (tplCode) {
            case 'WL':
                tplAreaTemp += '<fieldset class="' + tplCode + '"><h5>웹링크' + tplAreaTempTitle
                tplAreaTemp += '<label>링크(모바일웹)</label><input type="text" class="form-control" name="linkMo" placeholder="URL을 입력하세요" onchange="checkUrl($(this))"/><label>링크(PC)</label><input type="text" class="form-control" name="linkPc" placeholder="URL을 입력하세요" onchange="checkUrl($(this))" /></fieldset>'
                break;
            case 'AL':
                tplAreaTemp += '<fieldset class="' + tplCode + '"><h>앱링크' + tplAreaTempTitle
                tplAreaTemp += '<label>링크(안드로이드)</label><input type="text" name="linkAnd" placeholder="링크 주소를 입력하세요" onchange="checkUrl($(this))"/><label>링크(아이폰)</label><input type="text" name="linkIos" placeholder="링크 주소를 입력하세요" onchange="checkUrl($(this))"/></fieldset>'
                break;
            case 'BK':
                tplAreaTemp += '<fieldset class="' + tplCode + '"><h5>봇키워드' + tplAreaTempTitle + '</fieldset>'
                break;
            case 'MD':
                tplAreaTemp += '<fieldset class="' + tplCode + '"><h5>메세지전달' + tplAreaTempTitle + '</fieldset>'
                break;
        }
        btnSet++;
        $('#btnArea').prepend(tplAreaTemp);
        updateBtnArea(tplCode, 'new');
        resetMoveBtn();
    } else {
        if (btnSet == 5) {
            alert("버튼은 최대 5개까지만 생성 가능합니다.");
        } else {
            alert('버튼타입을 선택하세요.');
        }
    }
}

function removeBtn(el) {
    // 버튼 지우기
    btnSet--;
    resetMoveBtn();
    updateBtnArea(el, 'del');

}

function isBtnUp(el, type) {
    // 버튼넣기 위치변경
    var thisIndex = el.parent().parent().index()
    if (type) {
        // 올리기
        $('#btnArea').children().eq(thisIndex - 1).insertAfter(el.parent().parent())
        updateBtnArea(thisIndex, 'up');
    } else {
        // 내리기
        $('#btnArea').children().eq(thisIndex + 1).after(el.parent().parent())
        updateBtnArea(thisIndex, 'down');
    }
    // 정렬하기
    resetMoveBtn();
}

function resetMoveBtn() {
    // 버튼넣기 이동버튼 초기화시키기
    $('#btnArea fieldset').each(function (index, item) {
        $(item).find('button').show();
        if (index == 0) {
            $(item).find('.up').hide();
        }
        if (index == (btnSet - 1)) {
            $(item).find('.down').hide();
        }
    });
}

function updateBtnArea(el, type) {
    // 버튼 업데이트 반영하기
    var btnArea = $('#friendBtnArea');
    if (type == 'new') {
        // 버튼추가시 화면반영
        btnArea.prepend('<span>버튼명</span>');
    } else if (type == 'title') {
        // 텍스트 입력시 바인딩
        var thisTitle = el.val();
        if (thisTitle.length > 14) {
            el.val(thisTitle.substring(0, 14));
            return false;
        }
        var thisIndex = el.parent().index();
        if (thisTitle) {
            btnArea.children().eq(thisIndex).text(thisTitle);
        } else {
            btnArea.children().eq(thisIndex).text('버튼명');
        }
    } else if (type == 'del') {
        // 버튼 삭제시 화면반영하기
        var thisIndex = el.parent().parent().index();
        el.parent().parent().remove();
        btnArea.children().eq(thisIndex).remove();
    } else if (type == 'up') {
        // 올리기
        btnArea.children().eq(el - 1).insertAfter(btnArea.children().eq(el));
    } else if (type == 'down') {
        // 내리기
        btnArea.children().eq(el + 1).after(btnArea.children().eq(el));
    }
}