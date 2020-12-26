class Permutation:
    def __init__(self, words: list):
        self.words = words
        self.size = len(words)

    def get_size(self):
        return self.size

    def get_words(self):
        return self.words

    def get_word_size(self):
        return len(self.words[0])

def permut(word: str = '', letters: str = '', max: int = None, save: list = None) -> None:
    n = len(letters)
    if n == 0 or (max and len(word) > max):
        if save:
            save.append(word)
        else:
            print(word)
        return None

    arr = list(letters)

    for i, l in enumerate(arr):
        letters_aux = arr.copy()
        del letters_aux[i]
        permut(word + l, ''.join(letters_aux), max, save)


def make_permutations(l: str = '', m: int = None) -> Permutation:
    arr = ['']
    permut(letters=l, max=m, save=arr)
    arr = arr[1:]
    return Permutation(arr)


if __name__ == '__main__':
    perm = make_permutations('iracema')
    print(perm.get_size())
    print(perm.get_words())