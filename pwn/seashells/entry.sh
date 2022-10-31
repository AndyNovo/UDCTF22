#!/bin/bash

while :
do
    su -c "socat TCP4-listen:34347,reuseaddr,fork EXEC:/pwn/seashells" - pwnuser
done
