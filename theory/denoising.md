# DENOISING

The ultimate goal is to supress the noise from the contaminated image.

## Noise

Unwanted modification of signal during capture,conversion,tramsforamtion,proecessing etc.Types of noise 
* Photon shot noise (scene dependent) - Random arrival of photons in the potential well due to Quantum nauture of the light.
  * number of photons detected with a pixel(photon bucket) per unit times is random.This is basically called photon flux.So we take the average photon flux of each pixel.
* Readout noise - converion of photons to voltage or electron flux during this conversion process(pre A/D conversion) the curcuit will add a bit of noise.During 
A/D conversion the continuous signal is converted to descrete signal with a bit sensitivity but rounding off.
* Other sorces - Dark current noise,fixed pattern noise,defective pixels etc

## Denoising using gaussian filter

Denoising using a average filter can cause degradation of image by treating all the neighbouring pixles equally which leads to loss in inforamtion.So a gaussian filter
with distributed weights (weights decrease as we move away from the center pixelis used)(while maintaing the energy of the image) can be used.This i bascially a low pass 
filter which is used for supressing high frequency componets of image by blurring

But edge detail can be lost as its a linear filter.

## Denoising using median filter

Here a median value is used to replace the corrupted pixel.By using this impulsive noise(salt and pepper noise)(cause moslty due to quality of harware and sensor)
and edges can be preserved.

## Denoising by non local means

