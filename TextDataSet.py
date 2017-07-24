import os
import glob
class TextDataSet:

    #TODO: add appending functions

    #construct Dataset from standard outermost dir organization
    def __init__(self, data_dict):
        dirs = [str(data_dict + '/' + x + '/') for x in os.listdir(data_dict)]
        self.dir_files = [glob.glob(str(x + '/*.txt')) for x in dirs]
        self.categories = [x.split('-')[0] for x in os.listdir(data_dict)]
        self.tag_dict = {y:x for x,y in dict(enumerate(self.categories)).iteritems()}

    def get_categories(self):
        return self.categories


    def get_file_cat(self, filename):
        return filename.split('/')[-2].split('-')[0]

    def get_filenames(self):
        return self.dir_files

    def get_tag(self, string):
        return self.tag_dict.get(string)

    def print_elems(self):
        #for x in self.categories:
        #    print x

        #print self.dir_files[0]

        print self.tag_dict

def get_file_cat(filename):
    return filename.split('/')[-2].split('-')[0]
