import os
import glob
import nltk
from pre_process import process_dir


def pop_lists():
    ent = glob.glob(
    '/home/josh/Documents/COSC/projects/ML/datasets/bbc/entertainment/*.txt')

    biz = glob.glob(
    '/home/josh/Documents/COSC/projects/ML/datasets/bbc/business/*.txt')

    pol = glob.glob(
    '/home/josh/Documents/COSC/projects/ML/datasets/bbc/politics/*.txt')

    sport = glob.glob(
    '/home/josh/Documents/COSC/projects/ML/datasets/bbc/sport/*.txt')

    tech = glob.glob(
    '/home/josh/Documents/COSC/projects/ML/datasets/bbc/tech/*.txt')

    category_list = [ent, biz, pol, sport, tech]
    print type(category_list[0])
    return category_list

def create_output_dirs(lists):
    outdir ='/home/josh/Documents/COSC/projects/ML/datasets/bbc_processed/'
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for list in lists:
        path = str(outdir) + os.path.commonprefix(list).split('/')[-2] + '-processed'
        if not os.path.exists(path):
            os.makedirs(path)

def main():
    lists = pop_lists()
    create_output_dirs(lists)
    for dir in lists:
        process_dir(dir)










if __name__ == "__main__":
    main()
