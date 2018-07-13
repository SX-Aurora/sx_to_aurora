!CDIR NODEP(A)
print *,a
!cdir NODEP,unroll=5, loopchg
print *,a
*cdir loopcnt=10
print *,a
!cdir on_adb(z), altcode=dep
print *,a
