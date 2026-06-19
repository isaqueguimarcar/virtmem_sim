#!/bin/bash

echo "trace,frames,algoritmo,page_faults,pages_written" > resultados.csv

for trace in traces/*.trace
do
    for frames in 2 4 8 16 32 64
    do
        for alg in random fifo lru sc lfu mfu
        do
            output=$(./simulador "$trace" $frames $alg)

            faults=$(echo "$output" | grep "page faults" | awk '{print $6}')
            writes=$(echo "$output" | grep "written on disk" | awk '{print $8}')

            echo "$(basename "$trace"),$frames,$alg,$faults,$writes" >> resultados.csv

            echo "OK -> $(basename "$trace") | Frames=$frames | Alg=$alg"
        done
    done
done

echo
echo "Execução concluída!"
echo "Arquivo gerado: resultados.csv"