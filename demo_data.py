"""
Single source of truth for the sample dataset used in this project.

Because this build has no internet access to download the 25,000-image
ImageNet-trained ResNet/AlexNet/VGG weights, `classifier.py` cannot call a
real pretrained CNN. Instead this file defines a small, fully self-contained
"pretend classifier" truth table: for each of the 40 sample images, and for
each of the three architectures, it records what that architecture is
pretending to have seen.

The table is hand-designed (not random) so that it reproduces the same kinds
of outcomes a real run against real pretrained models produces:
  - most dog photos are classified correctly (label matches exactly)
  - some dog photos are classified as the WRONG breed (still a dog -> counts
    toward "correctly a dog" but not "correct breed")
  - a couple of harder images are misclassified across the dog/not-dog line
    in both directions, to exercise every branch of adjust_results4_isadog
  - accuracy differs by architecture, the same way it does with the real
    pretrained models: VGG is best on breed match, AlexNet weakest, ResNet
    in between.

Swap `classifier.py` back to a real torchvision call and this file is no
longer needed once you have internet access and the pet_images/ dataset.
"""

# Each entry: filename -> pet_label (the true content, used to build both the
# placeholder image and the filename students' get_pet_labels() must parse
# back out of the filename itself).
PET_IMAGES = {
    # ---- dogs (30 images across 10 breeds, 3 photos each) ----------------
    "Beagle_01.jpg": "beagle",
    "Beagle_02.jpg": "beagle",
    "Beagle_03.jpg": "beagle",
    "Boxer_01.jpg": "boxer",
    "Boxer_02.jpg": "boxer",
    "Boxer_03.jpg": "boxer",
    "Chihuahua_01.jpg": "chihuahua",
    "Chihuahua_02.jpg": "chihuahua",
    "Chihuahua_03.jpg": "chihuahua",
    "Collie_01.jpg": "collie",
    "Collie_02.jpg": "collie",
    "Collie_03.jpg": "collie",
    "Golden_retriever_01.jpg": "golden retriever",
    "Golden_retriever_02.jpg": "golden retriever",
    "Golden_retriever_03.jpg": "golden retriever",
    "German_shepherd_01.jpg": "german shepherd",
    "German_shepherd_02.jpg": "german shepherd",
    "German_shepherd_03.jpg": "german shepherd",
    "Great_dane_01.jpg": "great dane",
    "Great_dane_02.jpg": "great dane",
    "Great_dane_03.jpg": "great dane",
    "Poodle_01.jpg": "poodle",
    "Poodle_02.jpg": "poodle",
    "Poodle_03.jpg": "poodle",
    "Pug_01.jpg": "pug",
    "Pug_02.jpg": "pug",
    "Pug_03.jpg": "pug",
    "Saint_bernard_01.jpg": "saint bernard",
    "Saint_bernard_02.jpg": "saint bernard",
    "Saint_bernard_03.jpg": "saint bernard",
    # ---- not-dogs (10 images) --------------------------------------------
    "Fox_squirrel_01.jpg": "fox squirrel",
    "Persian_cat_01.jpg": "persian cat",
    "Rabbit_01.jpg": "rabbit",
    "Tiger_01.jpg": "tiger",
    "Cardinal_01.jpg": "cardinal",
    "Box_turtle_01.jpg": "box turtle",
    "Guitar_01.jpg": "guitar",
    "Sports_car_01.jpg": "sports car",
    "Sailboat_01.jpg": "sailboat",
    "Daisy_01.jpg": "daisy",
}

# Confusable "wrong but plausible" labels used to deliberately create
# mismatches (still same dog/not-dog side) for specific files.
CONFUSABLE = {
    "beagle": "walker hound",
    "boxer": "bull mastiff",
    "chihuahua": "toy terrier",
    "collie": "shetland sheepdog",
    "golden retriever": "labrador retriever",
    "german shepherd": "malinois",
    "great dane": "mastiff",
    "poodle": "afghan hound",
    "pug": "pekinese",
    "saint bernard": "bernese mountain dog",
    "fox squirrel": "eastern gray squirrel",
    "persian cat": "angora cat",
    "rabbit": "hare",
    "tiger": "leopard",
    "cardinal": "bullfinch",
    "box turtle": "mud turtle",
    "guitar": "banjo",
    "sports car": "convertible",
    "sailboat": "catamaran",
    "daisy": "sunflower",
}

# For each architecture: filenames that get the CONFUSABLE label instead of
# the correct one, i.e. deliberate classifier "mistakes". Anything not
# listed here is classified correctly by that architecture.
MISTAKES = {
    "resnet": {
        "Poodle_02.jpg",        # breed mismatch (still a dog)
        "Tiger_01.jpg",         # not-dog mismatch (still not-a-dog)
    },
    "alexnet": {
        # AlexNet is the weakest at breed identification.
        "Boxer_02.jpg",
        "Collie_01.jpg",
        "Poodle_01.jpg",
        "Poodle_02.jpg",
        "Saint_bernard_03.jpg",
        "Persian_cat_01.jpg",   # this one crosses the dog line, see below
    },
    "vgg": {
        "Chihuahua_03.jpg",     # single breed mismatch, VGG is strongest
    },
}

# Hard cases that cross the dog / not-dog line in one specific architecture
# only, so every branch of adjust_results4_isadog gets exercised somewhere
# across the three model runs:
#   - a real dog photo that a model mistakes for something that is NOT a dog
#   - a real not-dog photo that a model mistakes for a dog breed
CROSS_LINE = {
    "alexnet": {
        "Persian_cat_01.jpg": "toy poodle",   # not-dog misclassified AS a dog
        "Great_dane_03.jpg": "wild boar",     # dog misclassified as NOT a dog
    },
}
