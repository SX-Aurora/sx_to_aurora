#pragma cdir NODEP(A)
#pragma _NEC ivdep(A)
#pragma cdir NODEP,unroll=5, loopchg
#pragma _NEC ivdep
#pragma _NEC UNROLL(5)
#pragma cdir loopcnt=10
#pragma _NEC loop_count(10)
#pragma cdir on_adb(z), altcode=dep
#pragma _NEC (Z)
#pragma _NEC dependency_test
