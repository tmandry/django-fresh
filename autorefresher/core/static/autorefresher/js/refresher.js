function checkRefresh() {
    var req = new XMLHttpRequest();

    req.open('GET', '/refresher/', false);
    req.send();

    var refresh = JSON.parse(req.responseText).refresh;
    if (refresh) location.reload();

    doPoll();
}

function doPoll() {
    setTimeout(function() {
        checkRefresh();
    }, 3000);
}

doPoll();

