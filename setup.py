import setuptools

with open("README.md", "r", encoding="utf-8") as fh:

    long_description = fh.read()

setuptools.setup(

     name='whmsslinstall',  

     version='0.2',

     scripts=['bin/sslinstall'] ,

     author="James Rosado",

     author_email="dev@twmsllc.com",

     description= ("An Application to order and "
        "install Comodo DV SSL Certificates"
     ),

     long_description=long_description,

    long_description_content_type="text/markdown",

     url="https://github.com/twmsllc/whm-ssl-autoinstall",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: GNU General Public License",

         "Operating System :: CentOS 6+",

         "CPanel :: EasyApache4+ "

     ],

 )