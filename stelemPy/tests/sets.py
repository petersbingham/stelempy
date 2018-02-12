SETS_1_IN = [[1.01,2.,3.,4.],[5.,1.001,6.,7.],[8.,9.,1.0001,10.]]

SETS_1_01_FOUT1 = [([], [], []), 
                ([1.001], [[(1, 1), (0, 0)]], ['NEW']), 
                ([1.0001], [[(2, 2), (1, 1)]], ['REP'])]
SETS_1_01_COUT1 = [{1: [1.001, [(1, 1), (0, 0)], 'NEW'], 2: [1.0001, [(2, 2), (1, 1)], 'REP']}]
SETS_1_01_COUT1_PRE = [{0: [1.01, None, 'PRE'], 1: [1.001, [(1, 1), (0, 0)], 'NEW'], 2: [1.0001, [(2, 2), (1, 1)], 'REP']}]
SETS_1_01_COUT1_POST = [{0: [1.01, None, 'PRE'], 1: [1.001, [(1, 1), (0, 0)], 'NEW'], 2: [1.0001, [(2, 2), (1, 1)], 'REP']}]

SETS_1_01_FOUT2 = [([], [], []), 
                ([], [], []), 
                ([1.0001], [[(2, 2), (1, 1), (0, 0)]], ['NEW'])]
SETS_1_01_COUT2 = [{2: [1.0001, [(2, 2), (1, 1), (0, 0)], 'NEW']}]
SETS_1_01_COUT2_PRE = [{0: [1.01, None, 'PRE'], 1: [1.001, None, 'PRE'], 2: [1.0001, [(2, 2), (1, 1), (0, 0)], 'NEW']}]
SETS_1_01_COUT2_POST = [{0: [1.01, None, 'PRE'], 1: [1.001, None, 'PRE'], 2: [1.0001, [(2, 2), (1, 1), (0, 0)], 'NEW']}]


SETS_2_IN = [[1.01,2.01,3.,4.,5],[6.,2.001,1.001,7.,8.],
             [9.,10.,1.0001,11.,2.0001],[12.,13.,1.00001,14.,15.]]
SETS_2_01_FOUT1 = [([], [], []), 
               ([2.001, 1.001], [[(1, 1), (0, 1)], [(1, 2), (0, 0)]], ['NEW', 'NEW']), 
               ([2.0001, 1.0001], [[(2, 4), (1, 1)], [(2, 2), (1, 2)]], ['REP', 'REP']), 
               ([2.0001, 1.00001], [[(2, 4), (1, 1)], [(3, 2), (2, 2)]], ['LOST', 'REP'])]
SETS_2_01_COUT1 = [{1: [2.001, [(1, 1), (0, 1)], 'NEW'], 2: [2.0001, [(2, 4), (1, 1)], 'REP'], 3: [2.0001, None, 'LOST']}, 
                   {1: [1.001, [(1, 2), (0, 0)], 'NEW'], 2: [1.0001, [(2, 2), (1, 2)], 'REP'], 3: [1.00001, [(3, 2), (2, 2)], 'REP']}]
SETS_2_01_COUT1_PRE = [{0: [2.01, None, 'PRE'], 1: [2.001, [(1, 1), (0, 1)], 'NEW'], 2: [2.0001, [(2, 4), (1, 1)], 'REP'], 3: [2.0001, None, 'LOST']}, 
                       {0: [1.01, None, 'PRE'], 1: [1.001, [(1, 2), (0, 0)], 'NEW'], 2: [1.0001, [(2, 2), (1, 2)], 'REP'], 3: [1.00001, [(3, 2), (2, 2)], 'REP']}]
SETS_2_01_COUT1_POST = [{0: [2.01, None, 'PRE'], 1: [2.001, [(1, 1), (0, 1)], 'NEW'], 2: [2.0001, [(2, 4), (1, 1)], 'REP'], 3: [1.00001, None, 'LOST']}, 
                        {0: [1.01, None, 'PRE'], 1: [1.001, [(1, 2), (0, 0)], 'NEW'], 2: [1.0001, [(2, 2), (1, 2)], 'REP'], 3: [1.00001, [(3, 2), (2, 2)], 'REP']}]
# NB: Elements have reversed order. Because for the lower disThreshold the 1.001 is found first. Notes that they've swapped order in between the first two sets in SETS_2_IN
SETS_2_001_COUT1_POST = [{1: [1.001, None, 'PRE'], 2: [1.0001, [(2, 2), (1, 2)], 'NEW'], 3: [1.00001, [(3, 2), (2, 2)], 'REP']},
                         {1: [2.001, None, 'PRE'], 2: [2.0001, [(2, 4), (1, 1)], 'NEW'], 3: [1.00001, None, 'LOST']}]

SETS_2_0001_COUT1_POST = [{2: [1.0001, None, 'PRE'], 3: [1.00001, [(3, 2), (2, 2)], 'NEW']}]
'''
Diffs for SETS_2:

stelement around 1:
0->1  1.01  -1.001   =0.009
1->2  1.001 -1.0001  =0.0009
2->3  1.0001-1.000-1 =0.00009

stelement around 2:
0->1  2.01  -2.001   =0.009
1->2  2.001 -2.0001  =0.0009
'''
SETS_2_QI = ([[1.00001, 0.0001, 6], [2.0001, 0.001, 3]], None)

