function showTimer() {
    $(".minutes").html(minutes);
    if (seconds < 10) {
        $(".seconds").html("0" + seconds);
    }
    else {
        $(".seconds").html(seconds);
    }
    console.log(minutes + seconds);
}

function stopTimer() {
    timerFlag = 0;
    pauseFlag = 0;
    minutes = 25;
    seconds = 0;
    showTimer();
    $(".start-stop").html("Iniciar");
    $(".pause-area").hide();
    clearTimeout(t);
}

function startTimer() {
    timerFlag = 1;
    pauseFlag = 0;
    updateTimer();
    $(".start-stop").html("Pausar");
    $(".pause-area").show();
    $(".pause").text("Pausar");
    $(".start-stop-area").hide();
}

function pauseTimer() {
    pauseFlag = 1;
    clearTimeout(t);
    $(".start-stop-area").show();
    $(".pause").html("Resumo");
}

function resumeTimer() {
    pauseFlag = 0;
    updateTimer();
    $(".pause").html("Pausar");
    $(".start-stop-area").hide();
}

function updateTimer() {
    if (minutes == 0 && seconds == 0) {
        console.log("Store to databse and reset");
        // calling route to store date_time
        $.getJSON('/send_datetime', function () { });
        minutes = 25;
        seconds = 0;
        showTimer();
    }
    else if (seconds == 0) {
        minutes -= 1;
        seconds = 59;
        showTimer();
        t = setTimeout(updateTimer, 1000)
    }
    else {
        seconds -= 1;
        showTimer();
        t = setTimeout(updateTimer, 1000)
    }
}