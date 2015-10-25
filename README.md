# pcmanfm-custom-actions

All of these custom actions simply need to be dropped into 
/home/YOUR_USERNAME/.local/share/file-manager/actions

On a fresh install of Lubuntu, /file-manager/actions doesn't exist, so you'll
have to create it.

<b>[Set As Greeter Background]</b>

Required Files:
<ul>
	<li>Set As Greeter Background.desktop</li>
	<li>/modifyConfigFile/modifyConfigFile.py</li>
</ul>

Change LightDm Greeter background.

This one I created to easily change the lightdm greeter (login) background image. 
A couple steps do need to be taken before this one will work.  We need to 
install a single Python dependency to make this script work. First, open up a 
terminal:

<ol>
	<li>sudo apt-get install python-setuptools</li>
	<li>easy_install configobj</li>
</ol>

That's it, if you've already dropped the required files in your actions folder, 
simply log out, log back in, and right click a picture that you'd like to use as
your background, and select "Set As Greeter Background" from the menu.


<b>[Generate md5sum]</b>

Required Files:
	<ul>
		<li>md5sum.sh</li>
		<li>md5sum.desktop</li>
	</ul>

Easily generate a files md5sum in PcManFm.

This one I didn't create, I just modified a .desktop link to make it work with 
PcManFm actions.  Once you've dropped these files into your actions folder,
you need to make the md5sum.sh file executable, and install Zenity.  So open 
up a new terminal:

<ol>
	<li>cd ~/.local/share/file-manager/actions</li>
	<li>chmod +x md5sum.sh</li>
	<li>sudo apt-get install zenity</li>
</ol>

And now this one is ready to go!  Just log out and log back in to use it.
Attribution for this goes out to: shane <linuxmint.com>

<b>[Open Folder As Root]</b>

Got this from the Lubuntu site: <a href="http://lubuntu.me/tip-actions/">http://lubuntu.me/tip-actions/</a>


<b>[Set As Wallpaper]</b>

Got this from the Lubuntu site: <a href="http://lubuntu.me/tip-actions/">http://lubuntu.me/tip-actions/</a>
