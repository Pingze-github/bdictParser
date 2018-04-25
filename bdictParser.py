import binascii

class BdictParser():
    def __init__(self):
        pass

    def hex2chars(self, hex_data):
        words = []
        for i in range(0, len(hex_data), 4):
            word = bytes([int(hex_data[i:i+2], 16), int(hex_data[i+2:i+4], 16)]).decode('utf-16')
            if u'\u4e00' <= word <= u'\u9fa5':
                words.append(word)
            else:
                words = []
                break
        return words

    def parse(self, content):
        words = set([])
        hex_data = binascii.hexlify(content)
        hex_data = str(hex_data, encoding='utf-8')
        hex_data = hex_data[1696:]

        while True:
            wordCount = hex_data[0:2]
            wordCount = int(wordCount, 16)
            hex_data_part = hex_data[8+wordCount*4:8+wordCount*8]
            chars = self.hex2chars(hex_data_part)
            if len(chars) < 1:
                break
            word = ''.join(chars)
            words.add(word)
            hex_data = hex_data[8+wordCount*8:]
            if len(hex_data) < 1:
                break
        return list(words)

    def parse_file(self, fileName):
        with open(fileName, "rb") as f:
            content = f.read()
        words = self.parse(content)
        return words

bdict_parser = BdictParser()
