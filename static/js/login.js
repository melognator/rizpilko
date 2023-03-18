var googleUser = {};

// loads gapi, redirects if already logged in
gapi.load('auth2', function() {
  gapi.auth2.init({
    client_id: '979938330838-7os91u2uobgrtcjfmb86g47ic2a06asm.apps.googleusercontent.com',
  }).then(function(){
    auth2 = gapi.auth2.getAuthInstance();
    attachSignin(document.getElementById('googleLoginButton'));
    if (auth2.isSignedIn.get() === true) {
      window.location.replace("https://rizpi.ezequielmelogno.repl.co/");
    }
  });
});

// sign in button
function attachSignin(element) {
  auth2.attachClickHandler(element, {},
      function(googleUser) {
        var id_token = googleUser.getAuthResponse().id_token;
        var profile = googleUser.getBasicProfile();
        // sends token, name and email
        $.ajax({
          url: '/auth',
          type: 'POST',
          data: JSON.stringify({
            token: id_token,
            nombre: profile.getName(),
            email: profile.getEmail()
          }),
          contentType: "application/json; charset=utf-8",
          traditional: true,
          success: function(data) {
            window.location.replace("https://rizpi.ezequielmelogno.repl.co/");
          }
        });
      }
  );
}
