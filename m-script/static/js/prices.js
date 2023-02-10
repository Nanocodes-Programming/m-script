//// Get the CryptoCurrency Information from the API
jQuery.ajax({
  url: "https://min-api.cryptocompare.com/data/pricemultifull",
  data: "fsyms=BTC,ETH,DASH,LTC,DOGE,BCH&tsyms=USD",
  dataType : 'json',
}).done(function(data) 
{
  jQuery(".DASH_Live").html('$' + data.RAW.DASH.USD.PRICE);
  jQuery(".ETH_Live").html('$' + data.RAW.ETH.USD.PRICE);
  jQuery(".BTC_Live").html('$' + data.RAW.BTC.USD.PRICE);
  jQuery(".LTC_Live").html('$' + data.RAW.LTC.USD.PRICE);
  jQuery(".BCH_Live").html('$' + data.RAW.BCH.USD.PRICE);
  jQuery(".DOGE_Live").html('$' + data.RAW.DOGE.USD.PRICE.toFixed(4));
});