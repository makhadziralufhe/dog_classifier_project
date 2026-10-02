#!/bin/bash
#
# run_models_batch.sh
#
# Runs check_images.py once for each of the three CNN model architectures
# and saves each run's full output to its own text file.
#
#   sh run_models_batch.sh
#
mkdir -p results

python3 check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > results/resnet_pet-images.txt
python3 check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > results/alexnet_pet-images.txt
python3 check_images.py --dir pet_images/ --arch vgg     --dogfile dognames.txt > results/vgg_pet-images.txt

echo "Done. See results/resnet_pet-images.txt, results/alexnet_pet-images.txt, results/vgg_pet-images.txt"
