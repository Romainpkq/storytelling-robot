# The encode of word is UTF-8
# The encode of message is UTF-8

# 获取敏感词汇列表
Sensitive_word = []
with open('word_detect//violence.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        Sensitive_word.append(line.strip('\n'))
with open('word_detect//religion.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        Sensitive_word.append(line.strip('\n'))
with open('word_detect//drug.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        Sensitive_word.append(line.strip('\n'))
with open('word_detect//pornographic.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        Sensitive_word.append(line.strip('\n'))
with open('word_detect//badword.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        Sensitive_word.append(line.strip('\n'))
print(Sensitive_word)


class cNode(object):
    def __init__(self):
        self.children = None


class cDfa(object):
    def __init__(self, lWords):
        self.root = None
        self.root = cNode()
        for sWord in lWords:
            self.addWord(sWord)

    # The encode of word is UTF-8
    def addWord(self, word):
        node = self.root
        word = word.split(' ')
        iEnd = len(word) - 1
        for i in range(len(word)):
            if node.children == None:
                node.children = {}
                if i != iEnd:
                    node.children[word[i]] = (cNode(), False)
                else:
                    node.children[word[i]] = (cNode(), True)

            elif word[i] not in node.children:
                if i != iEnd:
                    node.children[word[i]] = (cNode(), False)
                else:
                    node.children[word[i]] = (cNode(), True)
            else:  # word[i] in node.children:
                if i == iEnd:
                    Next, bWord = node.children[word[i]]
                    node.children[word[i]] = (Next, True)

            node = node.children[word[i]][0]

    def isContain(self, sMsg):
        root = self.root
        iLen = len(sMsg)
        for i in range(iLen):
            p = root
            j = i

            while (j < iLen and p.children != None and sMsg[j] in p.children):
                (p, bWord) = p.children[sMsg[j]]
                if bWord:
                    return True
                j = j + 1
        return False


cdfa = cDfa(Sensitive_word)   # 敏感词汇表
print(cdfa.isContain(['drug','is','not','good']))  # 这里的输入是需要检测的文本
