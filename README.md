# mod_auth_mellon tests
For httpd using  auth
```
LoadModule cgid_module modules/mod_cgid.so
<Location /auth>
          MellonEnable "auth"
          DirectoryIndex index.cgi
          AddHandler cgi-script .cgi
          Options ExecCGI
</Location>
```
