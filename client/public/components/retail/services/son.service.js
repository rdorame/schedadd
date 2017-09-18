retail
  .factory('Son', function($resource) {
      return $resource(
          'http://localhost:8000/sons/:id/',
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
