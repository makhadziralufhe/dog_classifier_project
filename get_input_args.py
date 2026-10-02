"""
get_input_args.py

Defines get_input_args(), which creates and parses the command line
arguments for check_images.py using argparse. Enables three arguments:

  --dir      path to the folder of pet images      (default 'pet_images/')
  --arch     CNN model architecture to use          (default 'vgg')
  --dogfile  text file with valid dog breed names    (default 'dognames.txt')
"""

import argparse


def get_input_args():
    """
    Retrieves and parses command line arguments for check_images.py.

    Parameters:
     None - argparse reads sys.argv directly

    Returns:
     parse_args() -- an argparse.Namespace object with attributes
                      in_arg.dir, in_arg.arch, in_arg.dogfile
    """
    parser = argparse.ArgumentParser(
        description="Classify pet images using a pretrained CNN model and "
        "compare the classifier's results to the pet image's true label."
    )

    parser.add_argument(
        "--dir",
        type=str,
        default="pet_images/",
        help="path to the folder of pet images (default: pet_images/)",
    )
    parser.add_argument(
        "--arch",
        type=str,
        default="vgg",
        choices=["resnet", "alexnet", "vgg"],
        help="CNN model architecture to use for classification: "
        "resnet, alexnet or vgg (default: vgg)",
    )
    parser.add_argument(
        "--dogfile",
        type=str,
        default="dognames.txt",
        help="text file containing valid dog breed names, one per line "
        "(default: dognames.txt)",
    )

    return parser.parse_args()
