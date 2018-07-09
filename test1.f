!CDIR NODEP(A)
!NEC ivdep(A)
print *,a
!cdir NODEP,unroll=5, loopchg
!NEC ivdep
!NEC UNROLL(5)
print *,a
*cdir loopcnt=10
!NEC loop_count(10)
print *,a
!cdir on_adb(z), altcode=dep
!NEC (Z)
!NEC dependency_test
print *,a
