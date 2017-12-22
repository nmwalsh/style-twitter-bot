# run style transfer for statically named input image
cd ~/projects/fast-neural-style
th fast_neural_style.lua \
	-model models/eccv16/starry_night.t7 \
	-input_image ~/projects/style-twitter-bot/input_image.png \
	-output_image ~/projects/style-twitter-bot/output_images/out.png \
	-gpu 0
cd ~/projects/style-twitter-bot