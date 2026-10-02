"""
get_pet_labels.py

Defines get_pet_labels(), which builds the "results dictionary" from the
filenames in the pet images folder. Each filename encodes the true label of
the pet in the photo (e.g. "Poodle_07956.jpg" is a photo of a poodle); this
function extracts that label by stripping digits/extension and turning
underscores into spaces.
"""

import os


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on the filenames of the image
    files. These labels are used to check the accuracy of the classifier
    function, since the file names are assumed to be reliable ground truth.

    Parameters:
     image_dir - the path (as a string) to the folder of pet images

    Returns:
     results_dic - dictionary with 'key' = filename and 'value' = a
                   one-element list containing the pet label, e.g.
                   {'Poodle_07956.jpg': ['poodle'],
                    'fox_squirrel_01.jpg': ['fox squirrel'], ... }
    """
    filenames = [f for f in os.listdir(image_dir) if not f.startswith(".")]

    results_dic = dict()
    for filename in filenames:
        # Drop the extension, lowercase, split on underscores, and keep
        # only alphabetic tokens (this discards the trailing digits that
        # make each filename unique, e.g. "07956").
        name_no_ext = os.path.splitext(filename)[0]
        tokens = name_no_ext.lower().split("_")
        word_tokens = [t for t in tokens if t.isalpha()]
        pet_label = " ".join(word_tokens).strip()

        if filename not in results_dic:
            results_dic[filename] = [pet_label]

    return results_dic
