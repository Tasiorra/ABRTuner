#!/usr/bin/python

sizeDict = {3585: {0: 1765884, 1: 2106916, 2: 1921736, 3: 1880376, 4: 2248668, 5: 1957456, 6: 1643872, 7: 1590292, 8: 1651204, 9: 1233468, 10: 990948, 11: 2267468, 12: 2231184, 13: 1385560, 14: 975532, 15: 585244, 16: 2462800, 17: 2294916, 18: 1788256, 19: 2269536, 20: 1452300, 21: 1963284, 22: 1807432, 23: 2232688, 24: 1953696, 25: 2044688, 26: 1781300, 27: 2065932, 28: 1575252, 29: 1609092, 30: 1487080, 31: 2446444, 32: 1714184, 33: 2195840, 34: 2314656, 35: 1805364, 36: 2456408, 37: 1421468, 38: 1656280, 39: 2127972, 40: 2368048, 41: 1992612, 42: 1249072, 43: 1655904, 44: 1510204, 45: 2202232, 46: 1689180, 47: 2029084, 48: 1388004, 49: 2173468, 50: 2078528, 51: 2231560, 52: 2283260, 53: 2366356, 54: 2220468, 55: 2099772, 56: 2182304, 57: 2299240, 58: 1360744, 59: 2448888, 60: 1825668, 61: 2330448, 62: 2239268, 63: 2352256, 64: 2294540, 65: 2244720, 66: 2343420, 67: 2221596, 68: 2158052, 69: 1876616, 70: 1866652, 71: 1948808, 72: 2304504, 73: 452140}, 1434: {0: 519820, 1: 653488, 2: 609308, 3: 667964, 4: 980044, 5: 748240, 6: 658752, 7: 772492, 8: 681876, 9: 653676, 10: 565504, 11: 898452, 12: 940000, 13: 680936, 14: 554412, 15: 321480, 16: 956356, 17: 947520, 18: 782644, 19: 910108, 20: 694472, 21: 625476, 22: 635440, 23: 933796, 24: 849760, 25: 697856, 26: 637320, 27: 789224, 28: 628860, 29: 778132, 30: 737900, 31: 983428, 32: 783584, 33: 951092, 34: 908980, 35: 690336, 36: 974780, 37: 658752, 38: 756700, 39: 937932, 40: 924960, 41: 844684, 42: 639012, 43: 810656, 44: 706128, 45: 932480, 46: 739968, 47: 816484, 48: 526964, 49: 863860, 50: 821936, 51: 936428, 52: 868748, 53: 984932, 54: 916312, 55: 805956, 56: 819116, 57: 932292, 58: 617204, 59: 974592, 60: 644276, 61: 929660, 62: 920072, 63: 916124, 64: 923268, 65: 909732, 66: 945076, 67: 926088, 68: 895256, 69: 823064, 70: 747112, 71: 889804, 72: 903340, 73: 173148}, 2738: {0: 1271820, 1: 1593488, 2: 1331980, 3: 1359052, 4: 1769080, 5: 1467528, 6: 1351156, 7: 1257156, 8: 1275204, 9: 1039828, 10: 844120, 11: 1702528, 12: 1770772, 13: 1130632, 14: 801256, 15: 493500, 16: 1824164, 17: 1734864, 18: 1457000, 19: 1744452, 20: 1148680, 21: 1439328, 22: 1350028, 23: 1731668, 24: 1519228, 25: 1539156, 26: 1362812, 27: 1591044, 28: 1150936, 29: 1247568, 30: 1142100, 31: 1869284, 32: 1325024, 33: 1716064, 34: 1747836, 35: 1413384, 36: 1880940, 37: 1103372, 38: 1265992, 39: 1670380, 40: 1773592, 41: 1522988, 42: 1017080, 43: 1304344, 44: 1156952, 45: 1700460, 46: 1247756, 47: 1548368, 48: 1018960, 49: 1654964, 50: 1527500, 51: 1754604, 52: 1667748, 53: 1845972, 54: 1710236, 55: 1479184, 56: 1571304, 57: 1758364, 58: 1052612, 59: 1875112, 60: 1351908, 61: 1791264, 62: 1685984, 63: 1785436, 64: 1730728, 65: 1707228, 66: 1793332, 67: 1720388, 68: 1693316, 69: 1537276, 70: 1378416, 71: 1529756, 72: 1751596, 73: 360396}, 4661: {0: 2308828, 1: 2617336, 2: 2483480, 3: 2372372, 4: 2870196, 5: 2565448, 6: 2072700, 7: 2081160, 8: 2203548, 9: 1715500, 10: 1248696, 11: 2895764, 12: 2946900, 13: 1765132, 14: 1301336, 15: 754820, 16: 3192052, 17: 2986192, 18: 2203172, 19: 2948780, 20: 1830180, 21: 2845004, 22: 2524464, 23: 2751756, 24: 2617524, 25: 2672796, 26: 2233064, 27: 2713968, 28: 2093380, 29: 2034536, 30: 1960464, 31: 3156144, 32: 2386096, 33: 2941072, 34: 2989576, 35: 2364664, 36: 3165544, 37: 1940536, 38: 2206180, 39: 2849140, 40: 3040336, 41: 2563568, 42: 1661544, 43: 2163504, 44: 2115000, 45: 2862864, 46: 2272356, 47: 2602672, 48: 1861952, 49: 2804772, 50: 2832784, 51: 2896516, 52: 2937688, 53: 3078312, 54: 2900088, 55: 2767548, 56: 2700244, 57: 2946900, 58: 1721516, 59: 3201640, 60: 2327440, 61: 3078876, 62: 2903848, 63: 2992584, 64: 2992772, 65: 2873204, 66: 3041840, 67: 2881100, 68: 2715660, 69: 2159556, 70: 2162940, 71: 2353948, 72: 3012888, 73: 537304}, 5885: {0: 2945020, 1: 3278156, 2: 3257852, 3: 3193932, 4: 3462584, 5: 3168928, 6: 2878844, 7: 2645536, 8: 2698928, 9: 2057848, 10: 1448916, 11: 3583656, 12: 3593620, 13: 2117256, 14: 1524304, 15: 914056, 16: 3921680, 17: 3679160, 18: 2736528, 19: 3505636, 20: 2305632, 21: 3735748, 22: 3176824, 23: 3329480, 24: 3182464, 25: 3324028, 26: 2841244, 27: 3433068, 28: 2651740, 29: 2483668, 30: 2414108, 31: 3872048, 32: 2924340, 33: 3551132, 34: 3756616, 35: 3013452, 36: 3938600, 37: 2338156, 38: 2779392, 39: 3446604, 40: 3750600, 41: 3155768, 42: 1962908, 43: 2592708, 44: 2534992, 45: 3502064, 46: 2724872, 47: 3241496, 48: 2362596, 49: 3499432, 50: 3343768, 51: 3784440, 52: 3540604, 53: 3778424, 54: 3580460, 55: 3339068, 56: 3349596, 57: 3653404, 58: 2125528, 59: 3968680, 60: 2829024, 61: 3741576, 62: 3555268, 63: 3712624, 64: 3559404, 65: 3343768, 66: 4042000, 67: 3332300, 68: 3047292, 69: 2445504, 70: 2468440, 71: 2685204, 72: 3710556, 73: 570392}, 1002: {0: 394988, 1: 465676, 2: 437100, 3: 444432, 4: 682816, 5: 532228, 6: 433340, 7: 531476, 8: 492184, 9: 461352, 10: 411532, 11: 637320, 12: 672852, 13: 484852, 14: 411908, 15: 256432, 16: 654428, 17: 665708, 18: 563812, 19: 642208, 20: 496884, 21: 434468, 22: 449132, 23: 643336, 24: 606676, 25: 471692, 26: 446688, 27: 554788, 28: 463608, 29: 542192, 30: 580732, 31: 688644, 32: 590320, 33: 670032, 34: 633748, 35: 503088, 36: 676424, 37: 476768, 38: 544260, 39: 667964, 40: 652548, 41: 586748, 42: 515308, 43: 589192, 44: 530160, 45: 660444, 46: 536928, 47: 554600, 48: 378820, 49: 610436, 50: 575844, 51: 660444, 52: 619272, 53: 680372, 54: 653300, 55: 518880, 56: 567760, 57: 656872, 58: 484288, 59: 682252, 60: 444432, 61: 664204, 62: 658752, 63: 642772, 64: 638072, 65: 645968, 66: 671536, 67: 644464, 68: 639576, 69: 580920, 70: 570956, 71: 613820, 72: 684884, 73: 128780}}

