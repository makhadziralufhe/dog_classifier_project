"""
adjust_results4_isadog.py

Defines adjust_results4_isadog(), which uses a file of valid dog breed
names to determine, for every image, whether the *pet label* and the
*classifier label* are each a dog -- independently of whether they matched
each other exactly.
"""


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adds two more elements to each value in results_dic: whether the pet
    image's true label is a dog (1) or not (0), and whether the
    classifier's label is a dog (1) or not (0). A breed name only counts as
    "a dog" if it appears in dogfile.

    Parameters:
     results_dic - dictionary from classify_images(); each value list is
                   [pet_label, classifier_label, is_match] and this function
                   extends it in place to
                   [pet_label, classifier_label, is_match,
                    pet_label_is_dog, classifier_label_is_dog]
     dogfile - path to a text file listing valid dog breed names, one per
               line, lowercase

    Returns:
     None - results_dic is mutated in place
    """
    dognames_dic = dict()
    with open(dogfile, "r") as f:
        for line in f:
            name = line.strip().lower()
            if name and name not in dognames_dic:
                dognames_dic[name] = 1

    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        pet_is_dog = 1 if pet_label in dognames_dic else 0

        # classifier_label may contain several comma-separated terms (a real
        # pretrained CNN often returns e.g. "beagle, walker hound"); it
        # counts as a dog if ANY of those terms is a known dog breed.
        classifier_is_dog = 0
        for term in classifier_label.split(","):
            if term.strip() in dognames_dic:
                classifier_is_dog = 1
                break

        results_dic[key].extend([pet_is_dog, classifier_is_dog])
