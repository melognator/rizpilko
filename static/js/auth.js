var googleUser = {};

gapi.load('auth2', function() {
  gapi.auth2.init({
    client_id: '979938330838-7os91u2uobgrtcjfmb86g47ic2a06asm.apps.googleusercontent.com',
  }).then(function() {
    auth2 = gapi.auth2.getAuthInstance();
    if (auth2.isSignedIn.get() === false) {
      window.location.replace("https://rizpi.ezequielmelogno.repl.co/welcome");
    } else {
      // 
      // cargarTodo()
      var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
      // home
      $.ajax({
        url: '/usuario',
        type: 'POST',
        data: JSON.stringify({
          token: id_token
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          usuario = data
        }
      })
      .done(function() {
        $.ajax({
          url: '/home',
          type: 'POST',
          data: JSON.stringify({
            token: id_token
          }),
          contentType: "application/json; charset=utf-8",
          traditional: true,
          success: function(data) {
            home = data
            redirectHome()
          }
        })
      })
      .done(function() {
        $.ajax({
          url: '/categorias',
          type: 'POST',
          data: JSON.stringify({
            token: id_token
          }),
          contentType: "application/json; charset=utf-8",
          traditional: true,
          success: function(data) {
            categorias = data
          }
        })
      });

      // tareas
      $.ajax({
        url: '/tareas',
        type: 'POST',
        data: JSON.stringify({
          token: id_token
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          tareas = data
        }
      });

      // calendario
      $.ajax({
        url: '/calendario',
        type: 'POST',
        data: JSON.stringify({
          token: id_token
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          calendario = data
        }
      });

      // temporizador
      $.ajax({
        url: '/temporizador',
        type: 'POST',
        data: JSON.stringify({
          token: id_token
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          temporizador = data
        }
      });

      // configuracion
      $.ajax({
        url: '/configuracion',
        type: 'POST',
        data: JSON.stringify({
          token: id_token
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          configuracion = data
        }
      });

      // pomodoro
      $.ajax({
        url: '/pomodoro',
        type: 'POST',
        data: JSON.stringify({
          token: id_token
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          pomodoro = data
        }
      });

      // diario
      $.ajax({
        url: '/diario',
        type: 'POST',
        data: JSON.stringify({
          token: id_token
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          diario = data
        }
      });
      
    }
  });
});  
