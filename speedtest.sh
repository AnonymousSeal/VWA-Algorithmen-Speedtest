#!/usr/bin/env bash

len=$(cat primeproducts.txt | wc -l)

i=0
cat primeproducts.txt | while read line; do
  { time python -m primefac -m=ecm $line; } 2>&1 | grep -e $line -e real >> ecm.txt;
  { time python -m primefac -m=mpqs $line; } 2>&1 | grep -e $line -e real >> mpqs.txt;
  i=$(($i+1))
  echo "[$i/${len//[^0-9]/}]"
done
