class Permutation:
    def __init__(self, words: list):
        words.sort()
        self.__words = words.copy()
        self.__size = len(words)
        self.__compare()

    def __compare(self):
        file = open('dictionary.txt', 'r')
        words = [i.replace('\n', '').lower() for i in file.readlines()]
        words.sort()
        self.__real_words = []
        for i, word in enumerate(self.__words):
            if self.__binary_search(words, word):
                if not word in self.__real_words:
                    self.__real_words.append(word)

    def __binary_search(self, arr: list, goal: str) -> bool:
        init = 0
        end = len(arr)
        while True:
            m = init + int((end - init) / 2)
            if arr[m] == goal:
                return True

            if arr[m] > goal:
                end = m

            elif arr[m] < goal:
                init = m

            if end - init <= 1:
                return False

    def get_size(self) -> int:
        return self.__size

    def get_words(self) -> [str]:
        return self.__words

    def get_word_size(self) -> int:
        return len(self.__words[0])

    def get_real_words(self) -> [str]:
        return self.__real_words

    def get_size_real(self) -> int:
        return len(self.__real_words)


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
    perm = make_permutations('amora')
    print(perm.get_size_real())
    print(perm.get_real_words())
