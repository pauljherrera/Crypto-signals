strategy_config = {
    "destination_email" : ["luisomar242@gmail.com","cherpad78@gmail.com"] #list of mails

}


bittrex_config = {

    "interval" : 'fiveMin',       #intervals available on bittrex : oneMin, fiveMin ,thirtyMin, hour , Day
    "markets" : None,      #['BTC-LTC','BTC-ETH','BTC-XMR','BTC-CLOAK','BTC-VRC','BTC-AUR','BTC-PTC','BTC-CURE','BTC-DASH']
    "cron_intervals" : {"fiveMin": "*/5", 'thirtyMin' : '*/30', 'hour':'*/30 ','day':'*/1'}   #

}



volume_power_config = {

    "window" : 20,
    "threshold" : 10
}

Ema_crossover_config = {

    "slowEma" : 5,
    "fastEma" : 20

}