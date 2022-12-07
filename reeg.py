# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

"""import re

regex = r"[a-z]+t"

test_str = "the cat sat on the mat"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"\s([a-z]{2})\s"

test_str = "the cat sat on the mat"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution."""



""""
([0-9]{4})
"""
'''gm
1st Capturing Group ([0-9]{4})
Match a single character present in the list below [0-9]
{4} matches the previous token exactly 4 times
0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
Global pattern flags 
g modifier: global. All matches (don't return after first match)
m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
0-4	2022
0-4	2022
Search reference
Search reference
4
([0-9]{4})
2022/12/06
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"([0-9]{4})"

test_str = "2022/12/06"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitutio




import re

regex = r"([A-Za-z]+)\.$"

test_str = "Regular expression (regex, regexp or rational expression) is a sequence of characters that specifies a search pattern. Usually these patterns are used by string-searching algorithms for find or find and replace operations on strings, or for input validation."

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
