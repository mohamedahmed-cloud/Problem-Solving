read x
number=$(echo $x | bc -l)
printf "%.3f\n" $number 