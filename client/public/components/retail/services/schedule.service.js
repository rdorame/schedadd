retail
  .factory('Schedule', function($resource) {
      return $resource(
          'http://localhost:8000/schedules/:id/',
          {},
          {
              'query': {
                  method: 'GET',
                  isArray: true,
                  headers: {
                      'Content-Type':'application/json'
                  }
              }
          },
          {
              stripTrailingSlashes: false
          }
      );
  });
