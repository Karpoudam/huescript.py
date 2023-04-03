# huescript.py
A simple python script to use the Philips Hue API in order to check and change your lights' state.

# What for?
This script is intended to retrieve your Philips Hue data and then change a selected light's state.

## Warning!
Although this is a fairly simple script, it requires to have done a few steps to set up your Philips Hue API token. 
For more information about the required procedure, follow the steps here: https://developers.meethue.com/develop/get-started-2/

Once the setup is done, write down your **<BRIDGE_IP>** and your **<API_TOKEN>** somewhere safe as these two information will be needed.

# Setup
At the beginning, to avoid any error, you should turn the following lines into comments.
We will start by discovering the lights first, then you can uncomment the lines to change their states.

<div>
<p align="center">
  <img src="https://user-images.githubusercontent.com/73818280/229362599-b345d8c7-0728-4d44-9e2d-dbb013c5cc74.png">
</p>
<p align="center">Fig. 1: Line to comment</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/73818280/229362802-769f3c53-813d-4fb4-a1f0-0cf53578c3ad.png">
</p>
<p align="center">Fig. 2: More lines to comment</p>
</div>

The rest is pretty straightforward, you have to  replace the variables in **bridge_ip** and **username** by your **<BRIDGE_IP>** and your **<API_TOKEN>** respectively.

<p align="center">
  <img src="https://user-images.githubusercontent.com/73818280/229362126-99275235-4661-4229-9427-9fdec8bbe2e8.png">
</p>
<p align="center">Fig. 3: Variables to change</p>

Upon executing the script, you can see a similar message appear in your console:
<p align="center">
<img src="https://user-images.githubusercontent.com/73818280/229510527-25cace98-dc0c-4d14-99a8-de7ea2ba8136.png">
</p>
<p align="center">Fig. 4: Console logs after the first execution</p>

The numbers at the beginning of your console logs are your lights' ID. They are pretty useful as they are needed to change a selected light's state.
So now, you can uncomment the previously commented lines and replace the **<LIGHT_ID>** for the **"light_number"** variable with your selected ID.

Then, all you have to do is execute and ENJOY!

*Note*: Feel free to modify the script to be able to command multiple accessories at once or to dim the light.
<p align="center"><img src="https://user-images.githubusercontent.com/73818280/229363952-5857a4b4-01b6-4b2e-b893-e4c160d97284.png"></p>
<p align="center">Fig. 5: Example for dimming a light</p<
