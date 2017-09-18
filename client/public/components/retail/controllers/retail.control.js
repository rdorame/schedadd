retail
    .controller('RetailController', function($scope, Son, User, Schedule) {
        Son.query().$promise.then(function(data) {
            $scope.sons = data;
        });
        User.query().$promise.then(function(data) {
            $scope.users = data;
        });
        Schedule.query().$promise.then(function(data) {
            $scope.schedules = data;
        });
});
