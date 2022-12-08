#--- Day 7: No Space Left On Device ---

You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

```
$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
```

Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

```
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
````

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

```
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
```

Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

- The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
- The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
- Directory d has total size 24933642.
- As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
- To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?



     /
  a         b
c  d     e     f
     g     h  i j 









/vrvl 210089
/vrvl/pnfv 183315
/ldqc 468944
/ldqc/vhdgcsw 362227
/ldqc/vhdgcsw/rnz 0
/ldqc/vhdgcsw/rnz/zmflq 174075      
/ldqc/vhdgcsw/rnz/cmsccq 356488     
/ldqc/vhdgcsw/rnz/cmsccq/twqt 109250
/ldqc/vhdgcsw/rnz/chfccv 175830     
/ldqc/vhdgcsw/rfzrwc 0
/ldqc/vhdgcsw/rfzrwc/lcgv 285108
/ldqc/vhdgcsw/rfzrwc/lcgv/glqrj 283123
/ldqc/vhdgcsw/rfzrwc/lcgv/dlpng 195950
/ldqc/vhdgcsw/flhbhzlt 282258
/ldqc/tqwpmw 92747
/ldqc/rmljszcj 172566
/ldqc/rmljszcj/wqdlv 272345
/ldqc/rmljszcj/jnstrbj 750372
/ldqc/qtdlb 0
/ldqc/qtdlb/wqdlv 0
/ldqc/qtdlb/wqdlv/qccsnjd 333710
/ldqc/qtdlb/nsjlcmfz 53472
/ldqc/qtdlb/nsjlcmfz/qvpj 150929
/ldqc/qtdlb/gjpmcvwp 0
/ldqc/qtdlb/gjpmcvwp/cjjdzcwm 233873
/ldqc/jgbsw 361940
/ldqc/jgbsw/rfzrwc 57417
/ldqc/jgbsw/rfzrwc/gvqrwgrs 0
/ldqc/jgbsw/rfzrwc/gvqrwgrs/sgfltf 204207
/ldqc/jgbsw/rfzrwc/fcvfw 279614
/ldqc/jgbsw/cfdljgh 261471
/ldqc/jclb 0
/ldqc/jclb/zmflq 305021
/ldqc/jclb/vpfggv 569821
/ldqc/jclb/vpfggv/vvp 425303
/ldqc/jclb/vpfggv/vvp/nmbfwc 160971
/ldqc/jclb/vpfggv/vvp/nmbfwc/rfzrwc 257264
/ldqc/jclb/vpfggv/vvp/nmbfwc/fvh 444278
/ldqc/jclb/vpfggv/vvp/fsw 111889
/ldqc/jclb/vpfggv/vvp/fsw/rfzrwc 282718
/ldqc/jclb/vpfggv/tpmnhdc 0
/ldqc/jclb/vpfggv/tpmnhdc/nmbfwc 682056
/ldqc/jclb/vpfggv/tpmnhdc/nmbfwc/zppcvq 112537
/ldqc/jclb/vpfggv/tpmnhdc/nmbfwc/zmflq 124906
/ldqc/jclb/vpfggv/tpmnhdc/nmbfwc/lcgv 0
/ldqc/jclb/vpfggv/tpmnhdc/nmbfwc/lcgv/wths 120313
/ldqc/jclb/vpfggv/tpmnhdc/lcllz 210654
/ldqc/jclb/vpfggv/tpmnhdc/lcllz/zmflq 284536
/ldqc/jclb/vpfggv/tpmnhdc/lcllz/flwws 222222
/ldqc/jclb/vpfggv/tpmnhdc/fjwr 293243
/ldqc/jclb/vpfggv/scw 245681
/ldqc/jclb/vhjwtq 0
/ldqc/jclb/vhjwtq/qgqbrv 176900
/ldqc/jclb/pbb 0
/ldqc/jclb/pbb/zmflq 0
/ldqc/jclb/pbb/zmflq/wqdlv 799393
/ldqc/jclb/pbb/zmflq/wqdlv/rfzrwc 0
/ldqc/jclb/pbb/zmflq/wqdlv/rfzrwc/lmcg 32819
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv 633578
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zmflq 894852
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zmflq/wqgngf 37020
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zmflq/wqgngf/ldwgr 260404
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zmflq/wqgngf/jpgfsgd 0
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zmflq/wqgngf/jpgfsgd/qbrwz 199057
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zmflq/wqgngf/jpgfsgd/lcgv 284229
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zmflq/wqgngf/jpgfsgd/lcgv/wsjs 111635
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/zjr 224145
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/ppwcgc 249714
/ldqc/jclb/pbb/zmflq/wqdlv/jrqsqrv/ppwcgc/cvnd 248610
/ldqc/jclb/pbb/zmflq/wqdlv/dqpgtmdl 268413
/ldqc/jclb/pbb/zmflq/tntnjg 20210
/ldqc/jclb/pbb/zmflq/qsnfzp 241308
/ldqc/jclb/pbb/zmflq/nbbv 173445
/ldqc/jclb/pbb/zmflq/nbbv/wqdlv 293155
/ldqc/jclb/pbb/zmflq/mpmcghz 235248
/ldqc/jclb/pbb/zmflq/lcgv 205204
/ldqc/jclb/pbb/zmflq/lcgv/zmflq 102538
/ldqc/jclb/pbb/zmflq/lcgv/rnrmhfz 19759
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc 848968
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/zmflq 479520
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/wqmdw 0
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/wqmdw/zmrdf 0
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/wqmdw/zmrdf/qqgw 58554
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/rcvwcbfd 0
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/rcvwcbfd/wgp 81030
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/rcvwcbfd/vtrtt 138009
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/rcvwcbfd/vtrtt/ztsvzpn 51632
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/lcgv 0
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/lcgv/pqttlp 405302
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/lcgv/pqttlp/bgvhcgfn 228291
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/lcgv/lcgv 0
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/lcgv/lcgv/bpjzg 99853
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/bnsgzwhn 9892
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/bnsgzwhn/zmflq 448065
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/bnsgzwhn/wpwmflr 274142
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/bnsgzwhn/wpwmflr/srnm 0
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/bnsgzwhn/wpwmflr/srnm/rvvtgr 164604
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/bnsgzwhn/wpwmflr/rfzrwc 161517
/ldqc/jclb/pbb/zmflq/lcgv/rfzrwc/bnsgzwhn/wpwmflr/rfzrwc/zbhgwsd 43750
/ldqc/jclb/pbb/zmflq/lcgv/nmbfwc 0
/ldqc/jclb/pbb/zmflq/lcgv/nmbfwc/rwgscjbv 242899
/ldqc/jclb/pbb/zmflq/lcgv/nmbfwc/fgctdds 205015
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr 234510
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/wqdlv 103876
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/mczs 186843
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/mczs/thbwb 146494
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/mczs/pjm 0
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/mczs/pjm/wqdlv 201647
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv 0
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv/rfzrwc 156985
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv/rfzrwc/wqdlv 104474
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv/rfzrwc/wptr 46279
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv/rfzrwc/mqp 142621
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv/rfzrwc/jjl 124893
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv/rfzrwc/jjl/jrjjr 243753
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/lcgv/pwhl 125371
/ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr/hmjzlr 268342
/ldqc/jclb/pbb/zmflq/lcgv/jncrbhc 450028
/ldqc/jclb/pbb/zmflq/lcgv/hbzzf 36018
/ldqc/jclb/pbb/zmflq/lcgv/dzz 634406
/ldqc/jclb/pbb/zmflq/lcgv/dzz/sjrb 233530
/ldqc/jclb/pbb/zmflq/lcgv/dzz/rsdw 0
/ldqc/jclb/pbb/zmflq/lcgv/dzz/rsdw/lcgv 37080
/ldqc/jclb/pbb/zmflq/lcgv/dzz/cvvdv 375773
/ldqc/jclb/pbb/zmflq/hnrnldw 102631
/ldqc/jclb/pbb/wqdlv 146479
/ldqc/jclb/pbb/wqdlv/wqdlv 520160
/ldqc/jclb/pbb/wqdlv/wqdlv/swdnss 0
/ldqc/jclb/pbb/wqdlv/wqdlv/swdnss/bmrzhjs 272987
/ldqc/jclb/pbb/wqdlv/wqdlv/ppsm 705186
/ldqc/jclb/pbb/wqdlv/wqdlv/ppsm/ssggblm 295510
/ldqc/jclb/pbb/wqdlv/wqdlv/ppsm/ggjnl 45841
/ldqc/jclb/pbb/wqdlv/wqdlv/chnpddzn 256977
/ldqc/jclb/pbb/wqdlv/wqdlv/chnpddzn/wqdlv 6565
/ldqc/jclb/pbb/wqdlv/tgmqnq 487178
/ldqc/jclb/pbb/wqdlv/tgmqnq/lcgv 733438
/ldqc/jclb/pbb/wqdlv/tgmqnq/lcgv/rplqnt 119893
/ldqc/jclb/pbb/wqdlv/tgmqnq/lcgv/ljt 11842
/ldqc/jclb/pbb/wqdlv/tgmqnq/lcgv/dzfglmz 220883
/ldqc/jclb/pbb/wqdlv/nmbfwc 681992
/ldqc/jclb/pbb/wqdlv/nmbfwc/zvnrwfhn 242009
/ldqc/jclb/pbb/wqdlv/nmbfwc/wqdlv 69742
/ldqc/jclb/pbb/wqdlv/nmbfwc/jtn 23555
/ldqc/jclb/pbb/wqdlv/hrghbhj 723504
/ldqc/jclb/pbb/wqdlv/hrghbhj/zfjjncvd 59841
/ldqc/jclb/pbb/wqdlv/hrghbhj/tsdjgt 182740
/ldqc/jclb/pbb/wqdlv/hrghbhj/lcgv 30459
/ldqc/jclb/pbb/wqdlv/hrghbhj/lcgv/wqdlv 78475
/ldqc/jclb/pbb/wqdlv/fgggwt 264892
/ldqc/jclb/hnlrtpbz 665319
/ldqc/jclb/dtmtvbw 0
/ldqc/jclb/dtmtvbw/zmflq 223201
/ldqc/jclb/dtmtvbw/hzlhz 50958
/ldqc/jclb/dtmtvbw/bjthn 272777
/ldqc/jclb/bnz 199447
/ldqc/gqb 334869
/ldqc/gqb/vznbng 234790
/ldqc/gqb/lvwpqs 436217
/ldqc/gqb/jtf 337721
/ldqc/dvshtm 96767
/ldqc/dvshtm/qdmmpq 0
/ldqc/dvshtm/qdmmpq/vgrdpbg 0
/ldqc/dvshtm/qdmmpq/vgrdpbg/wqdlv 130393
/ldqc/dvshtm/qdmmpq/lzgwflt 148651
/ldqc/dvshtm/lcgv 82949
/ldqc/dnzfqzwv 0
/ldqc/dnzfqzwv/tqv 700472
/lcgv 0
/lcgv/znmzg 242260
/lcgv/vwhf 116134
/lcgv/vwhf/wszvqd 0
/lcgv/vwhf/wszvqd/lcpvwdq 236526
/lcgv/vwhf/wszvqd/lcpvwdq/lwhq 398415
/lcgv/vwhf/wszvqd/bhhtbv 248604
/lcgv/vwhf/wszvqd/bhhtbv/nmbfwc 83799
/lcgv/vwhf/wszvqd/bhhtbv/fbh 256295
/lcgv/vwhf/mrlvtb 40003
/lcgv/vwhf/lcgv 746860
/lcgv/vwhf/fcwzw 59717
/lcgv/vwhf/bgtgqzz 524013
/lcgv/vwhf/bgtgqzz/smhhzq 137259
/lcgv/vwhf/bgtgqzz/dzpjg 696077
/lcgv/lnztfr 468469
/lcgv/grldv 145761
/lcgv/grldv/wqdlv 253966
/lcgv/cthtlwds 0
/lcgv/cthtlwds/tfwgg 668342
/lcgv/cthtlwds/tfwgg/svvz 120895
/lcgv/cthtlwds/tfwgg/lcgv 182616
/lcgv/cthtlwds/tfwgg/gng 44313
/lcgv/cthtlwds/tfwgg/ddnfmsjc 0
/lcgv/cthtlwds/tfwgg/ddnfmsjc/lcgv 47252
/lcgv/cthtlwds/tfwgg/ddnfmsjc/hwmcsdvt 208912
/lcgv/cthtlwds/dghvw 107090
/jtrbrcjl 0
/jtrbrcjl/whqb 209584
/jtrbrcjl/nmbfwc 499010
/hmnpr 178623
/fwbjchs 176267