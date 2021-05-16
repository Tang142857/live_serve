var diaryList = document.getElementById("diaryList");
var addDiaryButton = document.getElementById("addDiary");

var addDiary = function() {
    var item = "<div class=\"subPage\"><a href=\"/pages/diary.html\" target=\"_blank\" class=\"sub_intrance\">Diary -></a></div>";
    diaryList.innerHTML = diaryList.innerHTML + item;
}

addDiaryButton.onclick = addDiary;