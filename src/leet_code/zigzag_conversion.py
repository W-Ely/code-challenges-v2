class Solution:

    def _zig(self, i, num_rows):
        if ((i - 1) // (num_rows - 1)) % 2 == 0:
            return ((i - 1) % (num_rows - 1)) + 1

    def _zag(self, i, num_rows):
        return num_rows - (((i - 1) % (num_rows - 1)) + 2)

    def convert(self, characters, num_rows):
        if num_rows == 1:
            return characters
        bins = [[] for _ in range(num_rows)]
        for i, character in enumerate(characters):
            if bin_row := self._zig(i, num_rows):
                bins[bin_row].append(character)
            else:
                bins[self._zag(i, num_rows)].append(character)
        return "".join(["".join(bin) for bin in bins])
