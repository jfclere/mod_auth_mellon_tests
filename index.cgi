#!/usr/bin/bash

echo "Status: 200 OK"
echo "Content-Type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Thanks Welcome Home</title>'
echo '</head>'
echo '<body>'
echo 'Not FOUND'
echo '</br>'

for a in `env | grep MELLON`
do
  echo $a
  echo '</br>'
done

echo '</br>'
echo '</body>'
echo '</html>'

exit 0