size_OfForest = {0:[282755, 155778, 311847, 422909, 432779, 443771, 439713, 439295, 440716, 427680, 434523, 432886, 409561, 447680, 404293, 424112, 417267, 437398, 433910, 430957, 422812, 435684, 422647, 435124, 441513, 435810, 438944, 439557, 435669, 438398, 416713, 440032, 433932, 410919, 434872, 457838, 429547, 421083, 441206, 402152, 433435, 410485, 422872, 440263, 412943, 393307, 443952, 417298, 430313, 428669, 446711, 413531, 472807, 367828, 442587, 428393, 443507, 430633, 445315, 449486, 428238, 409979, 429106, 418762, 426566, 435364, 438827, 452881, 443453, 451374, 425378, 442663, 442851, 432865, 449249, 433516, 444948, 440282, 445807, 433311, 434492, 437537, 468473, 379114, 412332, 452650, 428381, 459678, 441524, 447295, 451530, 445277, 425393, 429617, 384762, 448441, 436199, 390859, 328978, 442623, 430698, 442325, 416507, 433417, 437520, 438973, 347216, 313219, 457926, 148002, 127106, 173395, 7406, 2357],1:[341841, 199148, 336627, 612756, 692106, 690817, 684027, 696949, 682883, 624185, 678484, 670935, 632343, 711204, 619808, 660536, 659331, 688091, 676113, 675901, 661036, 676458, 663765, 682300, 686096, 683843, 687052, 683491, 686918, 687548, 658114, 669358, 696024, 652231, 673400, 713144, 675127, 658274, 696600, 624312, 681852, 641698, 662551, 691876, 649283, 637033, 665060, 645309, 660062, 659383, 696439, 646756, 736241, 577039, 693470, 689682, 694339, 661258, 694017, 703784, 687097, 654310, 668290, 659898, 668089, 686850, 691525, 707777, 695727, 705655, 674210, 690770, 690019, 684147, 694397, 669607, 696240, 692208, 697960, 687430, 680100, 586661, 591405, 550801, 657251, 696014, 678436, 653180, 647550, 611733, 601398, 584036, 580985, 579581, 611239, 701929, 692930, 508301, 402235, 709816, 674094, 698396, 652308, 682051, 687825, 691024, 516993, 413663, 721554, 176183, 152174, 188807, 7406, 2357],2:[361420, 202943, 336627, 684536, 997376, 1000196, 989321, 997321, 961050, 699395, 885824, 970564, 948069, 1031454, 878808, 943688, 942268, 985963, 974760, 968692, 960860, 983277, 958658, 989372, 985188, 994880, 990094, 988789, 994435, 995228, 976543, 979775, 1000331, 949356, 958789, 1024890, 972409, 962903, 1004805, 914264, 980379, 964551, 947521, 1002742, 941644, 939273, 988839, 937661, 946788, 968003, 996837, 933603, 1055340, 853048, 1003450, 991062, 985764, 959145, 1004067, 1013305, 993409, 915792, 969775, 939865, 973861, 980332, 990590, 1012894, 992790, 1009313, 961418, 995114, 999938, 973670, 1006467, 954598, 998824, 1003733, 1000622, 971581, 879654, 664203, 592438, 721182, 975811, 999182, 979203, 832007, 658110, 613783, 601419, 593037, 602727, 627169, 943591, 1010832, 998694, 632584, 494681, 1022651, 967670, 998609, 948966, 985700, 984630, 1013221, 697622, 430218, 904433, 194889, 188040, 193864, 7406, 2357],3:[361445, 202825, 336627, 688515, 1208841, 1366836, 1472773, 1497629, 1136723, 707595, 905629, 1258729, 1450174, 1563075, 1123597, 1079711, 1396811, 1493771, 1485297, 1489312, 1481155, 1498946, 1461493, 1496552, 1512231, 1498222, 1494487, 1510556, 1504993, 1494016, 1500580, 1476176, 1515653, 1422092, 1456469, 1515206, 1280007, 1335533, 1522721, 1375502, 1480791, 1486263, 1414297, 1535244, 1424551, 1397159, 1487633, 1400993, 1428228, 1461906, 1507339, 1430926, 1589255, 1294875, 1510965, 1492248, 1486481, 1473623, 1512695, 1513205, 1501455, 1357764, 1466293, 1458602, 1487608, 1508553, 1471707, 1517655, 1490323, 1516164, 1447519, 1506473, 1497075, 1462911, 1513577, 1443176, 1504746, 1511369, 1504359, 1336952, 891944, 672138, 594266, 974342, 1498308, 1467041, 1494174, 1074633, 659343, 614780, 601419, 599293, 603007, 640957, 1480140, 1550389, 1352669, 722686, 626551, 1558380, 1448439, 1513558, 1445404, 1494219, 1513412, 1532164, 951852, 443434, 906017, 197722, 227786, 199929, 7406, 2357],4:[361445, 202825, 336627, 690566, 1211250, 1370623, 1498517, 1562484, 1144999, 708726, 905629, 1262741, 1696865, 1807991, 1150117, 1095326, 1797201, 1999455, 1985966, 2001455, 2003956, 2014651, 1971690, 2005190, 2022374, 1994200, 2009105, 2000879, 2010476, 1980713, 2024019, 1924145, 2024856, 1897628, 1978537, 1925466, 1290482, 1562286, 2015012, 1882463, 1963452, 2012193, 1874609, 2066305, 1902900, 1886048, 2014663, 1818121, 1966850, 1981334, 2008226, 1941058, 2102235, 1557192, 2043530, 1988759, 1960959, 1972992, 1998028, 1885195, 1780691, 1728614, 1974001, 1965601, 2005824, 2004990, 1965262, 2015274, 1987818, 2026464, 1947231, 1999525, 1989057, 1977246, 2032277, 1913606, 2002800, 2018178, 2011893, 1556821, 890388, 673537, 594266, 1177204, 1996044, 1953201, 2014553, 1320054, 659544, 613427, 601419, 600169, 603810, 642127, 1947555, 2085534, 1410048, 722511, 754614, 2074743, 1948282, 2013801, 1947801, 2006921, 2010559, 2055168, 1134515, 443202, 906017, 201265, 227190, 211968, 7406, 2357],5:[361445, 202825, 336627, 690680, 1213661, 1371566, 1497758, 1566245, 1145621, 708726, 905629, 1262741, 1712850, 1812289, 1150117, 1095326, 2175159, 2504775, 2476217, 2506140, 2512320, 2516634, 2470706, 2509600, 2539359, 2482961, 2507343, 2507922, 2514849, 2481256, 2490955, 2427783, 2557376, 2385919, 2498460, 2264255, 1293722, 1587228, 2067374, 2251221, 2501152, 2451900, 2346051, 2600050, 2433845, 2358187, 2521675, 2026198, 2463138, 2491932, 2489983, 2451547, 2590907, 1790367, 2546688, 2493138, 2400311, 2069842, 2037571, 1884275, 1790516, 1964758, 2476670, 2471282, 2544016, 2496217, 2465368, 2517621, 2486400, 2532800, 2444004, 2490786, 2489363, 2461910, 2473110, 2216617, 2494800, 2528255, 2408238, 1600570, 892459, 681465, 594266, 1274997, 2309384, 2387810, 2522173, 1524144, 659827, 613290, 601419, 601546, 603654, 642127, 2117633, 2303689, 1424683, 721222, 889133, 2594359, 2428087, 2509516, 2466261, 2508273, 2522887, 2576514, 1304183, 443445, 906017, 202771, 225588, 212322, 7406, 2357]}
size_envivo = {0:[207189,219272,134208,204651,164461,230942,136746,150366,193697,193362,189146,153391,195591,177177,190923,155030,185660,164741,179442,131632,198676,115285,148044,181978,200708,177663,176815,109489,203211,196841,161524,151656,182521,172804,211407,171710,170866,178753,175461,184494,154382,206330,175870,178679,173567,172998,189473,172737,163181,181882,186151,164281,172026,173011,162488,201781,176856,137099,57015,234214,172494,184405,61936,43268,81580],1:[361158,370284,246858,357922,264156,371586,241808,270621,327839,334864,313171,253682,348331,319047,311275,282933,308899,289234,307870,207573,354546,208087,305510,364291,331480,298846,298034,195290,327636,354076,261457,272419,344053,307537,344697,301834,261403,332467,324205,276260,260969,357539,301214,320538,292593,290952,325914,285965,266844,327707,308757,271734,313780,284833,295589,331270,307411,224531,94934,385537,306688,310705,95847,78651,162260],2:[604139,577615,418531,555427,469238,614632,393715,428426,594788,527047,460827,500774,621760,556545,476734,417508,552639,462442,552256,303234,522859,337637,471941,598737,560588,487684,479873,284277,564825,546935,394056,442514,610493,523364,574457,499175,412705,586327,560284,476697,408166,570011,502061,569274,444948,507586,525450,541979,391886,539537,506089,408110,515570,462132,574826,523754,572621,344553,157240,610010,460871,480012,169331,126490,236234],3:[1184008,1123706,854424,1150093,902304,1237428,763515,840707,1279590,930828,996858,950867,1285933,1049248,984261,876058,1054391,875132,996451,660126,1032091,626844,949274,1197901,1001670,994288,925341,623084,977347,1184694,766276,834528,1285071,1017030,1080835,1078945,788728,1165402,1123991,937434,804808,1178153,922947,1175468,903392,970351,1094905,931644,854957,1179875,978233,794797,1073857,942081,1074761,1033448,1181202,660582,297985,1188866,910001,974311,314327,221329,445973],4:[1680951,1637558,1371111,1684293,1400042,1792609,1213669,1191552,1888982,1381292,1593129,1384566,1918298,1605664,1356382,1278860,1580165,1315506,1642869,928190,1416000,865548,1284104,1692271,1504744,1484004,1405086,891371,1401736,1743545,1084561,1099310,1789869,1675658,1636106,1492615,1200522,1787763,1690817,1459339,1250444,1691788,1403315,1732710,1270067,1514363,1615320,1507682,1260622,1784654,1352160,1115913,1637646,1546975,1637443,1475444,1616179,1113960,466635,1727956,1316739,1373312,458410,320487,573826]}



