#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
