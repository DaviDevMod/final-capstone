from functools import reduce


def add_prefix_un(word: str) -> str:
    return "un" + word


def make_word_groups(input_strings: list[str]) -> str:
    separator = " :: "
    prefix = input_strings[0]

    return reduce(
        lambda word_group, word: word_group + separator + prefix + word,
        input_strings,
    )


def remove_suffix_ness(word: str) -> str:
    if not word.endswith("ness"):
        raise ValueError('The input word must end in "ness".')

    return word[:-5] + "y" if word[:-4].endswith("i") else word[:-4]


def adjective_to_verb(sentence: str, index: int) -> str:
    punctuation = ",.;:?!'\""

    return sentence.split()[index].strip(punctuation) + "en"
