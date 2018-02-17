function im = hybrid_image(im1, im2, cutoff_low, cutoff_high)

low_pass = imgaussfilt(im1, cutoff_low);
high_pass = imgaussfilt(im2, cutoff_high);

im = low_pass + im2 - high_pass;
end