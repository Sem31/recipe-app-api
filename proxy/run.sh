#!/bin/sh


set -e

# environment substitut
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
cat /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
