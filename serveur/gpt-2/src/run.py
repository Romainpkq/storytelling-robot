from interactive_conditional_samples import model2


def run1(path1):
    """"
    generate 5 files and saved them
    param:
        path1: the path where saved the start of the text.
    """
    raw_text = "<|endoftext|>"      # add the indicator of the start of a story
    with open(path1, 'r', encoding='utf-8') as f1:
        for line in f1.readlines():
            raw_text += line

    model2.train(raw_text, 5)

    return


run1("/home/stu/pkq/gpt-2/samples/story_start/1_start.txt")
