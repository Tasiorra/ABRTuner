MediaPlayer.dependencies.VBR = function () {
    "use strict";

    // racecar video
	var size_video1 = [1680951,1637558,1371111,1684293,1400042,1792609,1213669,1191552,1888982,1381292,1593129,1384566,1918298,1605664,1356382,1278860,1580165,1315506,1642869,928190,1416000,865548,1284104,1692271,1504744,1484004,1405086,891371,1401736,1743545,1084561,1099310,1789869,1675658,1636106,1492615,1200522,1787763,1690817,1459339,1250444,1691788,1403315,1732710,1270067,1514363,1615320,1507682,1260622,1784654,1352160,1115913,1637646,1546975,1637443,1475444,1616179,1113960,466635,1727956,1316739,1373312,458410,320487,573826],
	size_video2 = [1184008,1123706,854424,1150093,902304,1237428,763515,840707,1279590,930828,996858,950867,1285933,1049248,984261,876058,1054391,875132,996451,660126,1032091,626844,949274,1197901,1001670,994288,925341,623084,977347,1184694,766276,834528,1285071,1017030,1080835,1078945,788728,1165402,1123991,937434,804808,1178153,922947,1175468,903392,970351,1094905,931644,854957,1179875,978233,794797,1073857,942081,1074761,1033448,1181202,660582,297985,1188866,910001,974311,314327,221329,445973],
	size_video3 = [604139,577615,418531,555427,469238,614632,393715,428426,594788,527047,460827,500774,621760,556545,476734,417508,552639,462442,552256,303234,522859,337637,471941,598737,560588,487684,479873,284277,564825,546935,394056,442514,610493,523364,574457,499175,412705,586327,560284,476697,408166,570011,502061,569274,444948,507586,525450,541979,391886,539537,506089,408110,515570,462132,574826,523754,572621,344553,157240,610010,460871,480012,169331,126490,236234],
	size_video4 = [361158,370284,246858,357922,264156,371586,241808,270621,327839,334864,313171,253682,348331,319047,311275,282933,308899,289234,307870,207573,354546,208087,305510,364291,331480,298846,298034,195290,327636,354076,261457,272419,344053,307537,344697,301834,261403,332467,324205,276260,260969,357539,301214,320538,292593,290952,325914,285965,266844,327707,308757,271734,313780,284833,295589,331270,307411,224531,94934,385537,306688,310705,95847,78651,162260],
	size_video5 = [207189,219272,134208,204651,164461,230942,136746,150366,193697,193362,189146,153391,195591,177177,190923,155030,185660,164741,179442,131632,198676,115285,148044,181978,200708,177663,176815,109489,203211,196841,161524,151656,182521,172804,211407,171710,170866,178753,175461,184494,154382,206330,175870,178679,173567,172998,189473,172737,163181,181882,186151,164281,172026,173011,162488,201781,176856,137099,57015,234214,172494,184405,61936,43268,81580];

    // weird video
    // var size_video1 = [2354772, 2123065, 2177073, 2160877, 2233056, 1941625, 2157535, 2290172, 2055469, 2169201, 2173522, 2102452, 2209463, 2275376, 2005399, 2152483, 2289689, 2059512, 2220726, 2156729, 2039773, 2176469, 2221506, 2044075, 2186790, 2105231, 2395588, 1972048, 2134614, 2164140, 2113193, 2147852, 2191074, 2286761, 2307787, 2143948, 1919781, 2147467, 2133870, 2146120, 2108491, 2184571, 2121928, 2219102, 2124950, 2246506, 1961140, 2155012, 1433658],
    // size_video2 = [1728879, 1431809, 1300868, 1520281, 1472558, 1224260, 1388403, 1638769, 1348011, 1429765, 1354548, 1519951, 1422919, 1578343, 1231445, 1471065, 1491626, 1358801, 1537156, 1336050, 1415116, 1468126, 1505760, 1323990, 1383735, 1480464, 1547572, 1141971, 1498470, 1561263, 1341201, 1497683, 1358081, 1587293, 1492672, 1439896, 1139291, 1499009, 1427478, 1402287, 1339500, 1527299, 1343002, 1587250, 1464921, 1483527, 1231456, 1364537, 889412],
    // size_video3 = [1034108, 957685, 877771, 933276, 996749, 801058, 905515, 1060487, 852833, 913888, 939819, 917428, 946851, 1036454, 821631, 923170, 966699, 885714, 987708, 923755, 891604, 955231, 968026, 874175, 897976, 905935, 1076599, 758197, 972798, 975811, 873429, 954453, 885062, 1035329, 1026056, 943942, 728962, 938587, 908665, 930577, 858450, 1025005, 886255, 973972, 958994, 982064, 830730, 846370, 598850],
    // size_video4 = [668286, 611087, 571051, 617681, 652874, 520315, 561791, 709534, 584846, 560821, 607410, 594078, 624282, 687371, 526950, 587876, 617242, 581493, 639204, 586839, 601738, 616206, 656471, 536667, 587236, 590335, 696376, 487160, 622896, 641447, 570392, 620283, 584349, 670129, 690253, 598727, 487812, 575591, 605884, 587506, 566904, 641452, 599477, 634861, 630203, 638661, 538612, 550906, 391450],
    // size_video5 = [450283, 398865, 350812, 382355, 411561, 318564, 352642, 437162, 374758, 362795, 353220, 405134, 386351, 434409, 337059, 366214, 360831, 372963, 405596, 350713, 386472, 399894, 401853, 343800, 359903, 379700, 425781, 277716, 400396, 400508, 358218, 400322, 369834, 412837, 401088, 365161, 321064, 361565, 378327, 390680, 345516, 384505, 372093, 438281, 398987, 393804, 331053, 314107, 255954],
    // size_video6 = [181801, 155580, 139857, 155432, 163442, 126289, 153295, 173849, 150710, 139105, 141840, 156148, 160746, 179801, 140051, 138313, 143509, 150616, 165384, 140881, 157671, 157812, 163927, 137654, 146754, 153938, 181901, 111155, 153605, 149029, 157421, 157488, 143881, 163444, 179328, 159914, 131610, 124011, 144254, 149991, 147968, 161857, 145210, 172312, 167025, 160064, 137507, 118421, 112270];

	var size_OfForest = {0:[282755, 155778, 311847, 422909, 432779, 443771, 439713, 439295, 440716, 427680, 434523, 432886, 409561, 447680, 404293, 424112, 417267, 437398, 433910, 430957, 422812, 435684, 422647, 435124, 441513, 435810, 438944, 439557, 435669, 438398, 416713, 440032, 433932, 410919, 434872, 457838, 429547, 421083, 441206, 402152, 433435, 410485, 422872, 440263, 412943, 393307, 443952, 417298, 430313, 428669, 446711, 413531, 472807, 367828, 442587, 428393, 443507, 430633, 445315, 449486, 428238, 409979, 429106, 418762, 426566, 435364, 438827, 452881, 443453, 451374, 425378, 442663, 442851, 432865, 449249, 433516, 444948, 440282, 445807, 433311, 434492, 437537, 468473, 379114, 412332, 452650, 428381, 459678, 441524, 447295, 451530, 445277, 425393, 429617, 384762, 448441, 436199, 390859, 328978, 442623, 430698, 442325, 416507, 433417, 437520, 438973, 347216, 313219, 457926, 148002, 127106, 173395, 7406, 2357],1:[341841, 199148, 336627, 612756, 692106, 690817, 684027, 696949, 682883, 624185, 678484, 670935, 632343, 711204, 619808, 660536, 659331, 688091, 676113, 675901, 661036, 676458, 663765, 682300, 686096, 683843, 687052, 683491, 686918, 687548, 658114, 669358, 696024, 652231, 673400, 713144, 675127, 658274, 696600, 624312, 681852, 641698, 662551, 691876, 649283, 637033, 665060, 645309, 660062, 659383, 696439, 646756, 736241, 577039, 693470, 689682, 694339, 661258, 694017, 703784, 687097, 654310, 668290, 659898, 668089, 686850, 691525, 707777, 695727, 705655, 674210, 690770, 690019, 684147, 694397, 669607, 696240, 692208, 697960, 687430, 680100, 586661, 591405, 550801, 657251, 696014, 678436, 653180, 647550, 611733, 601398, 584036, 580985, 579581, 611239, 701929, 692930, 508301, 402235, 709816, 674094, 698396, 652308, 682051, 687825, 691024, 516993, 413663, 721554, 176183, 152174, 188807, 7406, 2357],2:[361420, 202943, 336627, 684536, 997376, 1000196, 989321, 997321, 961050, 699395, 885824, 970564, 948069, 1031454, 878808, 943688, 942268, 985963, 974760, 968692, 960860, 983277, 958658, 989372, 985188, 994880, 990094, 988789, 994435, 995228, 976543, 979775, 1000331, 949356, 958789, 1024890, 972409, 962903, 1004805, 914264, 980379, 964551, 947521, 1002742, 941644, 939273, 988839, 937661, 946788, 968003, 996837, 933603, 1055340, 853048, 1003450, 991062, 985764, 959145, 1004067, 1013305, 993409, 915792, 969775, 939865, 973861, 980332, 990590, 1012894, 992790, 1009313, 961418, 995114, 999938, 973670, 1006467, 954598, 998824, 1003733, 1000622, 971581, 879654, 664203, 592438, 721182, 975811, 999182, 979203, 832007, 658110, 613783, 601419, 593037, 602727, 627169, 943591, 1010832, 998694, 632584, 494681, 1022651, 967670, 998609, 948966, 985700, 984630, 1013221, 697622, 430218, 904433, 194889, 188040, 193864, 7406, 2357],3:[361445, 202825, 336627, 688515, 1208841, 1366836, 1472773, 1497629, 1136723, 707595, 905629, 1258729, 1450174, 1563075, 1123597, 1079711, 1396811, 1493771, 1485297, 1489312, 1481155, 1498946, 1461493, 1496552, 1512231, 1498222, 1494487, 1510556, 1504993, 1494016, 1500580, 1476176, 1515653, 1422092, 1456469, 1515206, 1280007, 1335533, 1522721, 1375502, 1480791, 1486263, 1414297, 1535244, 1424551, 1397159, 1487633, 1400993, 1428228, 1461906, 1507339, 1430926, 1589255, 1294875, 1510965, 1492248, 1486481, 1473623, 1512695, 1513205, 1501455, 1357764, 1466293, 1458602, 1487608, 1508553, 1471707, 1517655, 1490323, 1516164, 1447519, 1506473, 1497075, 1462911, 1513577, 1443176, 1504746, 1511369, 1504359, 1336952, 891944, 672138, 594266, 974342, 1498308, 1467041, 1494174, 1074633, 659343, 614780, 601419, 599293, 603007, 640957, 1480140, 1550389, 1352669, 722686, 626551, 1558380, 1448439, 1513558, 1445404, 1494219, 1513412, 1532164, 951852, 443434, 906017, 197722, 227786, 199929, 7406, 2357],4:[361445, 202825, 336627, 690566, 1211250, 1370623, 1498517, 1562484, 1144999, 708726, 905629, 1262741, 1696865, 1807991, 1150117, 1095326, 1797201, 1999455, 1985966, 2001455, 2003956, 2014651, 1971690, 2005190, 2022374, 1994200, 2009105, 2000879, 2010476, 1980713, 2024019, 1924145, 2024856, 1897628, 1978537, 1925466, 1290482, 1562286, 2015012, 1882463, 1963452, 2012193, 1874609, 2066305, 1902900, 1886048, 2014663, 1818121, 1966850, 1981334, 2008226, 1941058, 2102235, 1557192, 2043530, 1988759, 1960959, 1972992, 1998028, 1885195, 1780691, 1728614, 1974001, 1965601, 2005824, 2004990, 1965262, 2015274, 1987818, 2026464, 1947231, 1999525, 1989057, 1977246, 2032277, 1913606, 2002800, 2018178, 2011893, 1556821, 890388, 673537, 594266, 1177204, 1996044, 1953201, 2014553, 1320054, 659544, 613427, 601419, 600169, 603810, 642127, 1947555, 2085534, 1410048, 722511, 754614, 2074743, 1948282, 2013801, 1947801, 2006921, 2010559, 2055168, 1134515, 443202, 906017, 201265, 227190, 211968, 7406, 2357],5:[361445, 202825, 336627, 690680, 1213661, 1371566, 1497758, 1566245, 1145621, 708726, 905629, 1262741, 1712850, 1812289, 1150117, 1095326, 2175159, 2504775, 2476217, 2506140, 2512320, 2516634, 2470706, 2509600, 2539359, 2482961, 2507343, 2507922, 2514849, 2481256, 2490955, 2427783, 2557376, 2385919, 2498460, 2264255, 1293722, 1587228, 2067374, 2251221, 2501152, 2451900, 2346051, 2600050, 2433845, 2358187, 2521675, 2026198, 2463138, 2491932, 2489983, 2451547, 2590907, 1790367, 2546688, 2493138, 2400311, 2069842, 2037571, 1884275, 1790516, 1964758, 2476670, 2471282, 2544016, 2496217, 2465368, 2517621, 2486400, 2532800, 2444004, 2490786, 2489363, 2461910, 2473110, 2216617, 2494800, 2528255, 2408238, 1600570, 892459, 681465, 594266, 1274997, 2309384, 2387810, 2522173, 1524144, 659827, 613290, 601419, 601546, 603654, 642127, 2117633, 2303689, 1424683, 721222, 889133, 2594359, 2428087, 2509516, 2466261, 2508273, 2522887, 2576514, 1304183, 443445, 906017, 202771, 225588, 212322, 7406, 2357]};

return {
        debug: undefined,

	getChunkSize: function (index, quality) {
        if (index < 0 || index > 64) {
            return 0;
        }

        // if using the weird racecar video use this switch
        // var chunkSize;
        // switch (quality) {
        //     case 5:
        //         chunkSize = size_video1[index];
        //         break;
        //     case 4:
        //         chunkSize = size_video2[index];
        //         break;
        //     case 3:
        //         chunkSize = size_video3[index];
        //         break;
        //     case 2:
        //         chunkSize = size_video4[index];
        //         break;
        //     case 1:
        //         chunkSize = size_video5[index];
        //         break;
        //     case 0:
        //         chunkSize = size_video6[index];
        //         break;
        //     default:
        //         chunkSize = 0;
        //         break;
        // }

        // if using the racecar video uncomment the switch below and comment the switch above
        var chunkSize;
        switch (quality) {
            case 4:
                chunkSize = size_video1[index];
                break;
            case 3:
                chunkSize = size_video2[index];
                break;
            case 2:
                chunkSize = size_video3[index];
                break;
            case 1:
                chunkSize = size_video4[index];
                break;
            case 0:
                chunkSize = size_video5[index];
                break;
            default:
                chunkSize = 0;
                break;
        }
        return chunkSize;
    },
    getChunkSize_OfForest: function (index, quality) {
        if (index < 0 || index >114) {
            return 0;
        }
        var chunkSize;
        chunkSize = size_OfForest[quality][index];
        return chunkSize;
    }
    };
};

MediaPlayer.dependencies.VBR.prototype = {
    constructor: MediaPlayer.dependencies.VBR
};
