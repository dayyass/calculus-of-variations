python calculus_of_variations/simplest_problem.py -L 'x_diff ** 2' -t0 0 -t1 1 -x0 0 -x1 1
python calculus_of_variations/boltz_problem.py -L 'x_diff ** 2 + 2 * x' -l 'x_t0 ** 2' -t0 0 -t1 1
python calculus_of_variations/isoperimetric_problem.py -f0 'x_diff ** 2' -t0 0 -t1 1 -x0 0 -x1 1 -f_list x -alpha_list 0
python calculus_of_variations/higher_derivatives_problem.py -n 2 -L 'x_diff_2 ** 2' -t0 0 -t1 1 -x0 0 -x1 0 -x0_array 0 -x1_array 1
python calculus_of_variations/multidimensional_problem.py -L 'x1_diff ** 2 + x2_diff ** 2' -t0 0 -t1 1 -x1_0 0 -x1_1 1 -x2_0 0 -x2_1 1
