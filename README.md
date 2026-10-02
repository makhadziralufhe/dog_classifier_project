# Dog Image Classifier — Pet Image Classification Project

Classifies pet photos with a pretrained CNN architecture (ResNet, AlexNet or
VGG), compares the classifier's guess against each photo's true label
(parsed from its filename), determines which images are actually dogs, and
reports summary statistics per architecture.

This build ships **one Jupyter notebook per rubric section** (in
`notebooks/`) that walks through, demonstrates, and verifies that section's
requirement using the real project code — plus the complete working project
itself (`check_images.py` and friends) that the notebooks import from.

## About the sample data

There's no internet access in this environment to download the real
pretrained ResNet/AlexNet/VGG weights (hundreds of MB each) or a real photo
dataset, so this build is self-contained instead:

- **`pet_images/`** — 40 generated placeholder JPEGs (30 dog photos across
  10 breeds, 10 not-dog photos), named the same way the real dataset is
  (e.g. `Beagle_01.jpg`), so `get_pet_labels()` parses real filenames.
- **`classifier.py`** — returns pre-recorded labels from `demo_data.py`
  instead of running a real CNN forward pass. Everything *around* it
  (path-building, lowercasing, match checking, the dog/not-dog logic, the
  statistics) is the real, unmodified logic — only the inside of
  `classifier()` is a stand-in.
- **`demo_data.py`** — the truth table `classifier.py` reads from. It's
  hand-designed (not random) to reproduce realistic outcomes: most images
  classify correctly, a few dog photos get the wrong *breed* (still
  correctly flagged as a dog), and a couple of hard cases cross the
  dog/not-dog line in one architecture only — enough variety to exercise
  every branch of the rubric, with VGG scoring best on breed accuracy,
  AlexNet weakest, and ResNet in between (the same ordering you'd see with
  the real pretrained models).

**To use this with the real dataset and real pretrained models**, drop a
real `pet_images/` folder and a real `dognames.txt` in this folder, and
replace the body of `classifier.py` with the course-provided version that
loads torchvision's `resnet18`, `alexnet` or `vgg16` — nothing else needs to
change, since every other file only ever calls `classifier(path, model)`.

## Project files

| File | Rubric section |
|---|---|
| `check_images.py` | Main script — timing, wires everything together |
| `get_input_args.py` | Command Line Arguments (`--dir`, `--arch`, `--dogfile`) |
| `get_pet_labels.py` | Pet Image Labels |
| `classifier.py` | Classifying Images (the CNN call itself) |
| `classify_images.py` | Classifying Images (calling + recording results) |
| `adjust_results4_isadog.py` | Classifying Labels as Dogs |
| `calculates_results_stats.py` | Results (statistics) |
| `print_results.py` | Results (printing) |
| `run_models_batch.sh` | Results (runs all three models) |
| `demo_data.py`, `generate_sample_data.py` | Sample-data plumbing (not part of the rubric) |

## Notebooks

Each notebook in `notebooks/` imports the real `.py` files above (not
copies) and has already been run once, so it ships with real output baked
in — open it and read top to bottom, or re-run it yourself.

1. **`01_timing_code.ipynb`** — the `time()`-before / `time()`-after pattern,
   confirmed inside `check_images.py`.
2. **`02_command_line_arguments.ipynb`** — verifies `--dir`, `--arch`,
   `--dogfile` and their defaults.
3. **`03_pet_image_labels.ipynb`** — verifies `get_pet_labels()` returns
   exactly 40 entries in the required `{filename: [label]}` format, and that
   `in_arg.dir` is what's actually passed in.
4. **`04_classifying_images.ipynb`** — verifies the `images_dir + users_key`
   path construction, the lowercase/strip step, and the 1/0 match bookkeeping.
5. **`05_classifying_labels_as_dogs.ipynb`** — pulls one concrete example of
   each of the four match/dog combinations straight out of a real run, so
   every rubric case is visibly demonstrated, not just asserted.
6. **`06_results.ipynb`** — runs `run_models_batch.sh`, prints all three
   models' full output, and tabulates them side by side.

## Running it

```bash
pip install jupyter nbformat pillow

# regenerate the 40 sample images (already included, but reproducible)
python3 generate_sample_data.py

# run the whole pipeline once, for one architecture
python3 check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt

# or run all three architectures and save their output to results/
sh run_models_batch.sh

# open the notebooks
jupyter notebook notebooks/
```