## function returns the dynamic value of the reservoir
#def dynamicReservoir(bw, chunkid, X, reservoir, CHUNKSIZE, bitrate, candidateBitRate):
#  if chunkid > len(sizeDict[candidateBitRate[0]]) - X / CHUNKSIZE:
#    return reservoir
#  bufAdded = 0
#  timeAccumulated = 0.0
#  while ((sizeDict[bitrate][chunkid] / 1000.0) * CHUNKSIZE) / float(bw) + timeAccumulated < X:
#    chunkid += 1
#    timeAccumulated += ((sizeDict[bitrate][chunkid] / 1000.0) * CHUNKSIZE) / float(bw)
##    print timeAccumulated
#    bufAdded += CHUNKSIZE
#  print "bufAdded: " + str(bufAdded)
#  ret = max(X - bufAdded, 2)
#  return ret
#
#candidateBitRate = [1434,2738,3585,4661,5885]
#print dynamicReservoir(2500, 10, 25, 15, 5, 1434, candidateBitRate)
#print dynamicReservoir(2500, 10, 25, 15, 5, 2738, candidateBitRate)
#print dynamicReservoir(2500, 10, 25, 15, 5, 3585, candidateBitRate)
#print dynamicReservoir(2500, 10, 25, 15, 5, 4661, candidateBitRate)
#print dynamicReservoir(500, 65, 25, 17, 5, 5885, candidateBitRate)
