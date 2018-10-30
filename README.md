# mod_auth_mellon tests
For httpd using  auth

<Location /auth>
          MellonEnable "auth"
          DirectoryIndex index.cgi
          AddHandler cgi-script .cgi
          Options ExecCGI
</Location>
