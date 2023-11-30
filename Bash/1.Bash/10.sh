read n
for ((i = 0; i < $n; i++));do
    read enter
    values[$i]=$enter
done
x=0
for i in ${values[@]};do
    x=$((x + i))
done
prepare="$x/$n"
# echo $prepare
result=$(echo  $prepare | bc -l)

printf "%.3f\n" $result