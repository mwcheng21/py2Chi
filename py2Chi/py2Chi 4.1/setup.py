from distutils.core import setup
import py2exe
setup(console=['py2Chi.py'])

##
##from distutils.core import setup
##import py2exe
##
##import sys; sys.argv.append('py2exe')
##
##py2exe_options = dict(
##                   bundle_files = 2,
##                   )
##
##setup(name='<py2Chi>',
##   version='1.0',
##   description='<pyMol to Chimera ProtCID Script converter>',
##   author='Micah Cheng',
##
##   console=['py2Chi.py'],
##   options={'py2exe': py2exe_options},
##   )
##
###setup(**setup_dict)
