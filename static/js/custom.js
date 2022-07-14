

$("#monthly").change(function () {
    let monthly = $("#monthly").val();
    let price = $("#service_price").val();
    let total = monthly * price;
    if (monthly == 12) {
        total = Math.round(total * 0.9)
    }
    $("#price").val(total);
    let
});