#!/bin/bash
curl "$1" -sI | grep Allow: | cut -d":" -f2- | sed 's/^ *//'
