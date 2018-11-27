<?php
    // This is just an example to illustrate the documentation
    // Prefer the PHP SDK

    $app_id = '5baa0c31c8bd0013008f72cc';
    $app_secret = 'MFD8y8bW6CZ4bmoVud70TscBsSfzWke';
    $username = '826413876@qq.com';
    $password = 'N@tatmo0';
    $scope = 'read_station read_thermostat write_thermostat'; // all scopes are selected.
    $token_url = "https://api.netatmo.com/oauth2/token";
    $postdata = http_build_query(
        array(
            'grant_type' => "password",
            'client_id' => $app_id,
            'client_secret' => $app_secret,
            'username' => $username,
            'password' => $password,
            'scope' => $scope
        )
    );

    $opts = array('http' =>
    array(
        'method'  => 'POST',
        'header'  => 'Content-type: application/x-www-form-urlencoded',
        'content' => $postdata
    )
    );

    $context  = stream_context_create($opts);

    $response = file_get_contents($token_url, false, $context);
    $params = null;
    $params = json_decode($response, true);

    $api_url = "https://api.netatmo.com/api/getuser?access_token="
    . $params['access_token'];

    $user = json_decode(file_get_contents($api_url));
    echo("It worked. Hello <".$user->body->mail.">\n");
	echo("Access_token is <".$params['access_token'].">\n");

    ?>