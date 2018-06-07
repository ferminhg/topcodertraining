class Substitute():
    def init(self):
        self.key = ''
    def getValue(self, key, code):
        result = ''
        for i in range(len(code)):
            pos = key.find(code[i])
            if pos != -1:
                result += str((pos+1) % 10)
        if result != '':
            return int(result)
        return 0

sb = Substitute()

assert sb.getValue("TRADINGFEW", "LGXWEV") == 709
assert sb.getValue("ABCDEFGHIJ", "XJ") == 0
assert sb.getValue("CRYSTALBUM", "MMA") == 6
assert sb.getValue("CRYSTALBUM", "") == 0