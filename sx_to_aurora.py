#!/usr/bin/env python

# simple replacement of old SX directives into new SX aurora TSUBASA directives
# (c) Holger Berger NEC Deutschland GmbH 2018

# reads files from commandline, renames to <name>.bkup and writes new file under old name

import sys,re,os

# fortran !CDIR 
#         *CDIR
# C/C++   #pragma cdir

dirs = {
    "ASSERT":"",
    "ARRAYCOMB":"",
    "END ARRAYCOMB":"",
    "ASSUME":"",
    "NOASSUME":"",
    "DATA_PREFETCH":"",
    "EXPAND":"unroll",
    "NOEXPAND":"",
    "IEXPAND":"",
    "INLINE":"",
    "LOOPCNT":"loop_count",
    "NEXPAND":"",
    "NOIEXPAND":"",
    "NOMOVE":"nomove", 
    "MOVE":"move_unsafe",
    "NOMOVEDIV":"",
    "NOOVERLAP":"",
    "OVERLAP":"",
    "SHAPE":"",
    "UNROLL":"UNROLL",
    "NOUNROLL":"",
    "OUTERUNROLL":"outerloop_unroll",
    "NOOUTERUNROLL":"noouterloop_unroll",
    "ZCHECK":"",
    "NOZCHECK":"",
    "ALTCODE=DEP":"dependency_test",
    "ALTCODE=SHORTLOOP":"shortloop_reduction",
    "ALTCODE=SHORT":"loop_count_test",
    "NOALTCODE":"",
    "ASSOC":"",
    "NOASSOC":"",
    "COLLAPSE":"",
    "COMPRESS":"",
    "NOCOMPRESS":"",
    "DIVLOOP":"",
    "NODIVLOOP":"",
    "GTHREORDER":"",
    "NOGTHREORDER":"",
    "LISTVEC":"list_vector",
    "NOLISTVEC":"nolist_vector",
    "LOOPCHG":"",
    "NOLOOPCHG":"",
    "LSTVAL":"",
    "NOLSTVAL":"",
    "NEIGHBORS":"",
    "NONEIGHBORS":"",
    "NOCONFLICT":"",
    "NODEP":"ivdep",
    "NODEP":"ivdep",
    "ON_ADB":"",
    "SHORTLOOP":"shortloop",
    "SPARSE":"",
    "NOSPARSE":"",
    "SPLIT":"",
    "NOSPLIT":"",
    "VECTHRESHOLD=":"",
    "VECTOR":"",
    "NOVECTOR":"",
    "VERRCHK":"",
    "NOVERRCHK":"",
    "VLCHK":"",
    "NOVLCHK":"",
    "VOB":"vob",
    "NOVOB":"novob",
    "VOVERTAKE":"vovertake",
    "NOVOVERTAKE":"novovertake",
    "VPREFETCH":"",
    "VPREFETCH":"",
    "NOVPREFETCH":"",
    "VREG":"vreg",
    "ALLOC_ON_VREG":"",
    "VWORK=":"",
    "VWORKSZ=":"",
    "ARRAY":"",
    "CNCALL":"cncall",
    "CONCUR":"concurrent",
    "NOCONCUR":"noconcurrent",
    "INNER":"",
    "NOINNER":"",
    "SELECT":"",
    "SKIP":"",
    "SYNC":"",
    "NOSYNC":"",
    "THRESHOLD":"",
    "NOTHRESHOLD":""
}

for f in sys.argv[1:]:
    os.rename(f,f+".sxbkup")
    new=open(f,"w")
    for l in open(f+".sxbkup","r"):
        line=l[:-1]
        print >>new,line
        spu= re.split('[\s|,]',line.upper())
        sp= re.split('[\s|,]',line)
        if spu[0] in ["!CDIR","*CDIR"] or (sp[0]=="#pragma" and sp[1]=="cdir"):
            if sp[0]=="#pragma": prefix = "#pragma _NEC"
            else: prefix = "!NEC"
            for i in spu[1:]:
                if i in dirs and dirs[i]!="": print >>new, prefix,dirs[i]
                elif '=' in i:
                    m = re.match('(\S+)=(\d+)',i)
                    try:
                        print  >>new,prefix,
                        print  >>new,"%s(%s)" % (dirs[m.group(1)],m.group(2))
                    except KeyError:
                        pass
                elif '(' in i:
                    m = re.match('(\S+)\((\S+)\)',i)
                    try:
                        print  >>new,prefix,
                        print  >>new,"%s(%s)" % (dirs[m.group(1)],m.group(2))
                    except KeyError:
                        pass
    new.close()
