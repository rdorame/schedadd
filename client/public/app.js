'use strict';

var retail = angular.module("retail",['ngResource']);

angular
    .module('SampleApplication', [
        'base64',
        'appRoutes',
        'retail',
        'ngCookies',
    ])
    .config(function($httpProvider, $base64) {
        var auth = $base64.encode("gabriel:password1234");
        $httpProvider.defaults.headers.common['Authorization'] = 'Basic ' + auth;
    })
    .run( function run( $http, $cookies ){

    // For CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');
});
