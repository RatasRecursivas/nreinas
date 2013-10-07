#!/usr/bin/env python

import matplotlib.pyplot as plt
from benchy.api import Benchmark, BenchmarkSuite, BenchmarkRunner

# Estos eran los casos que nos pidieron en la tarea, ojala no tome tanto ...
casos = (8, 10, 15, 20, 30, 50, 70, 100)
# Using the benchy library
setup = 'from reinas import nreinas'
suite = BenchmarkSuite()
repeats = 1 # Nica corremos tantas veces CADA prueba

for n in casos:
    stmt = 'soluciones = nreinas(' + str(n) + '); print soluciones'
    benchmark = Benchmark(stmt, setup, name = 'nreinas(' + str(n) + ')', ncalls = repeats, repeat = repeats)
    suite.append(benchmark)

runner = BenchmarkRunner(benchmarks=suite, tmp_dir='.', name= 'Tarea de las n reinas')
n_benchs, results = runner.run()

runner.plot_absolute(results, horizontal=False, logy = True)
plt.savefig('%s.png' % runner.name) # bbox_inches='tight')

print runner.to_rst(results)
