function checkRefresh() {
    var req = new XMLHttpRequest();

    req.open('GET', '/fresh/', false);
    req.send();

    var refresher = JSON.parse(req.responseText).refresher;
    if (refresher) location.reload();

    doPoll();
}

function doPoll() {
    setTimeout(function() {
        checkRefresh();
    }, 1000);
}

doPoll();

