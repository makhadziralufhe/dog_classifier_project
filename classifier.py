"""
classifier.py

Stand-in for the real classifier() function normally supplied by the course
(which loads a torchvision ResNet-18, AlexNet or VGG-16 pretrained on
ImageNet and returns its top-1 label for an image). Building this project
here has no network access to download those weights or a real photo
dataset, so this file returns pre-recorded labels from demo_data.py instead.

The *signature and calling convention are the real ones* used throughout the
project: classifier(path_to_image, model_name) -> label (str). Every other
file (classify_images.py, check_images.py, the notebooks) calls it exactly
the way it would call the real function, so swapping this file out for the
real implementation later requires no other changes.

    from classifier import classifier
    image_classification = classifier(images_dir + filename, model_name)
"""

import os
from demo_data import PET_IMAGES, CONFUSABLE, MISTAKES, CROSS_LINE

_VALID_MODELS = ("resnet", "alexnet", "vgg")


def classifier(path_to_image, model_name):
    """
    Pretends to run `path_to_image` through the named pretrained CNN and
    returns its predicted label, exactly as the real classifier() does.

    Parameters:
     path_to_image - path to the image, e.g. "pet_images/Beagle_01.jpg"
     model_name - one of 'resnet', 'alexnet', 'vgg'

    Returns:
     label - the model's predicted class label (str, as the raw model would
             return it -- classify_images.py is responsible for lowercasing
             and stripping it, matching the real project's division of work)
    """
    if model_name not in _VALID_MODELS:
        raise ValueError(f"Unknown model architecture '{model_name}'. Expected one of {_VALID_MODELS}.")

    filename = os.path.basename(path_to_image)
    if filename not in PET_IMAGES:
        raise FileNotFoundError(
            f"'{path_to_image}' is not one of the sample images this demo classifier knows about."
        )

    true_label = PET_IMAGES[filename]

    # A hard case that crosses the dog / not-dog line for this architecture.
    crossed = CROSS_LINE.get(model_name, {})
    if filename in crossed:
        return crossed[filename]

    # An ordinary same-side mistake (wrong breed / wrong object, but on the
    # correct side of the dog / not-dog line).
    if filename in MISTAKES.get(model_name, set()):
        return CONFUSABLE[true_label]

    # Otherwise the model "gets it right".
    return true_label
