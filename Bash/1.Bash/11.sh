declare -A result

read n
row=63
column=100
for ((i=0; i < $row; i++)); do
    for ((j=0; j < $column; j++)); do
        result[$i,$j]="_"
    done
done
# create tree.
binaryTree(){
    if [ $4 -gt 0 ]; then
        for((i=0; i<$3; i++));do
            result[$(($1-$i)),$2]='1'
            result[$(($1-$3-$i)),$(($2-$i - 1))]='1'
            result[$(($1-$3-$i)),$(($2+$i + 1))]='1'
        done
        binaryTree $(($1-2*$3)) $(($2-$3)) $(($3/2)) $(($4-1))
        binaryTree $(($1-2*$3)) $(($2+$3)) $(($3/2)) $(($4-1))
    fi
}

# tree $1  $2   $3   $4
binaryTree 62 49 16 $n

for ((i=0; i < $row; i++)); do
    for ((j=0; j < $column; j++)); do
        printf  ${result[$i,$j]}
    done
    printf '\n'
done