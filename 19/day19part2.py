import re
n42 = ['aabaabba', 'aabbbbba', 'aabbabba', 'aaabbbba', 'aaababba', 'aaaabbba', 'aaaaabba', 'aabaaaba', 'aabababa', 'aaaaaaba', 'aaabbaba', 'abbababa', 'abbbaaba', 'abbaaaba', 'abbaabba', 'abbabbba', 'abaababa', 'abaabbba', 'abaaabba', 'ababaaba', 'ababbbba', 'ababbbaa', 'abbbbbaa', 'abababaa', 'abbaabaa', 'abaaabaa', 'aaaaabaa', 'aabbabaa', 'aabaabaa', 'aaabaaaa', 'aabbaaaa', 'aaaaaaaa', 'abbaaaaa', 'abaaaaaa', 'abaabaaa', 'abbabaaa', 'abbbbaab', 'abbbbbab', 'abbabbab', 'abbaabab', 'abbaaaab', 'abbaaabb', 'abbbbabb', 'abbabbbb', 'abbbabbb', 'abbaabbb', 'abababbb', 'ababaabb', 'ababbabb', 'ababbaab', 'abaabaab', 'abaaaaab', 'abababab', 'aabbaaab', 'aabbbbab', 'aabbbaab', 'aababbab', 'aabaabab', 'aabaaaab', 'aabbabbb', 'aabbaabb', 'aabbbbbb', 'aabbbabb', 'aaabbabb', 'aaaababb', 'aaaabbbb', 'aaaaaaab', 'aaabbaab', 'aaabaaab', 'aaaabbab', 'baabaaaa', 'baabbaaa', 'baaababa', 'baaaabba', 'baabbaba', 'babaaaaa', 'babbbbaa', 'babbabaa', 'babbaaaa', 'babbaaba', 'babbabba', 'babaabba', 'baabbabb', 'baabbbab', 'baabbaab', 'baabaabb', 'baababab', 'baabaaab', 'baaaaaab', 'baaabbab', 'baaaaabb', 'baaabbbb', 'baaababb', 'babbbaab', 'bababaab', 'babaaaab', 'babbabab', 'babaaabb', 'babbbbbb', 'bababbbb', 'babaabbb', 'bbbababb', 'bbbaabab', 'bbbbbbab', 'bbbbbbbb', 'bbbbbabb', 'bbbbaaab', 'bbbbabbb', 'bbbbabab', 'bbaabaab', 'bbabbbab', 'bbabbbbb', 'bbababab', 'bbaababa', 'bbabbbba', 'bbaabbba', 'bbaaabba', 'bbaabaaa', 'bbabaaaa', 'bbaaaaaa', 'bbababaa', 'bbbabbba', 'bbbaabba', 'bbbabaaa', 'bbbabbaa', 'bbbbabba', 'bbbbaaba', 'bbbbbbaa']
n31 = ['bbababba', 'bbbbbbba', 'bbabaaba', 'bbbaaaba', 'bbaaaaba', 'bbbababa', 'bbbbbaba', 'bbabbaba', 'bbaabbaa', 'bbabbbaa', 'bbaaabaa', 'bbbbabaa', 'bbbaabaa', 'bbbbbaaa', 'bbabbaaa', 'bbbaaaaa', 'bbbbaaaa', 'bbaaabab', 'bbaabbab', 'bbaaaaab', 'bbabbaab', 'bbabaaab', 'bbbbbaab', 'bbbaaaab', 'bbbabbab', 'bbbabaab', 'bbbabbbb', 'bbbaabbb', 'bbbaaabb', 'bbbbaabb', 'bbabbabb', 'bbabaabb', 'bbaababb', 'bbaaaabb', 'bbaabbbb', 'bbababbb', 'bbaaabbb', 'babbabbb', 'baaaabbb', 'baabbbbb', 'baababbb', 'babababb', 'babbbabb', 'babbaabb', 'baaabaab', 'babbaaab', 'baaaabab', 'babbbbab', 'bababbab', 'babaabab', 'babbbaaa', 'bababaaa', 'babaabaa', 'bababbaa', 'baaabbaa', 'baaabaaa', 'baaaabaa', 'baaaaaaa', 'baabbbaa', 'baababaa', 'babbbbba', 'bababbba', 'baabbbba', 'baaabbba', 'baababba', 'baabaaba', 'babaaaba', 'baaaaaba', 'babababa', 'babbbaba', 'abbbabba', 'abbbbbba', 'abababba', 'abaaaaba', 'abbbbaba', 'ababbaba', 'aabbaaba', 'aabbbaba', 'aaabaaba', 'aaaababa', 'aababbba', 'aabbbbaa', 'aababbaa', 'aaabbbaa', 'aaaabbaa', 'aaababaa', 'abbbabaa', 'abbabbaa', 'abaabbaa', 'aabbbaaa', 'aababaaa', 'aaabbaaa', 'aaaabaaa', 'abbbbaaa', 'ababbaaa', 'ababaaaa', 'abbbaaaa', 'aabaaaaa', 'aaabaabb', 'aabaaabb', 'aaaaaabb', 'aabababb', 'aababbbb', 'aaabbbbb', 'aaababbb', 'aabaabbb', 'aaaaabbb', 'aaaabaab', 'aaaaabab', 'aaabbbab', 'aaababab', 'aabbabab', 'aababaab', 'abaaabbb', 'abbbbbbb', 'ababbbbb', 'abaabbbb', 'abaaaabb', 'abaababb', 'abbbaabb', 'abbababb', 'abbabaab', 'abbbaaab', 'abbbabab', 'ababaaab', 'ababbbab', 'abaabbab', 'abaaabab']
class day19part2:
    def rg(self, pile, x):
        cnt = 0
        c = ""
        r = ""
        for i in range(x):
            c = "a" + c + "b"
            r += "|(^a+("+c+")$)"
        for p in pile:
            #aim, something like this: |(^a+(ab)$)|(^a+(aabb)$)|(^a+(aaabbb)$)|(^a+(aaaabbbb)$)|(^a+(aaaaabbbbb)$)|(^a+(aaaaaabbbbbb)$)
            rege = '(^aab$)' + r
            if re.search(rege, p):
                cnt += 1
        return cnt
    def __init__(self, fName, n42, n31):
        self.input = [x.splitlines() for x in open(fName, "r").read().split("\n\n")]
        self.n42 = n42
        self.n31 = n31
        # for a in n31:
        #     print (len(a))
        pile = []
        for one in self.input[1]:
            tmp = one
            nw = ""
            while len(tmp) > 0:
                tmp2 = tmp[0:8]
                if (tmp2 in n42):
                    nw += "a"
                elif (tmp2 in n31):
                    nw += "b"
                else:
                    nw += "c"
                tmp = tmp[8:]
            pile.append(nw)
        nr = 0
        last = 0
        current = self.rg(pile,nr)
        while last != current:
            nr += 1
            last = current
            current = self.rg(pile,nr)
        print (current)
task = day19part2("input.txt", n42, n31)
