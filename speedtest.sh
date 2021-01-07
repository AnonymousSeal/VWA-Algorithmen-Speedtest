# speedtest.sh
#!/usr/bin/env bash

inputfile="primeproducts.txt"
prefix="MacBook"
method="basic" #ecm, mpqs, basic

len=$(cat $inputfile | wc -l)

i=0
cat $inputfile | while read line; do
  case $method in
  "ecm")
    source venv2/bin/activate
    { time python -m primefac -m=ecm $line; } 2>&1 | grep -e $line -e real >> ecm.txt;;
  "mpqs")
    source venv2/bin/activate
    { time python -m primefac -m=mpqs $line; } 2>&1 | grep -e $line -e real >> mpqs.txt;;
  "basic")
    source venv3/bin/activate
    { time python basic_algorithm.py -n $line; } 2>&1 | grep -e $line -e real >> basic.txt;;
  *)
    echo "method $method not found. Valid options: ecm, basic, mpqs";;
  esac
  i=$(($i+1))
  echo "[$i/${len//[^0-9]/}]"
done
