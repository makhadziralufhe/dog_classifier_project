"""
print_results.py

Defines print_results(), which prints the summary statistics for a model
run, and optionally lists every image where the pet label and classifier
label disagreed (for dog-detection misses and/or breed misses).
"""


def print_results(
    results_dic,
    results_stats_dic,
    model,
    print_incorrect_dogs=False,
    print_incorrect_breed=False,
):
    """
    Prints summary results for one classification run, and optionally the
    detail for every image that was misclassified.

    Parameters:
     results_dic - dictionary from adjust_results4_isadog()
     results_stats_dic - dictionary from calculates_results_stats()
     model - the CNN model architecture used, e.g. 'vgg'
     print_incorrect_dogs - True prints all images where the pet image is a
                            dog but the classifier's label is NOT a dog, or
                            vice versa (default False)
     print_incorrect_breed - True prints all images where the pet image and
                             the classifier both agree it's a dog, but the
                             breed doesn't match (default False)

    Returns:
     None
    """
    print(f"\n*** Results Summary for CNN Model Architecture: {model.upper()} ***")
    print(f"{results_stats_dic['n_images']:2d} images")
    print(f"{results_stats_dic['n_dogs_img']:2d} images of dogs")
    print(f"{results_stats_dic['n_notdogs_img']:2d} images of not-a-dog")

    print(f"\n{'% Match:':22s} {results_stats_dic['pct_match']:5.1f}%")
    print(f"{'% Correct Dogs:':22s} {results_stats_dic['pct_correct_dogs']:5.1f}%")
    print(f"{'% Correct Breed:':22s} {results_stats_dic['pct_correct_breed']:5.1f}%")
    print(f"{'% Correct Not-Dogs:':22s} {results_stats_dic['pct_correct_notdogs']:5.1f}%")

    if print_incorrect_dogs and (
        results_stats_dic["n_correct_dogs"] + results_stats_dic["n_correct_notdogs"]
        != results_stats_dic["n_images"]
    ):
        print("\nINCORRECT Dog/Not-Dog Assignments:")
        for key in results_dic:
            pet_label, classifier_label, _, pet_is_dog, classifier_is_dog = results_dic[key]
            if pet_is_dog != classifier_is_dog:
                print(f"Real: {pet_label:>25s}   Classifier: {classifier_label:s}")

    if print_incorrect_breed:
        has_breed_miss = False
        for key in results_dic:
            pet_label, classifier_label, is_match, pet_is_dog, classifier_is_dog = results_dic[key]
            if pet_is_dog and classifier_is_dog and not is_match:
                has_breed_miss = True
                break

        if has_breed_miss:
            print("\nINCORRECT Dog Breed Assignments:")
            for key in results_dic:
                pet_label, classifier_label, is_match, pet_is_dog, classifier_is_dog = results_dic[key]
                if pet_is_dog and classifier_is_dog and not is_match:
                    print(f"Real: {pet_label:>25s}   Classifier: {classifier_label:s}")
