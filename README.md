<h2>Installation</h2>
<code>git clone https://github.com/altazur/ImageConverter.git</code>
<br>
<code>cd ImageConverter</code>
<br>
<code>pip install requirements.txt</code>
<h2>Usage</h2>
-C "JPG" converts File to Output with given format<br>
-R "128, 128" resizes File to Output with given dimension<br>
-F "Image.jpg" input file path<br>
-O "NewImage.jpg" output filte path<br>
<h1>Example</h1>
<h2>Convert jpg to png</h2>
<code>python ImageConverter.py -F "Image.jpg" -O "Converted.png" -C "png"</code>
<h2>Resize image to 128x128</h2>
<code>python ImageConverter.py -F "Image.jpg" -O "PreviewImage.jpg" -R "128,128"</code>
