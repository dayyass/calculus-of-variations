# simplest problem
python calculus_of_variations/simplest_problem.py -L "x_diff ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "1"
python calculus_of_variations/simplest_problem.py -L "x_diff ** 2 + t * x" -t0 "0" -t1 "1" -x0 "0" -x1 "0"
python calculus_of_variations/simplest_problem.py -L "t * x_diff ** 2" -t0 "1" -t1 "E" -x0 "0" -x1 "1"
python calculus_of_variations/simplest_problem.py -L "x_diff ** 2 + x_diff * x + 12 * t * x" -t0 "0" -t1 "1" -x0 "0" -x1 "0"
python calculus_of_variations/simplest_problem.py -L "x_diff ** 2 - t ** 2 * x" -t0 "0" -t1 "1" -x0 "0" -x1 "0"

# boltz problem
python calculus_of_variations/boltz_problem.py -L "x_diff ** 2 + 2 * x" -l "x_t0 ** 2" -t0 "0" -t1 "1"
python calculus_of_variations/boltz_problem.py -L "x_diff ** 2 - x" -l "-x_t1 ** 2 / 2" -t0 "0" -t1 "1"
python calculus_of_variations/boltz_problem.py -L "t ** 2 * x_diff ** 2" -l "-2 * x_t0 + x_t1 ** 2" -t0 "1" -t1 "2"
python calculus_of_variations/boltz_problem.py -L "2 * (t * x_diff ** 2 + x_diff * x)" -l "3 * x_t0 ** 2 - x_t1 ** 2 - 4 * x_t1" -t0 "1" -t1 "E"

# isoperimetric problem
python calculus_of_variations/isoperimetric_problem.py -f0 "x_diff ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "1" -f_list "x" -alpha_list "0"
python calculus_of_variations/isoperimetric_problem.py -f0 "x_diff ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "1" -f_list "t * x" -alpha_list "0"
python calculus_of_variations/isoperimetric_problem.py -f0 "x_diff ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "0" -f_list "x, t * x" -alpha_list "1, 0"
python calculus_of_variations/isoperimetric_problem.py -f0 "x_diff ** 2" -t0 "0" -t1 "pi" -x0 "1" -x1 "-1" -f_list "x * cos(t)" -alpha_list "pi / 2"
python calculus_of_variations/isoperimetric_problem.py -f0 "t ** 2 * x_diff ** 2" -t0 "1" -t1 "2" -x0 "1" -x1 "2" -f_list "t * x" -alpha_list "7 / 3"

# higher derivatives problem
python calculus_of_variations/higher_derivatives_problem.py -n "2" -L "x_diff_2 ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "0" -x0_array "0" -x1_array "1"
python calculus_of_variations/higher_derivatives_problem.py -n "2" -L "x_diff_2 ** 2 - 48 * x" -t0 "0" -t1 "1" -x0 "1" -x1 "0" -x0_array "-4" -x1_array "0"
python calculus_of_variations/higher_derivatives_problem.py -n "3" -L "x_diff_3 ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "1" -x0_array "0, 0" -x1_array "3, 6"
python calculus_of_variations/higher_derivatives_problem.py -n "4" -L "x_diff_4 ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "1" -x0_array "0, 0, 0" -x1_array "3, 6, 10"

# multidimensional problem
python calculus_of_variations/multidimensional_problem.py -L "x1_diff**2 + x2_diff**2" -t0 "0" -t1 "1" -x1_0 "0" -x1_1 "1" -x2_0 "0" -x2_1 "1"
python calculus_of_variations/multidimensional_problem.py -L "x1_diff ** 2 + x2_diff ** 2" -t0 "0" -t1 "1" -x1_0 "0" -x1_1 "1" -x2_0 "1" -x2_1 "E"
python calculus_of_variations/multidimensional_problem.py -L "x2 ** 2 + x1_diff ** 2 + x2_diff ** 2" -t0 "0" -t1 "1" -x1_0 "0" -x1_1 "1" -x2_0 "1" -x2_1 "E"
python calculus_of_variations/multidimensional_problem.py -L "x1_diff * x2_diff - x1 * x2" -t0 "0" -t1 "pi / 2" -x1_0 "0" -x1_1 "1" -x2_0 "1" -x2_1 "0"
python calculus_of_variations/multidimensional_problem.py -L "2 * x1 + x2 ** 2 + x1_diff ** 2 + x2_diff ** 2" -t0 "0" -t1 "1" -x1_0 "0" -x1_1 "0.5" -x2_0 "1" -x2_1 "exp(-1)"
