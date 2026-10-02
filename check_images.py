#!/usr/bin/env python3
"""
check_images.py

Main script for the project: classifies pet images using a pretrained CNN
model architecture, compares the classifier's labels against each pet
image's true label (parsed from its filename), determines which images are
of dogs, and reports overall statistics -- all timed start to finish.

Usage:
    python3 check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
"""

from time import time

from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    # ---- Start timer, before any of the main logic runs -------------------
    start_time = time()

    in_arg = get_input_args()

    results_dic = get_pet_labels(in_arg.dir)

    classify_images(in_arg.dir, results_dic, in_arg.arch)

    adjust_results4_isadog(results_dic, in_arg.dogfile)

    results_stats_dic = calculates_results_stats(results_dic)

    print_results(
        results_dic,
        results_stats_dic,
        in_arg.arch,
        print_incorrect_dogs=True,
        print_incorrect_breed=True,
    )

    # ---- Stop timer, after all the main logic has finished -----------------
    end_time = time()

    tot_time = end_time - start_time
    hours = int(tot_time / 3600)
    minutes = int((tot_time % 3600) / 60)
    seconds = int(tot_time % 60)
    print(
        "\n** Total Elapsed Runtime:",
        f"{hours:02d}:{minutes:02d}:{seconds:02d}",
    )


if __name__ == "__main__":
    main()
