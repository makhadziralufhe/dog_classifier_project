"""
calculates_results_stats.py

Defines calculates_results_stats(), which tallies up the per-image results
built by get_pet_labels(), classify_images() and adjust_results4_isadog()
into whole-run counts and percentages.
"""


def calculates_results_stats(results_dic):
    """
    Calculates summary statistics for the whole run: how many images were
    dogs vs. not-dogs, how many the classifier got right, and the resulting
    percentages.

    Parameters:
     results_dic - dictionary from adjust_results4_isadog(); each value list
                   is [pet_label, classifier_label, is_match,
                       pet_label_is_dog, classifier_label_is_dog]

    Returns:
     results_stats_dic - dictionary of run statistics:
        n_images            total number of images
        n_dogs_img          number of images that are actually dogs
        n_notdogs_img       number of images that are actually not dogs
        n_match             number of images where labels matched exactly
        n_correct_dogs      number of dog images correctly classified as dogs
        n_correct_notdogs   number of not-dog images correctly classified
                             as not dogs
        n_correct_breed     number of dog images with the correct breed
        pct_match           % of images where labels matched exactly
        pct_correct_dogs    % of dog images correctly classified as dogs
        pct_correct_breed   % of dog images with the correct breed
        pct_correct_notdogs % of not-dog images correctly classified as
                             not dogs
    """
    results_stats_dic = dict()

    results_stats_dic["n_images"] = len(results_dic)
    results_stats_dic["n_dogs_img"] = 0
    results_stats_dic["n_notdogs_img"] = 0
    results_stats_dic["n_match"] = 0
    results_stats_dic["n_correct_dogs"] = 0
    results_stats_dic["n_correct_notdogs"] = 0
    results_stats_dic["n_correct_breed"] = 0

    for key in results_dic:
        _, _, is_match, pet_is_dog, classifier_is_dog = results_dic[key]

        if is_match:
            results_stats_dic["n_match"] += 1

        if pet_is_dog:
            results_stats_dic["n_dogs_img"] += 1
            if classifier_is_dog:
                results_stats_dic["n_correct_dogs"] += 1
            if is_match:
                results_stats_dic["n_correct_breed"] += 1
        else:
            results_stats_dic["n_notdogs_img"] += 1
            if not classifier_is_dog:
                results_stats_dic["n_correct_notdogs"] += 1

    n_dogs = results_stats_dic["n_dogs_img"]
    n_notdogs = results_stats_dic["n_notdogs_img"]

    results_stats_dic["pct_match"] = (
        results_stats_dic["n_match"] / results_stats_dic["n_images"] * 100.0
    )
    results_stats_dic["pct_correct_dogs"] = (
        results_stats_dic["n_correct_dogs"] / n_dogs * 100.0 if n_dogs else 0.0
    )
    results_stats_dic["pct_correct_breed"] = (
        results_stats_dic["n_correct_breed"] / n_dogs * 100.0 if n_dogs else 0.0
    )
    results_stats_dic["pct_correct_notdogs"] = (
        results_stats_dic["n_correct_notdogs"] / n_notdogs * 100.0 if n_notdogs else 0.0
    )

    return results_stats_dic
