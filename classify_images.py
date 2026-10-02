"""
classify_images.py

Defines classify_images(), which runs every pet image through the
classifier() function for the chosen CNN model architecture, and records
whether the classifier's label matches the pet image's true label.
"""

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Runs classifier() on every image in results_dic and appends the
    classifier's label and a match flag to that image's entry.

    Parameters:
     images_dir - path to the folder of pet images, ending in '/'
     results_dic - dictionary from get_pet_labels(); this function extends
                   each value list in place with
                   [pet_label, classifier_label, is_match]
     model - CNN model architecture to use: 'resnet', 'alexnet' or 'vgg'

    Returns:
     None - results_dic is mutated in place
    """
    for users_key in results_dic:
        # images_dir already ends in '/' (see get_input_args' default), so
        # the path is built by simple concatenation.
        classifier_label = classifier(images_dir + users_key, model)
        classifier_label = classifier_label.lower().strip()

        pet_label = results_dic[users_key][0]

        # A match only counts if pet_label appears in classifier_label as a
        # whole word (or whole comma-separated term), not as a substring of
        # some other word -- e.g. pet_label "pug" must not match inside
        # classifier_label "pugilist".
        found = classifier_label.find(pet_label)
        is_match = 0
        if found >= 0:
            starts_word = found == 0 or classifier_label[found - 1] in (" ", ",")
            end = found + len(pet_label)
            ends_word = end == len(classifier_label) or classifier_label[end] in (" ", ",")
            if starts_word and ends_word:
                is_match = 1

        results_dic[users_key].extend([classifier_label, is_match])
