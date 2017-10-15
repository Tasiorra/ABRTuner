set term pngcairo dashed dl 2.0 font ",16"
set output 'avgbr_compare.png'
set xlabel 'Avg. bitrate'
set ylabel 'CDF'
plot 'cdf_bitrate_robustmpc.txt' u 2:1 with lines lw 3 t 'Default MPC', \
'cdf_bitrate_mpc-tuner.txt' u 2:1 with lines lw 3 t 'Tuner MPC'

reset
set term pngcairo dashed dl 2.0 font ",16"
set output 'rebuf_compare.png'
set xlabel 'Rebuf ratio'
set ylabel 'CDF'
set yrange [80:100]
set xrange [0:6]
set key bottom right
plot 'cdf_rebuf_robustmpc.txt' u 2:1 with lines lw 3 t 'Default MPC', \
'cdf_rebuf_mpc-tuner.txt' u 2:1 with lines lw 3 t 'Tuner MPC'
